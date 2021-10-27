import requests
from datetime import datetime


# п.1 декоратор-логгер
def get_info_function(function):
    def new_function(*args, **kwargs):
        result = function(*args, **kwargs)
        log = f'Время: {datetime.now()}, имя функции:{function.__name__}, аргументы: {args} {kwargs}, ' \
              f'результат: {result} \n'
        with open('logs.txt', 'a', encoding='UTF-8') as file:
            file.writelines(log)
        return result
    return new_function


# п.2 декоратор-логгер с параметром – путь к логам
def get_log_function_path(path):
    def get_info_function(function):
        def new_function(*args, **kwargs):
            result = function(*args, **kwargs)
            log = f'Время: {datetime.now()}, имя функции:{function.__name__}, аргументы: {args} {kwargs}, ' \
                  f'результат: {result} \n'
            with open(path, 'a', encoding='UTF-8') as file:
                file.writelines(log)
            return result
        return new_function
    return get_info_function


# п.3 Применить написанный логгер к приложению из любого предыдущего д/з.
@get_log_function_path('log_2.txt')
def smartest_hero(list_hero):
    hero_intelligence = {}
    url = 'https://superheroapi.com/api/2619421814940190/'
    for hero in list_hero:
        response = requests.get(url + '/search/' + hero)
        for element in response.json()['results']:
            hero_intelligence[element['name']] = element['powerstats']['intelligence']
    smartest = sorted(hero_intelligence)
    return f'Самый умный супергерой - {smartest[-1]}'


result = smartest_hero(['Captain America', 'Thanos', 'Hulk'])
print(result)