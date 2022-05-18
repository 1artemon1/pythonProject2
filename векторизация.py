n = open("filterNeg.txt", encoding="utf-8").read().split(sep='!!!')
p = open("filterPos.txt", encoding="utf-8").read().split(sep='!!!')

X = [] #массив отзывов
k, m = 0, 0
y = [0] * 50000 #массив ответов к отзывам

#чередуем позитивные и негативные отзывы, чтобы сохранялся баланс классов в любом train
for i in range(50000):
  if i%2 == 1:
    X.append(n[k])
    k += 1
  if i%2 == 0:
    X.append(p[m])
    y[i] = 1  # создаём ответы к отзывам       0 - neg, 1 - pos
    m += 1
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
#tf-idf векторизация
#размерность вектора зависит от train, на одном из них 20329

from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score


#кроссвалидация train test split 0.8 0.2
train1x = vectorizer.fit_transform(X[:40000]) #первые 40к отзывов
train1y = y[:40000]
test1x = vectorizer.transform(X[40000:])
test1y = y[40000:]


train2x = vectorizer.fit_transform(X[:30000]+X[40000:]) 
train2y = y[:30000]+y[40000:]
test2x = vectorizer.transform(X[30000:40000])
test2y = y[30000:40000]


train3x = vectorizer.fit_transform(X[:20000] + X[30000:])
train3y = y[:20000] + y[30000:]
test3x = vectorizer.transform(X[20000:30000])
test3y = y[20000:30000]


train4x = vectorizer.fit_transform(X[:10000] + X[20000:])
train4y = y[:10000] + y[20000:]
test4x = vectorizer.transform(X[10000:20000])
test4y = y[10000:20000]


train5x = vectorizer.fit_transform(X[10000:])
train5y = y[10000:]
test5x = vectorizer.transform(X[:10000])
test5y = y[:10000]

#метрики
def metricsAll(test1y, test2y, test3y, test4y, test5y, a1, a2, a3, a4, a5):
  r_a_s1 = [0] * 5
  rec1 = [0] * 5
  acc1 = [0] * 5
  prec1 = [0] * 5
  f1s1 = [0] * 5
  #вычисляем для каждого отдельного разбиения на train test
  r_a_s1[0] = roc_auc_score(test1y, a1)
  r_a_s1[1] = roc_auc_score(test2y, a2)
  r_a_s1[2] = roc_auc_score(test3y, a3)
  r_a_s1[3] = roc_auc_score(test4y, a4)
  r_a_s1[4] = roc_auc_score(test5y, a5)

  rec1[0] = recall_score(test1y, a1)
  rec1[1] = recall_score(test2y, a2)
  rec1[2] = recall_score(test3y, a3)
  rec1[3] = recall_score(test4y, a4)
  rec1[4] = recall_score(test5y, a4)

  acc1[0] = accuracy_score(test1y, a1)
  acc1[1] = accuracy_score(test2y, a2)
  acc1[2] = accuracy_score(test3y, a3)
  acc1[3] = accuracy_score(test4y, a4)
  acc1[4] = accuracy_score(test5y, a5)

  prec1[0] = precision_score(test1y, a1)
  prec1[1] = precision_score(test2y, a2)
  prec1[2] = precision_score(test3y, a3)
  prec1[3] = precision_score(test4y, a4)
  prec1[4] = precision_score(test5y, a5)

  f1s1[0] = f1_score(test1y, a1)
  f1s1[1] = f1_score(test2y, a2)
  f1s1[2] = f1_score(test3y, a3)
  f1s1[3] = f1_score(test4y, a4)
  f1s1[4] = f1_score(test5y, a5)


  print("AUC-ROC: ", np.mean(r_a_s1), '+/-', np.std(r_a_s1))

  print("Recall: ", np.mean(rec1), '+/-', np.std(rec1))
  #доля объектов, названных классификатором положительными и при этом действительно являющимися положительными

  print("Accuracy: ", np.mean(acc1), '+/-', np.std(acc1))
  #доля объектов положительного класса из всех объектов положительного класса нашел алгоритм

  print("Precision: ", np.mean(prec1), '+/-', np.std(prec1))
  #доля объектов действительно принадлежащих данному классу относительно всех объектов которые система отнесла к этому классу

  print("F1 score: ", np.mean(f1s1), '+/-', np.std(f1s1))
  #достигает максимума при максимальной полноте и точности


def metricsC(y, r): #для константных классификаторов
  print("AUC-ROC = ", roc_auc_score(y, r))
  print("Recall: ", recall_score(y, r))
  print("Accuracy: ", accuracy_score(y, r))
  print("Precision: ", precision_score(y, r))
  print("F1 score: ", f1_score(y, r))
  
  
 #Random Forest classifier
from sklearn.ensemble import RandomForestClassifier

model1 = RandomForestClassifier(n_estimators = 500, random_state = 1, n_jobs= -1 )

model1.fit(train1x, train1y)
a1 = model1.predict(test1x)

model1.fit(train2x, train2y)
a2 = model1.predict(test2x)

model1.fit(train3x, train3y)
a3 = model1.predict(test3x)

model1.fit(train4x, train4y)
a4 = model1.predict(test4x)

model1.fit(train5x, train5y)
a5 = model1.predict(test5x)

import numpy as np
print("Random Forest classifier")
metricsAll(test1y, test2y, test3y, test4y, test5y, a1, a2, a3, a4, a5)


print('Random classifier')

r = np.random.randint(0, 1 + 1, 50000)
metricsC(y, r)


print("Constant classifier")

c = [*np.random.randint(0, 1+1, 1)] * 50000
metricsC(y, c)


print("Random classifier in the same ratio as in answer")

randratio = np.random.choice(2, 50000, p= [0.5, 0.5])
  #в ответе распределение классов 1 к 1
metricsC(y, randratio)

from sklearn.naive_bayes import MultinomialNB
#Наивный Байес
print("Naive Bayes Classificator")
model2 = MultinomialNB()

model2.fit(train1x, train1y)
a1 = model2.predict(test1x)

model2.fit(train2x, train2y)
a2 = model2.predict(test2x)

model2.fit(train3x, train3y)
a3 = model2.predict(test3x)

model2.fit(train4x, train4y)
a4 = model2.predict(test4x)

model2.fit(train5x, train5y)
a5 = model2.predict(test5x)

metricsAll(test1y, test2y, test3y, test4y, test5y, a1, a2, a3, a4, a5)



from sklearn.linear_model import LogisticRegression

print("Logistic Regression Model")

model3 = LogisticRegression()

model3.fit(train1x, train1y)
a1 = model3.predict(test1x)

model3.fit(train2x, train2y)
a2 = model3.predict(test2x)

model3.fit(train3x, train3y)
a3 = model3.predict(test3x)

model3.fit(train4x, train4y)
a4 = model3.predict(test4x)

model3.fit(train5x, train5y)
a5 = model3.predict(test5x)

metricsAll(test1y, test2y, test3y, test4y, test5y, a1, a2, a3, a4, a5)
