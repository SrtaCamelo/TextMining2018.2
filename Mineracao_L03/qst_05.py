#Mineração de Texto 2018.2
#Raissa Camelo Salhab
#Lista 03, Questão 05

#------------------------Imports--------------------
import os
import nltk
from math import log
from math import exp
#------------------------Functions-----------------
#---------------------File Opener------------------
def sentenceSplitter(file):
    dtc = nltk.data.load('tokenizers/punkt/portuguese.pickle')
    sentences = dtc.tokenize(file.strip())
    return sentences

def readFile(path):
    f = open(path, 'r')
    my_file_data = f.read()
    f.close()
    return my_file_data

def fetchCorpus():
    corpusSentencesL = []
    corpusSentences = []
    path = "Noticias_Portugues"
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path,file)
        sentences = readFile(file_path)
        sentences = sentenceSplitter(sentences)
        corpusSentencesL.append(sentences)
    for sentenceList in corpusSentencesL:
        for sentence in sentenceList:
            corpusSentences.append(sentence)
    return corpusSentences

def toLower(sentences):
    sentences = [sentence.lower() for sentence in sentences]
    return sentences
def tokenizeSentences(sentences):
    tokens = [nltk.word_tokenize(sentence, language='portuguese') for sentence in sentences]
    return tokens

def unpack(corpus):
    word_list =[]
    for list in corpus:
        for word in list:
            word_list.append(word)
    return word_list

def calculateFrequency(fdist):
    word_freq = []
    for word, frequency in fdist.most_common(len(fdist)):
        tuple = (word,frequency)
        word_freq.append(tuple)
    return word_freq

def unigram(corpus):
    corpus = unpack(corpus)
    fdist = nltk.FreqDist(corpus)

    word_freq = calculateFrequency(fdist)
    n = len(fdist)
    new_word_freq = []

    for word, freq in word_freq:
        freq = freq/n
        freq = log(freq,2.71)
        tuple = (word,freq)
        new_word_freq.append(tuple)

    return new_word_freq

def sentenceProbability(sentence,unigrams):
    tokens = nltk.word_tokenize(sentence, language='portuguese')
    prob = 0
    for token in tokens:
        for uni in unigrams:
            if token == uni[0]:
                p = uni[1]
                prob += p
    prob = exp(prob)
    return prob


def userSentence(unigrams):
    sentence = input("Type a sentence: ")
    prob = sentenceProbability(sentence,unigrams)
    return prob
#-------------------Path Definer ------------------
sentences = fetchCorpus()
low_sentences = toLower(sentences)
corpus_tokens = tokenizeSentences(low_sentences)
unigrams = unigram(corpus_tokens)
print(unigrams)
prob = userSentence(unigrams)
print(prob)