#Mineração de Texto 2018.2
#Raissa Camelo Salhab
#Lista 02, Questão 01
#--------------------------------------Word Clouds with NLTK-----------------------------------------------------

#-------------Imports-----------
import nltk
from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
from nltk.tree import Tree
import nltk.parse.api
from pycorenlp import StanfordCoreNLP
#---------------------------------------Itens 1 & 2 & 3--------------------------------------------------------------
#------------Function Definitions---------
    #----------File Opener----------------
def openFile(path):
    f = open(path, 'r+')
    my_file_data = f.read()
    f.close()
    return my_file_data
    #---------StopWords Definition--------
def extractStopWords(data,stopWords):
    stopWords = nltk.word_tokenize(stopWords)
    filteredWords = []
    for word in data:
        if word not in stopWords:
            filteredWords.append(word)
    return filteredWords

#-------Open / Read File--------  #Switch file names for different quest itens
path = 'C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/AULA_03/LE_02/NLP.txt'
path2 = 'C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/AULA_03/LE_02/Corpus_en_NER.txt'
pathStopWords = 'C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/AULA_03/LE_02/stopwords.txt'

#--------Call the file-----------  #Choose the item path and comment others
my_file_data = openFile(path2)     #Switch between path and path2 for different itens
stopWords = openFile(pathStopWords)#Only use for StopWords in item 3

#----Tokenize to fetch words--------------
tokens = nltk.word_tokenize(my_file_data)
#----------------------------------------

#------Filter StopWords----------- #Only use this stage for item 3, comment otherwise
tokens = extractStopWords(tokens,stopWords)
#--------------Data----------------------

noun_tags = ['NN','NNP','NNS','NNPS']
verb_tags = ["VB","VBD","VBG","VBN","VBP","VBZ"]
#----------------------------------------

#----POS TAG words to get noums--------------
nouns = []
unic_nouns = []
nouns_frequency = []
pos_tagged = nltk.pos_tag(tokens)

#-----------Isolate Nouns or Verbs------------
for word,tag in pos_tagged:
    if tag in verb_tags:     #Switch between noun_tags and verb_tags for both questions
        nouns.append(word)
#------------------------------------

#----Fetch 20 most frquent noums-----
freq = nltk.FreqDist(w.lower() for w in nouns)
for i in freq.most_common(20):
    unic_nouns.append(i[0])
    nouns_frequency.append(i[1])

#-----Lemmanizing Words------------
lemmas = []
wordnet_lemmatizer = WordNetLemmatizer()
for word in unic_nouns:
    lemma = wordnet_lemmatizer.lemmatize(word,)
    lemmas.append(lemma)
#-----------------------------------
#--------Word Cloud----------------- #Print to generate Word Clouds
""""
for i in range(len(lemmas)):
    print(str(nouns_frequency[i])+ " " + lemmas[i])
"""
#-------------------------------------Item 4-----------------------------------------------------------
sentence = "The last love letter I wrote was probably about 10 years ago."
#tokenized = nltk.word_tokenize(sentence)

parse = StanfordCoreNLP('http://localhost:9000')

output = parse.annotate(sentence, properties={
  'annotators': 'parse',
  'outputFormat': 'json'
})

tree1 = output['sentences'][0]['parse'] + ""
treeFinal = Tree.fromstring(tree1)
treeFinal.draw()
#t = Tree.
#t.draw()

