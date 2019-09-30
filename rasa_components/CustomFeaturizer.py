from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfTransformer
import pickle

import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import sys

class Featurizer(Component):
    """A pre-trained sentiment component"""

    name = "Featurizer"
    provides = ["feature_vector","feature_vector_tfidf"]
    requires = ["tokens"]
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(Featurizer, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def loadmodels(self):
        with open('../vocab.data', 'rb') as filehandle:
            # read the data as binary data stream
            word_array_read = pickle.load(filehandle)
        return word_array_read

    def getWordbag(self,word_array, tokens):
        bag = [0] * len(word_array)
        for word in tokens:
            if (word in word_array):
                bag[(word_array.index(word))] = 1
        return bag

    def gettfidf(self, sentence_list):
        X_train_counts = csr_matrix(sentence_list)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        return X_train_tfidf

    def getFeaturizedSentence(self,tokens):
        word_array_read = self.loadmodels()
        sentence_bag = self.getWordbag(word_array_read, tokens)
        sentence_tfidf = self.gettfidf([sentence_bag])
        return sentence_bag,sentence_tfidf


    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""
        # print (self.getFeaturizedSentence((message.get("tokens"))))
        sentence_bag, sentence_tfidf = self.getFeaturizedSentence(message.get("tokens"))
        message.set("feature_vector", sentence_bag, add_to_output=True)
        message.set("feature_vector_tfidf", sentence_tfidf, add_to_output=True)

    def persist(path, project_name, fixed_model_name):
        """Pass because a pre-trained model is already persisted"""

        pass
