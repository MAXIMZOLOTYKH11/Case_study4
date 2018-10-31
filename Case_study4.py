"""Case-study #4 Анализ текста
Разработчики:
Иванов А.С., Петров П.С., Сидоров C.H.

"""

text = input("Введите текст:")

count_sentens = text.count('.')
print('Предложений:', count_sentens)

count_words = text.count(' ')
print('Слов:', count_words + 1)

count_syllables = 0
for i in text:
    letter = i.lower()
    if letter == "а" or letter == "о" or \
       letter == "е" or letter == "и" or \
       letter == "у" or letter == "ы" or \
       letter == "ё":
        count_syllables += 1
print('Слогов:', count_syllables)

ASL = (count_words + 1) / count_sentens
print('Средняя длина предложения в словах:', ASL)
ASW = count_syllables / (count_words + 1)
print('Средняя длина слова в слогах:', ASW)
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
print('Индекс удобочитаемости Флеша:', FRE)

if FRE <= 25:
    print('Текст трудно читается (для выпускников ВУЗов).')
elif 25 < FRE <= 50:
    print('Текст немного трудно читать (для студентов).')
elif 50 < FRE <= 80:
    print('Простой текст (для школьников).')
elif 80 < FRE:
    print('Текст очень легко читается (для младших школьников).')
