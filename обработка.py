#обработка
import re
import os
import nltk
from nltk.corpus import stopwords  # стоп слова
from nltk.stem.snowball import SnowballStemmer

nltk.download('words')  # для проверки правописания
from nltk.corpus import words

spell = set(words.words())
sn_stemmer = SnowballStemmer("english")

stop_words = set(stopwords.words('english'))
stop_words.add("br")  # переноc str
fileA = open('filterAll.txt', 'w')

f = 0

def handling(path, f, k):
    for file in os.scandir(path):
        fil = open(file.path, encoding='utf-8')
        words = fil.read().lower().split()  # массив слов в нижнем регистре
        f += 1
        print(f)

        for r in words:
            if r not in stop_words:  # сначала убираем стоп-слова, тк в некоторых есть '
                r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова

            if r != '' and r not in stop_words and r in spell:  # для удаленных чисел ставших пустым местом или слипшихся
                fileA.write(" " + sn_stemmer.stem(r))  # оставляем основу слова

        fileA.write(k)
        if f != 50000:
            fileA.write("!!!")  # разделитель отзывов
        fil.close()
    return f

f = handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\train\neg", f, '0')
f = handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\test\neg", f, '0')

f = handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\train\pos", f, '1')
handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\test\pos", f, '1')
fileA.close()
