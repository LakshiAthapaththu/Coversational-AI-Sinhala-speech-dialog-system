from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
import pickle
import nltk
import os
import sys

class IntentClassifier(Component):

    name = "IntentClassifier"
    provides = ["intent_number","confident"]
    requires = ["feature_vector","feature_vector_tfidf"]
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(IntentClassifier, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        pass

    def loadmodels(self):
        filenameSVM = '../custom_nlu_models/finalized_model_SVM.sav'
        filenameNB = '../custom_nlu_models/finalized_model_NB.sav'
        filenameLR = '../custom_nlu_models/finalized_model_LR.sav'

        loaded_model_SVM = pickle.load(open(filenameSVM, 'rb'))
        loaded_model_NB = pickle.load(open(filenameNB, 'rb'))
        loaded_model_LR = pickle.load(open(filenameLR, 'rb'))

        with open('../vocab.data', 'rb') as filehandle:
            # read the data as binary data stream
            word_array_read = pickle.load(filehandle)
        return loaded_model_SVM, loaded_model_NB, loaded_model_LR, word_array_read

    def predict(self, sentence, classifier):
        prediction = classifier.predict(sentence)
        return prediction

    def predictEnsemble(self,loaded_model_SVM, loaded_model_NB, loaded_model_LR, sentence_tfidf, bag):
        predSVM = self.predict(sentence_tfidf, loaded_model_SVM)[0]
        predNB = self.predict(sentence_tfidf.toarray(), loaded_model_NB)[0]
        predLR = self.predict([bag], loaded_model_LR)[0]

        confSVM = (max(loaded_model_SVM.predict_proba(sentence_tfidf)[0]))
        confNB = (max(loaded_model_NB.predict_proba(sentence_tfidf.toarray())[0]))
        confLR = (max(loaded_model_LR.predict_proba([bag])[0]))

        l = [predSVM, predNB, predLR]
        conf = [confSVM, confNB, confLR]
        returned_conf = max(conf)

        if (l[0] != l[1] and l[1] != l[2] and l[0] != l[2]):
            most_voted = l[(conf.index(max(conf)))]

        else:
            most_voted = max(set(l), key=l.count)

        if (min(conf) < 0.5):
            returned_conf = min(conf)
        return most_voted, returned_conf

    def process(self, message, **kwargs):

        loaded_model_SVM, loaded_model_NB, loaded_model_LR, word_array_read = self.loadmodels()


        sentence_bag = message.get("feature_vector")
        sentence_tfidf = message.get("feature_vector_tfidf")
        most_voted, conf = self.predictEnsemble(loaded_model_SVM, loaded_model_NB, loaded_model_LR, sentence_tfidf,sentence_bag)
        message.set("intent_number",most_voted, add_to_output=True)
        message.set("confident", conf, add_to_output=True)
        message.set("feature_vector","",  add_to_output=True)
        message.set("feature_vector_tfidf", "", add_to_output=True)


    def persist(path, project_name, fixed_model_name):
        pass
