__author__ = 'agorgoma'


def isPasswordStrong(text):
    import re
    ch8Regex = re.compile(r'(.{8})+')  # проверяем, что в пароле минимум 8 символов
    upRegex = re.compile(r'([A-Z])+')  # проверка наличия хотябы одного символа в верхнем регистре
    lowRegex = re.compile(r'([a-z])+')  # проверка наличия хотябы одного символа в верхнем регистре
    digRegex = re.compile(r'([0-9])+')  # проверка наличия хотябы одного числового символа

    if ch8Regex.search(text) and upRegex.search(text) and lowRegex.search(text) and digRegex.search(text) is not None:
        print('Password strong')
    else:
        if ch8Regex.search(text) is None:
            print('Need min 8 characters')
        elif upRegex.search(text) is None:
            print('None upper char')
        elif lowRegex.search(text) is None:
            print('None lower char')
        elif digRegex.search(text) is None:
            print('None digit char')


isPasswordStrong('paS1sword')