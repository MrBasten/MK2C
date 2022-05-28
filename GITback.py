import csv
import pandas as pd
import random
from math import sqrt

# переделка спикска в датафрейм
with open('Достопримечательности.csv', encoding='utf-8') as File:
    data = csv.reader(File)
    data = pd.DataFrame(data)

# убрать косяк с переименовыванием столбцов
data.columns = data.iloc[0]
data = data.drop(data.index[0])

data = data.drop(['Город', 'Аэропорт'], axis=1)

data['Удаленность'] = pd.to_numeric(data['Удаленность'])
data['Время_на_посещение'] = pd.to_numeric(data['Время_на_посещение'])
data['Время_С'] = pd.to_numeric(data['Время_С'])
data['Время_ДО'] = pd.to_numeric(data['Время_ДО'])

# вычисление общего времени (пробки?)
data['Общее_время'] = [2*x for x in data['Удаленность']]
data['Общее_время'] = round(
    data['Общее_время'] + data['Время_на_посещение'] + 1).astype(int)

'''
a = 8
b = 10

data_time = data
for i in range(data_time.count()[0]):

    a_plus_road = a + data_time.loc[i]['Удаленность']
    b_minus_road = b - data_time.loc[i]['Удаленность']

    if a_plus_road > 24:
        a_plus_road -= 24
    if b_minus_road < 0:
        b_minus_road += 24

    dia_left = max(a_plus_road, data_time.loc[i]['Время_С'])
    dia_right = min(b_minus_road, data_time.loc[i]['Время_ДО'])
    dia = dia_right - dia_left

    if dia < data_time.loc[i]['Время_на_посещение']:
        data_time = data_time.drop(labels=[i], axis=0)

data = data_time.reset_index(drop=True)
'''


def l_dost(data):
    d = list(data['Достопремечательность'])
    return d


def synth_critics():

    import random

    critics = {}
    dost = l_dost(data)

    for per in range(1, 11):
        a = {}
        for d in dost:
            x = random.choice([' ', 1, 2, 3, 4, 5])
            if x == ' ':
                continue
            a[d] = x
        critics[per] = a
    return critics


def ask_client():

    import random

    client = {}
    ask = random.sample(l_dost(data), 3)

    for a in ask:
        # print(f'Оцените по 5-бальной шкале желание посетить {a}')
        # client[a] = int(input())
        client[a] = random.choice([1, 2, 3, 4, 5])

    return client


critics = synth_critics()
client = ask_client()


# Возвращает коэффициент корреляции Пирсона между client и произвольным p
def Pirson(critics, client, p):

    from math import sqrt

    # Получить список предметов, оцененных обоими
    si = {}
    for item in client:
        if item in critics[p]:
            si[item] = 1
    # Если нет ни одной общей оценки, вернуть 0
    if len(si) == 0:
        return 0
    # Найти число элементов
    n = len(si)
    # Вычислить сумму всех предпочтений
    sum1 = sum([client[it] for it in si])
    sum2 = sum([critics[p][it] for it in si])
    # Вычислить сумму квадратов
    sum1Sq = sum([pow(client[it], 2) for it in si])
    sum2Sq = sum([pow(critics[p][it], 2) for it in si])
    # Вычислить сумму произведений
    pSum = sum([client[it] * critics[p][it] for it in si])
    # Вычислить коэффициент Пирсона
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den

    return r


def topMatches(critics, client, n):

    scores = [(Pirson(critics, client, other), other)
              for other in critics]  # if other != person

    scores.sort()
    scores.reverse()

    return scores[0:n]


# Получить рекомендации для заданного человека, пользуясь взвешенным средним оценок, данных всеми остальными пользователями

def getRecommendations(critics, client, Pirson):

    totals = {}
    simSums = {}

    for other in critics:
        #  сравнивать меня с собой же не нужно
        # if other == client:
        # continue
        sim = Pirson(critics, client, other)
        # игнорировать нулевые и отрицательные оценки
        if sim <= 0:
            continue

        for item in critics[other]:
            # оценивать только фильмы, которые я еще не смотрел
            if item not in client or client[item] == 0:
                # Коэффициент подобия * Оценка
                totals.setdefault(item, 0)
                totals[item] += critics[other][item] * sim
                # Сумма коэффициентов подобия
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Создать нормализованный список
    rankings = [(total / simSums[item], item)
                for (item, total) in totals.items()]
    # Вернуть отсортированный список
    rankings.sort()
    rankings.reverse()

    return rankings[0:6]


# ВЫЗОВ
r = getRecommendations(critics, client, Pirson)


#######################################################


res = []
for i in r:
    res.append(i[1])


def for_col(i):
    loc_data = data[data['Достопремечательность'] == i]

    dictt = {'Достопремечательность': list(loc_data['Достопремечательность'])[0],
             'Описание': 'бла-бла-бла',
             'Стоимость': list(loc_data['Стоимость'])[0],
             'Общее_время': list(loc_data['Общее_время'])[0],
             'Краткое описание': list(loc_data['Краткое описание'])[0],
             'Описание': list(loc_data['Описание'])[0]}

    return dictt
