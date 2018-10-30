#Mineração de Textos 2018.2
#Raissa Camelo
#Sentence Spliter

f = open('C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/Aula_02/texto_pt.txt', 'r+')
my_file_data = f.read()
f.close()

#Define Structures
output = []
token = ""
token_size = 0
sentence = " "
#Define EOS
eos = ['!','?']

ors = ["ou","or"]
eos2 = ["(","[","{"]

#Flags
or_detected = 0
period_detected = 0
is_capitalized = 0

#EOS
def eos_make(token, token_size,sentence):
    output.append(sentence)
    token = ""
    token_size = 0
    sentence = ""

for char in my_file_data:
    if char not in eos:
        if token in ors and char == " ":
            eos_make(token, token_size, sentence)
            output.append(token)
        if char != " ":
            token = token + char
            token_size += 1
            #print(token)
        else:
            token = token + char
            sentence += token
            token = ""
            token_size = 0
    elif char == ".":
        period_detected = 1
        token = token + char
        if token_size < 2:
            token_size += 1
    else:
        token = token + char
        eos_make(token, token_size,sentence)
        #print(char)
print(output)