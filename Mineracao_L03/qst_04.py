#Mineração de Texto 2018.2
#Raissa Camelo Salhab
#Lista 03, Questão 04

#------------------------Imports--------------------
import nltk
from nltk.corpus import brown
import matplotlib.pyplot as plt
#------------------------Functions-----------------
#---------------------File Opener------------------
def openFile(path):
    f = open(path, 'r+')
    my_file_data = f.read()
    f.close()
    return my_file_data

def preprossess(corpus):
    words = [word.lower() for word in corpus if len(word) > 1]
    words = [word for word in words if not word.isnumeric()]
    return words

def calculateFrequency(fdist):
    word_freq = []
    for word, frequency in fdist.most_common(len(fdist)):
        tuple = (word,frequency)
        word_freq.append(tuple)
    return word_freq

def unigram(corpus):
    corpus = preprossess(corpus)
    fdist = nltk.FreqDist(corpus)

    word_freq = calculateFrequency(fdist)
    n = len(fdist)
    new_word_freq = []

    for word, freq in word_freq:
        freq = freq/n
        tuple = (word,freq)
        new_word_freq.append(tuple)

    word_freq = new_word_freq[0:50]
    return word_freq

def getClass(corpus):
    wordList = []
    for word, freq in corpus:
        wordList.append(word)
    pos = nltk.pos_tag(wordList)
    print(pos)
    return pos

def getPOSfrequency(pos_tagged):
    tag_freq = nltk.FreqDist(tag for (word, tag) in pos_tagged)
    tags = []
    frequency = []
    for i in tag_freq.most_common():
        tags.append(i[0])
        frequency.append(i[1])
    return tags,frequency

def plotHistogram(tags,freqs):
    plt.figure(0)
    plt.bar(tags, freqs)
    plt.xlabel("TAGS")
    plt.ylabel("Frequency")
    plt.title("Tag Frequency")
    plt.grid(True)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5, forward=True)
    plt.savefig('qst04_L03')


#----------------------Main Code-------------------
corpus = brown.words(categories='news')
print(type(corpus))
uni = unigram(corpus)
pos_tagged = getClass(uni)
tag, freq = getPOSfrequency(pos_tagged)
#plotHistogram(tag,freq)

"""
Preposições, conjunções e artigos são sempre as palavras mais frequentes em textos
"""