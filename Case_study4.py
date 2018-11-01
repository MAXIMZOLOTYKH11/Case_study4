"""Case-study #4 Анализ текста
Разработчики:
Зеленская, Золотых, Шерубнева

"""
import ru_local

text = input(ru_local.ENTER_TEXT)

count_sentens = text.count('.')
print(ru_local.SENTENCES, count_sentens)

count_words = text.count(' ')
print(ru_local.WORDS, count_words + 1)

count_syllables = 0
for i in text:
    letter = i.lower()
    if letter == "а" or letter == "о" or \
       letter == "е" or letter == "и" or \
       letter == "у" or letter == "ы" or \
       letter == "ё":
        count_syllables += 1
print(ru_local.SYLLABLES, count_syllables)

ASL = (count_words + 1) / count_sentens
print(ru_local.AVERAGE_SENTENCE_LENGTH_IN_WORDS, ASL)
ASW = count_syllables / (count_words + 1)
print(ru_local.AVERAGE_SENTENCE_LENGTH_IN_SYLLABLES, ASW)
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
print(ru_local.INDEX_READABILITY_FLASH, FRE)

if FRE <= 25:
    print(ru_local.TEXT_IS_DIFFICULT_TO_READ)
elif 25 < FRE <= 50:
    print(ru_local.TEXT_IS_A_BIT_DIFFICULT_TO_READ)
elif 50 < FRE <= 80:
    print(ru_local.SIMPLE_TEXT)
elif 80 < FRE:
    print(ru_local.TEXT_IS_EASY_TO_READ)
