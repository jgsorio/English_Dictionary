import json
from difflib import get_close_matches

dados = json.load(open('data.json'))

answer = input('What word do you wanna search? ')

'''
Método que retorna com 80% de assertividade as palavras similares
dentro do dicionario, caso o cliente digite algo errado
@author José Guilherme
'''


def filter_word(word):
    return get_close_matches(word, dados.keys(), cutoff=0.8)


def word_test(word):
    words = filter_word(word)
    if len(words) > 0:
        for word in words:
            if word.upper() in dados:
                return dados[word.upper()]
            elif word.title() in dados:
                return dados[word.title()]
            elif word.lower() in dados:
                return dados[word.lower()]
            elif word.capitalize() in dados:
                return dados[word.capitalize()]
    else:
        return False


while answer != '':
    if type(word_test(answer)) != bool:
        for (indice, result) in enumerate(word_test(answer)):
            print(f'{indice} - {result}')
    else:
        print('The search return no results!')
    answer = input('What word do you wanna search? ')
