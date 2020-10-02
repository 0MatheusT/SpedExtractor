
# -*- coding: utf8 -*
''' 
A Simple Extractor Key Note for SPED Fiscal 
created by Matheus Tavares
'''

# Abrindo arquivo Sped para ler e Criando arquivo com notas separadas
sped = open("sped.txt", "r")

noteLine =[]

# Encontrando linhas C100 e salvando em Lista
for line in sped:
    if line[0:6] == '|C100|':
        noteLine.append(line)

# Separa os dados da nota pelos pipes e salva em array
sepNote = []

for line in noteLine:
        sepNote.append(line.split('|'))

# Salvando as chaves das notas em arquivo
keyNotes = open("./keys.txt", "w")
for i in sepNote:
    if (len(i[9]) > 0):
        keyNotes.write(i[9] + '\n')

sped.close()
keyNotes.close()