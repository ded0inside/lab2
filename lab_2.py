import csv


def get_text_value(message):
    while True:
        value = input(message)
        if value == '' or value.isalpha():
            break
    return value.lower()


def get_num_value(message):
    while True:
        value = input(message)
        if value == '' or value.isdigit():
            break
    return value.lower()


def check_year(user_year, game_year):
    return user_year == '' or game_year <= int(user_year)


def check_age(user_age, game_age):
    return user_age == '' or game_age <= int(user_age)


def check_genre(user_genres, game_genres):
    return (user_genres == [''] or
            any(u_genre in game_genres for u_genre in user_genres))


def check_category(user_category, game_category):
    return (user_category == [''] or
            any(u_category in game_category for u_category in user_category))


def check_platform(user_platform, game_platform):
    return (user_platform == [''] or
            any(u_platform in game_platform for u_platform in user_platform))


def check_price(user_price, game_price):
    return user_price == '' or game_price <= float(user_price)


def check_rating(user_rating, game_rating):
    return user_rating == '' or game_rating >= float(user_rating)


print('Вас приветсвтвует мастер поиска игр!')
print('Пройдите краткий опрос, чтобы мы смогли посоветовать вам игры.')
print('Вводите ответы через запятую. Чтобы пропустить - нажмите Enter.')

message = 'Какой максимальный год выпуска игры вас интересует? '
years = get_num_value(message)

message = 'Какой жанр игр вас интересует (Action, RPG)? '
genres = get_text_value(message).split(',')

message = 'Укажите минимальное ограничение по возрасту: '
age = get_num_value(message)

message = 'Укажите категорию игры (Multiplayer, Online): '
categories = get_text_value(message).split(',')

message = 'На какую платформу планируется установка (windows, mac, linux)? '
platforms = get_text_value(message).split(',')

message = 'Укажите максимальную цену игры ($): '
prices = get_num_value(message)

message = 'Укажите минимальный процент положительных отзывов: '
ratings = get_num_value(message)


with open('steam.csv', encoding='utf-8') as f, \
        open('out.txt', 'w', encoding='utf-8') as out:
    reader = csv.reader(f)
    collumns = next(reader)
    for row in reader:
        game_name = row[1]
        game_year = int(row[2].lower().split('-')[0])
        game_platform = row[6].lower().split(';')
        game_age = int(row[7])
        game_category = row[8].lower().split(';')
        game_genres = row[9].lower().split(';')
        game_price = float(row[17])
        game_rating = float(int(row[12])/(int(row[12])+int(row[13])))*100

        if (check_year(years, game_year)
                and check_genre(genres, game_genres)
                and check_age(age, game_age)
                and check_category(categories, game_category)
                and check_platform(platforms, game_platform)
                and check_price(prices, game_price)
                and check_rating(ratings, game_rating)):
            out.write(game_name + '\n')
