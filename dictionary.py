import json

dados = json.load(open('data.json'))

answer = input('What word do you wanna search? ')

while answer != '':
    try:
        for result in dados[answer.lower()]:
            print(result)
    except:
        print('The search returned no results')
    answer = input('What word do you wanna search? ')

