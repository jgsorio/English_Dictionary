import json
from difflib import get_close_matches

dados = json.load(open('data.json'))

answer = input('What word do you wanna search? ')


def word_test(word):
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



'''
Método que retorna com 80% de assertividade as palavras similares
dentro do dicionario, caso o cliente digite algo errado
@author José Guilherme
'''


def filter_word(word):
    matches = get_close_matches(word, dados.keys(), cutoff=0.8)
    if len(matches) > 1:
        question = input(f'Did you mean {matches[0]}? Press y or n ')
        if question.lower() == 'y':
            return str(matches[0])
        else:
            answer = input('What word do you wanna search? ')
            return filter_word(answer)
    else:
        print('No results found!')
        answer = input('What word do you wanna search? ')
        return filter_word(answer)

while answer != '':
    word = filter_word(answer)
    if type(word) != bool:
        for (indice, result) in enumerate(word_test(word)):
            print(f'{indice} - {result}')
    else:
        print('No results found!')
    answer = input('What word do you wanna search? ')
