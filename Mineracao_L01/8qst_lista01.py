import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
#from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt


f = open('C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/Aula_02/texto_en.txt', 'r+')
my_file_data = f.read()
f.close()

#Tokenization
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(my_file_data)

len_tokens =len(tokens)
print (len_tokens)

#Sentence Spliting
sentences = sent_tokenize(my_file_data)
len_sentences =len(sentences)
print (len_sentences)

media = len_tokens/len_sentences
print(media)

#Lemmatizer
lemmas = []
wordnet_lemmatizer = WordNetLemmatizer()
for word in tokens:
    lemma = wordnet_lemmatizer.lemmatize(word)
    lemmas.append(lemma)
print(lemmas)



#Stemmer
radicals = []
unic_radix = []
#porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer("english")
for word in tokens:
    stem = snowball_stemmer.stem(word)
    #stem = porter_stemmer.stem(word)
    radicals.append(stem)
#print (radicals)
for radix in radicals:
    if radix not in unic_radix:
        unic_radix.append(radix)
#print(unic_radix)
print(len(radicals), len(unic_radix))

#POS TAGGING
tags = []
frequency = []
unic_tags = []
pos_tagged = nltk.pos_tag(tokens)
#print(pos_tagged)
#total_tags = len(pos_tagged)
#print(total_tags)
#for word,tag in pos_tagged:  #Split tags from words
    #tags.append(tag)
#Contar frequencia de cada TAG
#tags.sort()
#print(tags)

tag_freq = nltk.FreqDist(tag for (word, tag) in pos_tagged)
"""
for i in tag_freq.most_common():
    tags.append(i[0])
    frequency.append(i[1])
#print(len(tags))
#print((frequency))

#tags has all tags sorted
#freq has all frequencies for each tag (in order)

#-----------Plot Grafic--------------#

plt.figure(0)
plt.bar(tags, frequency)
plt.xlabel("TAGS")
plt.ylabel("Frequency")
plt.title("Tag Frequency")
plt.grid(True)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5, forward=True)
plt.savefig('8qst_e.png')

#----------Plot other grafic------- Radical Frequency
rads = []
freq = []
radicals.sort()
rad_freq = nltk.FreqDist(rad for (rad) in radicals)
for i in rad_freq.most_common():
    rads.append(i[0])
    freq.append(i[1])
print(len(rads))
print(len(freq))

plt.figure(1)
plt.bar(rads[0:15], freq[0:15])
plt.xlabel("Steamming")
plt.ylabel("Frequency")
#plt.yticks(sorted(set(list(stem_cont.values()))))
plt.title("Radical Frequency")
plt.grid(True)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5, forward=True)
plt.savefig('8qst_f.png')
"""