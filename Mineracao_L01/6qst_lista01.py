#Mineração de Textos 2018.2
#Raissa Camelo
#Tokenizer

f = open('C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/Aula_02/texto_pt.txt', 'r+')
my_file_data = f.read()
f.close()

#Define Delimiters
delimiters = [",",".",";",";","!","?","(",")","<",">","\"","'","\n","\t"," "]
whiteSpace = ["\n","\t"," "]
#OutPut
output = []
word = ""

for char in my_file_data:
    if char not in delimiters:    #element of word
        ch = char
        word = word + char
    else:
        if char not in whiteSpace: #delimiter to be a token and to close previous token and insert in the list
            output.append(word)
            word = ""  #Clear stream
            output.append(char)
        else:                       #white space to be ignored, close previous token and insert in the list
            output.append(word)
            word = ""  #Clear stream
print(output)
   #print (char)
#print (my_file_data)
