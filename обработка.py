import nltk
import re
import os
import io
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from spellchecker import SpellChecker

spell = SpellChecker() # проверка правописания

sn_stemmer = SnowballStemmer("english")

stop_words = set(stopwords.words('english'))
stop_words.add("br") #перенос стр


appendFile = open('filterAll.txt', 'w')

f = 0
for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\Настя\aclImdb\train\neg"):
  fil = io.open(file.path, encoding = 'utf-8')
  words = fil.read().lower().split() # массив слов в нижнем регистре

  f += 1
  print(f)

  for r in words:

    if r not in stop_words:      #сначала убираем стоп-слова, тк в некоторых есть '

      r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
      if r != '' and r not in stop_words and r in spell: #для удаленных чисел ставших пустым местом или слипшихся
        appendFile.write(" " + sn_stemmer.stem(r)) #оставляем основу слова

  appendFile.write("!!!") #разделитель отзывов
  fil.close()

for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\Настя\aclImdb\train\pos"):
  fil = io.open(file.path, encoding = 'utf-8')
  words = fil.read().lower().split() # массив слов в нижнем регистре

  f += 1
  print(f)

  for r in words:

    if r not in stop_words:      #сначала убираем стоп-слова, тк в некоторых есть '

      r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
      if r != '' and r not in stop_words and r in spell: #для удаленных чисел ставших пустым местом или слипшихся
        appendFile.write(" " + sn_stemmer.stem(r)) #оставляем основу слова

  appendFile.write("!!!") #разделитель отзывов
  fil.close()

for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\Настя\aclImdb\test\neg"):
  fil = io.open(file.path, encoding = 'utf-8')
  words = fil.read().lower().split() # массив слов в нижнем регистре

  f += 1
  print(f)

  for r in words:

    if r not in stop_words:      #сначала убираем стоп-слова, тк в некоторых есть '

      r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
      if r != '' and r not in stop_words and r in spell: #для удаленных чисел ставших пустым местом или слипшихся
        appendFile.write(" " + sn_stemmer.stem(r)) #оставляем основу слова

  appendFile.write("!!!") #разделитель отзывов
  fil.close()

for file in os.scandir(r"C:\Users\asmis\OneDrive\Рабочий стол\Настя\aclImdb\test\pos"):
  fil = io.open(file.path, encoding = 'utf-8')
  words = fil.read().lower().split() # массив слов в нижнем регистре

  f += 1
  print(f)

  for r in words:

    if r not in stop_words:      #сначала убираем стоп-слова, тк в некоторых есть '

      r = re.sub("[^A-Za-z]", "", r)  # удаляем числа и знаки препинания из слова
      if r != '' and r not in stop_words and r in spell: #для удаленных чисел ставших пустым местом или слипшихся
        appendFile.write(" " + sn_stemmer.stem(r)) #оставляем основу слова
  if f != 50000:
    appendFile.write("!!!") #разделитель отзывов
  fil.close()

appendFile.close()
