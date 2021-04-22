import json

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
        return ['The search returned no results']


while answer != '':
    for result in word_test(answer):
        print(result)
    answer = input('What word do you wanna search? ')
