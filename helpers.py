import random
import string


def register_new_string():
    # метод генерирует строку, состоящую только из букв нижнего регистра
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(8))
    return random_string


    # генерация уникальной строки
def generation_string():
    random_number = random.randint(100, 999)
    random_string = f'{random_number}'

    return random_string
