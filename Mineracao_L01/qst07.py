#Mineração de Textos 2018.2
#Raissa Camelo
#Sentence Spliter

f = open('C:/Users/Familia Camelo/Documents/Raissa Camelo/Mineracao_rinaldo/Aula_02/texto_pt.txt', 'r+')
my_file_data = f.read()
f.close()
#Delimiters
eos = ["?","!"]
eos2 = [")","]","}"]
eos3 = ["$","(","[","{"]

flag_period = 0
flag_capitalized = 0
flag_spaceAfterPeriod = 0
flag_whiteSpace = 0
#Data
sentence = ""
token = ""
token_size = 0
output = []

def eos_make(token, token_size,sentence,flag_period, flag_capitalized):
    flag_period = 0
    flag_capitalized = 0
    token += char
    token += " "
    sentence+= token
    output.append(sentence)
    token = ""
    token_size = 0
    sentence = ""
def not_eos(token,token_size):
    token += char
    token_size += 1
for char in my_file_data:
    if char in eos:
        eos_make(token,token_size,sentence,flag_period,flag_capitalized)
    if char != " ":
        not_eos(token,token_size)
    else:
        flag_whiteSpace = 1
        token += " "
        sentence+=(token)
        token = ""
        token_size = 0
    if char in eos2 and flag_period ==0:
        eos_make(token, token_size, sentence,flag_period,flag_capitalized)
    if char == ".":
        flag_period = 1
    if flag_period == 1:
        flag_capitalized = token.isupper()
        if flag_capitalized ==1 and token_size< 5 and char.isupper():
            not_eos(token, token_size)
        if char == ".":
            not_eos(token, token_size)
        if flag_spaceAfterPeriod == 1 and char.isupper():
            eos_make(token, token_size, sentence, flag_period, flag_capitalized)
        if char == " ":
            flag_spaceAfterPeriod = 1
        if token_size< 3:
            not_eos(token, token_size)
    if flag_whiteSpace == 1 and char in eos3:
        eos_make(token, token_size, sentence, flag_period, flag_capitalized)
print(output)


