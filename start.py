# <------------>
# v0.2
# Author: Smilentus
# <------------>
# Переменные
engAl = 'abcdefghijklmnopqrstuvwxyz'
rusAl = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
digitAl = '0123456789'
symbAl = '!@#$%^&*_+"№;:?-=~`\{\}[]()"\'\\|<>,.?/'

# Место для функций
def locateCulture(char):
    ''' Определение принадлежности символа к алфавиту '''
    for x in engAl:
        if char == x:
            return '[ENG]'
    for x in rusAl:
        if char == x:
            return '[RUS]'
    for x in digitAl:
        if char == x:
            return '[DGT]'
    for x in symbAl:
        if char == x:
            return '[SMB]'
    return '[ERR]' 

def toLanguage():
    ''' Проверяет строку посимвольно на принадлежность к языку '''
    lngText = ''
    for c in resultTxt:
        lngText += f'{c} is {locateCulture(c)} / '
    return lngText

def toDigit():
    ''' Подсчитывает позицию буквы в алфавите, находит сумму позиций и сумму цифр '''
    digitText = ''
    sum = 0
    for x in resultTxt:
        if locateCulture(x) == '[RUS]':
            for c in range(0, len(rusAl)):
                if x == rusAl[c]:
                    digitText += f'{x}:{c + 1} / '
                    sum += c + 1
        elif locateCulture(x) == '[ENG]':
            for c in range(0, len(engAl)):
                if x == engAl[c]:
                    digitText += f'{x}:{c + 1} / '
                    sum += c + 1
    digitText += f'(Сумма чисел: {sum} / Сумма цифр в числе: {toCyph(sum)})'
    if sum == 0:
        return 'None'
    else:
        return digitText

def toCyph(num):
    ''' Рекурсивно считает сумму цифр в числе '''
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    if result < 10:
        return result
    return toCyph(result)

def adaptOrigin():
    ''' Выполняет преобразования оригинального текста для дальнейшего упрощения работы с ним '''
    global resultTxt
    resultTxt = resultTxt.replace(' ', '')
    resultTxt = resultTxt.lower()

def outputInformation():
    ''' Проверяет и выводит итоговый результат работы программы '''
    if resultTxt == '':
        print('Оригинальная строка содержала только пробелы! :c')
    else:
        print(f'[0] Оригинальная строка: {origin}')
        print(f'')
        print(f'[1] Алфавитное представление: {toLanguage()}')
        print(f'')
        print(f'[2] Транслит: {transText}')
        print(f'')
        print(f'[3] Позиции букв в алфавите: {toDigit()}')
        print(f'')
        print(f'[4] Бинарное представление: {binaryText}')
    print(f'')
    input('Нажмите Enter для завершения ...')

# Ввод информации
origin = input('Введите текст >')
resultTxt = origin

# Дополнительные преобразования оригинальной строки
adaptOrigin()
transText = 'None'
binaryText = 'None'

# Итоговый вывод
outputInformation()