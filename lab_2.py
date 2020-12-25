import csv


def text_equalizer(message):
    while True:
        if message == '' or message.isalpha():
            break
    return message.lower()


def num_equalizer(message):
    while True:
        if message == '' or message.isdigit():
            break
    return message.lower()


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


def check_developer(user_developer, game_developer):
    return (user_developer == [''] or
            any(u_developer in game_developer for u_developer in user_developer))


message = input("Укажите максимальный год выпуска: ")
year = num_equalizer(message)

message = input('Укажите интересующего Вас разработчика: ')
developer = text_equalizer(message).split(',')

message = input('Укажите платформу игры: ')
platform = text_equalizer(message).split(',')

message = input('Укажите минимальное ограничение по возрасту: ')
age = num_equalizer(message)

message = input('Укажите категорию игры: ')
categories = text_equalizer(message).split(',')

message = input('Укажите жанр игры: ')
genres = text_equalizer(message).split(',')

message = input('Укажите максимальную цену игры в доллорах: ')
price = num_equalizer(message)

with open('steam.csv', encoding='utf-8') as f, \
        open('answer.txt', 'w', encoding='utf-8') as ans:
    reader = csv.reader(f)
    collumns = next(reader)
    for row in reader:
        game_name = row[1]
        game_year = int(row[2].lower().split('-')[0])
        game_developer = row[4].lower().split(';')
        game_platform = row[6].lower().split(';')
        game_age = int(row[7])
        game_category = row[8].lower().split(';')
        game_genres = row[9].lower().split(';')
        game_price = float(row[17])

        if (check_year(year, game_year)
                and check_genre(genres, game_genres)
                and check_age(age, game_age)
                and check_category(categories, game_category)
                and check_platform(platform, game_platform)
                and check_price(price, game_price)
                and check_developer(developer, game_developer)):
            ans.write(game_name + '\n')
