import collections
import csv
from csv import writer
file = open("filterAll.txt", encoding= "utf-8")
reviews = file.read().split(sep = '!!!')

print(len(reviews))

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text


#IDF
dict = {}
def analysis(my_list, dict):
  for i in my_list:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1


for review in reviews:
    review = review.split()
    analysis(review, dict)


import math

for key in dict:
  dict[key] = math.log10(25000/dict[key]) #idf dictionary
print(len(dict), "!!!@!!!")


#vectoriztion
vectors = open("vectors.csv", 'w')
writer = csv.writer(vectors)

f = 0
for review in reviews:
  review = review.split()
  rev = set(review)
  s = [0] * 33812
  i = 0
  count = compute_tf(review)
  for key in dict:
    if key in rev:
      tfidf = count[key] * dict[key]
      tfidf = '{:.3f}'.format(tfidf)
      s[i] =float(tfidf)
    i += 1

  writer.writerow(s)
  f += 1
  print(f)

file.close()
vectors.close()
