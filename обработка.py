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
stop_words.add("br")  # перенос стр

appendFile1 = open('filterPos.txt', 'w')
appendFile2 = open('filterNeg.txt', 'w')

f = 0
def handling(path, fileW, f):
    for file in os.scandir(path):
        fil = open(file.path, encoding='utf-8')
        words = fil.read().lower().split()  # массив слов в нижнем регистре
        f += 1
        print(f)
        for r in words:
            if r not in stop_words:  # сначала убираем стоп-слова, тк в некоторых есть '
                r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова

            if r != '' and r not in stop_words and r in spell:  # для удаленных чисел ставших пустым местом или слипшихся
                fileW.write(" " + sn_stemmer.stem(r))  # оставляем основу слова
        if f % 25000!=0:
            fileW.write("!!!")  # разделитель отзывов
        fil.close()
    return f

f = handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\train\neg", appendFile2, f)
f = handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\test\neg", appendFile2, f)
appendFile2.close()

f = handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\train\pos", appendFile1, f)
handling(r"C:\Users\sever\OneDrive\Рабочий стол\имдб\aclImdb_v1\aclImdb\test\pos", appendFile1, f)
appendFile1.close()
