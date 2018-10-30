#Mineração de Texto 2018.2
#Raissa Camelo Salhab
#Lista 02, Questão 02
#--------------------------------------------CoreNLP-----------------------------------------------------------------
#---------Imports--------------
import corenlp
import pycorenlp
from stanfordcorenlp import StanfordCoreNLP
import json

#-------------Function Definitions------
def openFile(path):
    f = open(path, 'r+')
    my_file_data = f.read()
    f.close()
    return my_file_data
#------------------CoreNLP Call------------------------------------------
nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-02-27')
path = "C:/Users/SrtaCamelo/Documents/2018.2/Mineracao_rinaldo/AULA_03/LE_02/Corpus_en_NER.txt"
#------------------------Call File-------------
file = openFile(path)
#------------------Tokenizing-------------------

tokenized = nlp.word_tokenize(file)
#------------------Sentence Spliting-------------------------
def sentence_splitter(file):
    props = {'annotators': 'tokenize,ssplit', 'pipelineLanguage': 'en', 'outputFormat': 'json'}
    ssplit = nlp.annotate(file, properties=props)
    ssplit = json.loads(ssplit)
    sentence_list = []
    sentence = ""
#------------Extract Sentence From Json-----------------------
    for splitList in ssplit["sentences"]:
        sentenceList = splitList["tokens"]
        for word in sentenceList:
            wword = word["word"]
            wword += " "
            sentence += wword

        sentence_list.append(sentence)
        sentence = ""
    return sentence_list
#print(sentence_list)

#----------------------POS Tag--------------------------------
pos = nlp.pos_tag(file)
#print ('Part of Speech:',pos )
#------------------------Lemma------------------------------
props = {'annotators': 'tokenize, ssplit, pos,lemma', 'pipelineLanguage': 'en', 'outputFormat': 'json'}
lemmas = nlp.annotate(file, properties=props)
lemmas = json.loads(lemmas)

original_words = []
lemma_list = []
#print(lemmas)
#------------Extract Tuple (original,lemma) From Json-----------------------
for lem in lemmas["sentences"]:
    for token in lem["tokens"]:
        word = token['word']
        lemma = token['lemma']
        original_words.append(word)
        lemma_list.append(lemma)
        #print(word, lemma)
#print(original_words)
#print(lemma_list)

#--------------------------Named Entities (NER)----------------
ner = nlp.ner(file)
#print ('Named Entities:', ner)
#print ('Constituency Parsing:', nlp.parse(file))
#---------------------------Dependency Parse-------------------
#dep_parsing = nlp.dependency_parse(file)
#print ('Dependency Parsing:', dep_parsing)

#----------------------------1 Qst -------------------------------
"""
iterator = 0
verb_list= []
for tag in pos:
    if 'VB' in tag[1]:
        if tag[0] not in verb_list:
            lemma = lemma_list[iterator]
            word = tag[0]
            verb_list.append(word)
            print(word,"-",lemma, ",")
    iterator +=1
"""
#----------------------- 2 Qst -----------------------------------
"""
#print(ner)
named_entities = []
for entity in ner:
    if entity[1] != 'O':
        named_entities.append(entity)
        print(entity[0], entity[1])

"""
#---------------------- 3 Qst -----------------------------------
# path = "NLP.txt"
file = openFile(path)
sentences = sentence_splitter(file)
#print(sentences)

dependencies = []
for i in range(3):
    sentence = sentences[i]
    #print(sentence)
    dep_parsing = nlp.dependency_parse(sentence)
    for dep in dep_parsing:
        #print(dep[0])
        if dep[0] not in dependencies:
            dependencies.append(dep[0])

for dep in dependencies:
    print(dep)

nlp.close()


