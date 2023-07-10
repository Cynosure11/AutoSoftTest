'''
introduce args and kwargs
как я понял на **kwargs можно добавить несколько аргументов
вкратце про *args,
плейлист в музыке есть песни
- плейлист
-- песня 1
-- песня 2
-- песня 3
Выводит все песни
'''


def my_function(*args):
    for arg in args:
        print(arg)


print('Hello', 'World', 2023, 'Testing', 'Evetything')


def my_function2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


my_function2(name="Alice", age=25, city="New York")
