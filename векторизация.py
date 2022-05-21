X = open("filterAll.txt", encoding="utf-8").read().split(sep=' !!! ') #массив отзывов
y = [0] * 50000 #массив ответов к отзывам

import numpy as np

X = np.random.permutation(X)

for i in range(len(X)):
  y[i] = int(X[i][-1])
  X[i] = X[i][:-1]

X = list(X)
y = list(y)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
#tf-idf векторизация
#размерность вектора зависит от train, на одном из них 20329
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

train_x, train_y, test_x, test_y = [0]*5, [0]*5, [0]*5, [0]*5

for i in range(5):
  train_x[i] = vectorizer.fit_transform(X[:(4-i)*10**4] + X[(5-i)*10**4:]) #mb append
  train_y[i] = y[:(4-i)*10**4] + y[(5-i)*10**4:]
  test_x[i] = vectorizer.transform(X[(4-i)*10**4:(5-i)*10**4])
  test_y[i] = y[(4-i)*10**4:(5-i)*10**4]

#кроссвалидация train test split 0.8 0.2
#метрики
def metricsAll(test_y, a):
  for i in range(5):
    a[i] = list(a[i])
    
  metrics = [[0]*5 for i in range(5)]

  for i in range(5):
    metrics[0][i] = roc_auc_score(test_y[i], a[i]) # первая стр - ROC-AUC

  for i in range(5):
    metrics[1][i] = recall_score(test_y[i], a[i]) # вторая стр - Reacall

  for i in range(5):
    metrics[2][i] = accuracy_score(test_y[i], a[i]) # третья стр - Accuracy
  
  for i in range(5):
    metrics[3][i] = precision_score(test_y[i], a[i]) # четвёртая стр - Precision
  
  for i in range(5):
    metrics[4][i] = f1_score(test_y[i], a[i]) # пятая стр - F1
  
  #вычисляем для каждого отдельного разбиения на train test

  print("AUC-ROC: ", np.mean(metrics[0]), '+/-', np.std(metrics[0]))

  print("Recall: ", np.mean(metrics[1]), '+/-', np.std(metrics[1]))
  #доля объектов, названных классификатором положительными и при этом действительно являющимися положительными

  print("Accuracy: ", np.mean(metrics[2]), '+/-', np.std(metrics[2]))
  #доля объектов положительного класса из всех объектов положительного класса нашел алгоритм

  print("Precision: ", np.mean(metrics[3]), '+/-', np.std(metrics[3]))
  #доля объектов действительно принадлежащих данному классу относительно всех объектов которые система отнесла к этому классу

  print("F1 score: ", np.mean(metrics[4]), '+/-', np.std(metrics[4]))
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

a = []
for i in range(5):
  model1.fit(train_x[i], train_y[i])
  a.append(model1.predict(test_x[i]))

print("Random Forest classifier")
metricsAll(test_y, a)

print('Random classifier')

r = np.random.randint(0, 1 + 1, 50000)
metricsC(y, r)

print("Constant classifier")

c = [*np.random.randint(0, 1+1, 1)] * 50000
metricsC(y, c)

print("Random classifier in the same ratio as in answer")

k = [0]*5
for i in range(i):
  k[i] = test_y[i].count(0)/10000

r = [[0]*10**4 for i in range(5)]

for i in range(5):
  r[i] = np.random.choice(2, 10000, p= [k[i], 1-k[i]])

metricsAll(test_y, r)

from sklearn.naive_bayes import MultinomialNB
#Наивный Байес
print("Naive Bayes Classificator")
model2 = MultinomialNB()

b=[]

for i in range(5):
  model2.fit(train_x[i], train_y[i])
  b.append(model2.predict(test_x[i]))

metricsAll(test_y, b)

from sklearn.linear_model import LogisticRegression

print("Logistic Regression Model")

model3 = LogisticRegression()
b = []
for i in range(5):
  model3.fit(train_x[i], train_y[i])
  b.append(model3.predict(test_x[i]))

metricsAll(test_y, b)
