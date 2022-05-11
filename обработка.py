import re
import os
import nltk
from nltk.corpus import stopwords #стоп слова
from nltk.stem.snowball import SnowballStemmer
nltk.download('words') #для проверки правописания
from nltk.corpus import words

spell = set(words.words())
sn_stemmer = SnowballStemmer("english")

stop_words = set(stopwords.words('english'))
stop_words.add("br")  # перенос стр

appendFile = open('filterTrain.txt', 'w')

f = 0
for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\train\neg"):
    fil = open(file.path, encoding='utf-8')
    words = fil.read().lower().split()  # массив слов в нижнем регистре

    f += 1
    print(f)

    for r in words:

        if r not in stop_words:  # сначала убираем стоп-слова, тк в некоторых есть '

            r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
            if r != '' and r not in stop_words and r in spell:  # для удаленных чисел ставших пустым местом или слипшихся
                appendFile.write(" " + sn_stemmer.stem(r))  # оставляем основу слова

    appendFile.write("!!!")  # разделитель отзывов
    fil.close()

for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\train\pos"):
    fil = open(file.path, encoding='utf-8')
    words = fil.read().lower().split()  # массив слов в нижнем регистре

    f += 1
    print(f)

    for r in words:

        if r not in stop_words:  # сначала убираем стоп-слова, тк в некоторых есть '

            r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
            if r != '' and r not in stop_words and r in spell:  # для удаленных чисел ставших пустым местом или слипшихся
                appendFile.write(" " + sn_stemmer.stem(r))  # оставляем основу слова

    appendFile.write("!!!")  # разделитель отзывов
    fil.close()


appendFile2 = open('filterTest.txt', 'w')

for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\test\neg"):
    fil = open(file.path, encoding='utf-8')
    words = fil.read().lower().split()  # массив слов в нижнем регистре

    f += 1
    print(f)

    for r in words:

        if r not in stop_words:  # сначала убираем стоп-слова, тк в некоторых есть '

            r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
            if r != '' and r not in stop_words and r in spell:  # для удаленных чисел ставших пустым местом или слипшихся
                if f >= 25000 and f < 30000:  # еще 5к отзывов из теста в трэйн добавляем
                    appendFile.write(" " + sn_stemmer.stem(r))  # оставляем основу слова
                else:
                    appendFile2.write(" " + sn_stemmer.stem(r))  # оставляем основу слова
    if f >= 25000 and f < 30000:
        appendFile.write("!!!")  # разделитель отзывов
    else:
        appendFile2.write("!!!")  # разделитель отзывов
    fil.close()

for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\test\pos"):
    fil = open(file.path, encoding='utf-8')
    words = fil.read().lower().split()  # массив слов в нижнем регистре

    f += 1
    print(f)

    for r in words:

        if r not in stop_words:  # сначала убираем стоп-слова, тк в некоторых есть '

            r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
            if r != '' and r not in stop_words and r in spell:  # для удаленных чисел ставших пустым местом или слипшихся
                if f > 45000 and f <= 50000:  # еще 5к отзывов из теста в трэйн добавляем
                    appendFile.write(" " + sn_stemmer.stem(r))  # оставляем основу слова
                else:
                    appendFile2.write(" " + sn_stemmer.stem(r))  # оставляем основу слова
    if f > 45000 and f < 50000:
        appendFile.write("!!!")  # разделитель отзывов
    elif f!=50000:
        appendFile2.write("!!!")  # разделитель отзывов

    fil.close()

appendFile.close()
appendFile2.close()
