from nltk.stem import WordNetLemmatizer
from stanfordcorenlp import StanfordCoreNLP
import nltk
#-------------Function Definitions------
def openFile(path):
    f = open(path, 'r+')
    my_file_data = f.read()
    f.close()
    return my_file_data
#-------------Save sentences in Tuple (index,sentence) Begin with 1
#---------------Ner / Unic Ner----------------------------------------
#-----------------Calculate globalScore-----------------------------
def globalScore(ner_number, total_sentences,sentence_index,):
    score_pos = 1 - (sentence_index/total_sentences)
    numerator =  (2* ner_number)
    denominator = total_sentences + score_pos
    global_score = 1+ (numerator/denominator)
    return global_score
#------------Fetch Key to order Tuple------------------------------
def getKey(trio):
    return trio[1]

#------------------CoreNLP Call------------------------------------------
nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-02-27')
path = "C:/Users/SrtaCamelo/PycharmProjects/Mineracao_L02/News/news"

#------------------Iterate Over Files-------------------------------
for i in range(1):
    sentence_list = []
    #trio = ("Index","GlobalScore","Sentence")
    #sentence_list.append(trio)
    #----------------Read File---------------
    file_path = path + str(i+1)+".txt"
    file = openFile(file_path)
    sentences = nltk.sent_tokenize(file)
    #print(sentences)
    #-------------Count sentences----- sentence_number
    sentence_number = len(sentences)

    #---------------Index Sentences and Sentence NER----------  ner_number
    sentence_count = 0
    for sentence in sentences:
        #print(sentence_count,sentence)
        sentence_count += 1

        ner = nlp.ner(sentence)
        ner_number = 0
        for entity in ner:
            if entity[1] !='O':
                ner_number +=1
        #Sentence Index - sentence_count
        #Sentence NER - ner_number
        #Total Number of Sentences - sentence_number
        globScore = globalScore(ner_number,sentence_number,sentence_count)
        trio = (sentence_count, globScore,sentence)
        sentence_list.append(trio)
    sorted_sentence_list = sorted(sentence_list,key = getKey, reverse= 1)
    #------------- fetch 30% most frequent--------------------------------
    percentage = int((sentence_number * 30)/100)
    print(percentage)
    #----------------Show Result------------------------------------------
    for j in range(percentage):
        print(sorted_sentence_list[j])

    #------------------ Sentence NER----------  ner_number

#------------------------Close Java environment-------------
nlp.close()
