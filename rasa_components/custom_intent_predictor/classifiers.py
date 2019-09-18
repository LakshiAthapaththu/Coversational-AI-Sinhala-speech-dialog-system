import numpy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import random
from keras.layers import Input, Embedding, Dot, Reshape, Dense
from keras.models import Model
from sklearn.linear_model import LogisticRegression
from numpy import array, matrix
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import SGDClassifier
import pickle
from sklearn import svm, datasets


def readData():
	data = pd.read_csv("TrainingCorpus.csv")
	test = pd.read_csv("testset.csv")
	return data,test


def getCorpus(corpus):
	word_array = []
	for sentence in corpus:
		word_array.extend(str(sentence).split())
		word_array = (set(word_array))
		word_array= list(word_array)

	return word_array

def generateWordBags(corpus,word_array):
	sentence_bags = []
	for sentence in corpus:
		bag = [0]*len(word_array)
		for word in (str(sentence).split()):
			if(word in word_array):
				bag[(word_array.index(word))] = 1
		sentence_bags.append(bag)
	return sentence_bags


def trainClassifiers(word_bags,label_bags,X_train_tfidf):
	LRclassifier = LogisticRegression()
	LRclassifier.fit(word_bags,label_bags)
	NBclassifier = MultinomialNB().fit(X_train_tfidf, label_bags)
	SVMclassifier = SGDClassifier().fit(X_train_tfidf, label_bags)

	return LRclassifier,NBclassifier,SVMclassifier


def scoreClassifier(word_bags_test,label_bags_test,classifier):
	score = classifier.score(word_bags_test,label_bags_test)
	return score




def gettfidf(sentence_list):
	X_train_counts = csr_matrix(sentence_list)
	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	return X_train_tfidf

def getWordbag(word_array,sentence):
	bag = [0]*len(word_array)
	for word in (str(sentence).split()):
		if(word in word_array):
			bag[(word_array.index(word))] = 1
	return bag


def predict(sentence,classifier):
	prediction = classifier.predict(sentence)
	return prediction


def trainSVM(training_labels,X_train_tfidf,X_test_tfidf,test_labels):
	#which type of hyperplane to seperate the data linear means line in 2D
	kernels = ["linear", "rbf", "poly"]
	#gamma is a parameter for non linear hyperplanes The higher the gamma value it tries to exactly fit the training data set
	gammas = [0.00001,0.0001,0.001,0.01,0.1,1,10,25,50,75,100,250,500,1000,5000,10000]
	#C is the penalty parameter of the error term. It controls the trade off between smooth decision boundary and classifying the training points correctly.
	s = [0.0001,0.001, 0.10, 0.1, 1,10, 25, 50, 100, 1000]

	hyperparameters = dict(kernel=kernels,gamma=gammas,C=s)
	svc = svm.SVC()

	clf = GridSearchCV(svc, hyperparameters, cv=20, verbose=0)
	best_model = clf.fit(X_train_tfidf, training_labels)
	print('Best Parameters', clf.best_params_)
	c = clf.best_params_['C']
	kernal = clf.best_params_['kernel']
	gamma = clf.best_params_['gamma']


	svc = svm.SVC(kernel = kernal, gamma = gamma, C = c, probability=True).fit(X_train_tfidf, training_labels)
	# scoreSVM = svc.score(X_test_tfidf,test_labels)
	# print("Score is: ", scoreSVM)
	return svc

def trainNB(X_train_tfidf, label_bags,X_test_tfidf,test_labels):

	gnb = GaussianNB()
	# mnb = MultinomialNB()
	# MNBclassifier = mnb.fit(X_train_tfidf, label_bags)
	GNBclassifier = gnb.fit(X_train_tfidf.toarray(), label_bags)
	# bnb = BernoulliNB()
	# BNBclassifier = bnb.fit(X_train_tfidf.toarray(), label_bags)
	return GNBclassifier


	# score1 = MNBclassifier.score(X_test_tfidf,test_labels)
	# score2 = GNBclassifier.score(X_test_tfidf.toarray(),test_labels)
	# score3 = BNBclassifier.score(X_test_tfidf.toarray(),test_labels)
	# print(score1)
	# print(score2)
	# print(score3)

	# print(cross_val_score(gnb,X_train_tfidf.toarray() , label_bags, scoring='accuracy', cv=10).mean())
	# print(cross_val_score(mnb, X_train_tfidf.toarray(), label_bags, scoring='accuracy', cv=10).mean())


def trainLR(word_bags,label_bags,word_bags_test, label_bags_test):
	C_param_range = [0.0001,0.001, 0.01, 0.1, 1, 10, 100]
	panalties = ['l2','l1']
	hyperparameters = dict(penalty=panalties,C=C_param_range)
	lr = LogisticRegression()
	clf = GridSearchCV(lr, hyperparameters, cv=20, verbose=0)
	clf.fit(word_bags,label_bags)
	# print('Best Parameters', clf.best_params_)

	c = clf.best_params_['C']
	panelty = clf.best_params_['penalty']

	LRClassifier = LogisticRegression(penalty=panelty, C=c, random_state=0,solver='newton-cg')
	LRClassifier.fit(word_bags, label_bags)
	# score = LRClassifier.score(word_bags_test, label_bags_test)
	# print(score)

	return LRClassifier

	# for i in C_param_range:
	# 	# Apply logistic regression model to training data
	# 	lr = LogisticRegression(penalty='l2', C=i, random_state=0)
	# 	lr.fit(word_bags,label_bags)
	# 	score = lr.score(word_bags_test, label_bags_test)
	# 	print(score)


training,test = readData()

training_corpus = list(training.utter)
training_labels = list(training.intent)

test_corpus = list(test.utter)
test_labels = list(test.intent)


word_array = (getCorpus(training_corpus))
training_sentence_bag = (generateWordBags(training_corpus,word_array))
test_sentence_bag = (generateWordBags(test_corpus,word_array))



X_train_tfidf = gettfidf(training_sentence_bag)
X_test_tfidf = gettfidf(test_sentence_bag)


SVMClassifier = trainSVM(training_labels,X_train_tfidf,X_test_tfidf,test_labels)
NBClassifier = trainNB(X_train_tfidf,training_labels,X_test_tfidf,test_labels)
LRClassifier = trainLR(training_sentence_bag,training_labels,test_sentence_bag,test_labels)



filenameSVM = '../custom_nlu_models/finalized_model_SVM.sav'
filenameNB = '../custom_nlu_models/finalized_model_NB.sav'
filenameLR = '../custom_nlu_models/finalized_model_LR.sav'

pickle.dump(NBClassifier, open(filenameNB, 'wb'))
pickle.dump(SVMClassifier, open(filenameSVM, 'wb'))
pickle.dump(LRClassifier, open(filenameLR, 'wb'))

with open('../vocab.data', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(word_array, filehandle)













