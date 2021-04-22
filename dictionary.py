import json

dados = json.load(open('data.json'))

answer = input('What word do you wanna search? ')

while answer != '':
    try:
        for result in dados[answer]:
            print(result)
    except:
        print('The search not return results')
    answer = input('What word do you wanna search? ')

