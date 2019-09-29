# coding=utf-8
import pickle
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from rasa_nlu.model import Interpreter
import json

def predict(sentence,classifier):
	prediction = classifier.predict(sentence)
	return prediction


def getWordbag(word_array,sentence):
	bag = [0]*len(word_array)
	for word in (str(sentence).split()):
		if(word in word_array):
			bag[(word_array.index(word))] = 1
	return bag


def gettfidf(sentence_list):
	X_train_counts = csr_matrix(sentence_list)
	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	return X_train_tfidf

def generateWordBags(corpus,word_array):
	sentence_bags = []
	for sentence in corpus:
		bag = [0]*len(word_array)
		for word in (str(sentence).split()):
			if(word in word_array):
				bag[(word_array.index(word))] = 1
		sentence_bags.append(bag)	
	return sentence_bags

def loadmodels():
		
	filenameSVM = '../custom_nlu_models/finalized_model_SVM.sav'
	filenameNB = '../custom_nlu_models/finalized_model_NB.sav'
	filenameLR = '../custom_nlu_models/finalized_model_LR.sav'

	loaded_model_SVM = pickle.load(open(filenameSVM, 'rb'))
	loaded_model_NB = pickle.load(open(filenameNB, 'rb'))
	loaded_model_LR = pickle.load(open(filenameLR, 'rb'))

	with open('../vocab.data', 'rb') as filehandle:
	# read the data as binary data stream
		word_array_read = pickle.load(filehandle)
	return loaded_model_SVM,loaded_model_NB,loaded_model_LR,word_array_read


def predictEnsemble(loaded_model_SVM,loaded_model_NB,loaded_model_LR,sentence_tfidf,bag,sentence):
	predSVM = predict(sentence_tfidf,loaded_model_SVM)[0]
	predNB = predict(sentence_tfidf.toarray(),loaded_model_NB)[0]
	predLR = predict([bag],loaded_model_LR)[0]

	confSVM =  (max(loaded_model_SVM.predict_proba(sentence_tfidf)[0]))
	confNB = (max(loaded_model_NB.predict_proba(sentence_tfidf.toarray())[0]))
	confLR = (max(loaded_model_LR.predict_proba([bag])[0]))


	print(predSVM," ",predNB," ",predLR)
	print(confSVM," ",confNB," ",confLR)


	# accuracy = accuracy_score(labels_test, pred)

	# word_embedding_result = interpreter.parse(sentence)
	# intent_from_embedding = word_embedding_result['intent']['name']


	l = [predSVM,predNB,predLR]
	conf = [confSVM,confNB,confLR]
	returned_conf = max(conf)



	if(l[0] != l[1] and l[1]!=l[2] and l[0] != l[2]):
		most_voted = l[(conf.index(max(conf)))]

	else:
		most_voted = max(set(l), key = l.count)

	if(min(conf)<0.5):
		returned_conf = min(conf)

	# most_voted = max(set(l), key = l.count)
	# return most_voted
	return most_voted, returned_conf

def mapIntentDescription(intent_num):
    mapper = {
        "1" : "open a new bank account",
        "2" : "savings account",
        "3" : "fixed account",
        "4": "account type",
        "5": "selection",
        "6": "try again",
        "7": "don't try again",
        "8": "correct detailas",
        "9": "incorrect details",
        "10": "confirmation",
        "11": "not confirmation",
        "12": "number of months",
        "13": "after completion",
        "14": "monthly"
}

    return mapper[str(intent_num)]


def predictIntent(sentence):

	# interpreter = Interpreter.load("./models/current/nlu")
	# file_read = open('test_sentences','r')
	#
	# test = pd.read_csv("testset.csv")
	# test_corpus = list(test.utter)
	# test_labels = list(test.intent)

	# print("sentence",sentence)
	loaded_model_SVM,loaded_model_NB,loaded_model_LR,word_array_read = loadmodels()

	# for line in file_read:
	# sentence = line
	sentence_bag = getWordbag(word_array_read,sentence)
	sentence_tfidf = gettfidf([sentence_bag])
	most_voted, conf = predictEnsemble(loaded_model_SVM,loaded_model_NB,loaded_model_LR,sentence_tfidf,sentence_bag,sentence)
	# print("intent",most_voted)
	print("sentence", sentence)
	return mapIntentDescription(most_voted), conf


# print(predictIntent("මට නව ගිණුමක් විවෘත කරන්න ඕන"))



