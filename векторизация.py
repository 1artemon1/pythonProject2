from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

revTrain = open("filterTrain.txt", encoding="utf-8").read().split(sep='!!!')

train = vectorizer.fit_transform(revTrain)
print(*train.shape)

revTest = open("filterTest.txt", encoding="utf-8").read().split(sep='!!!')[:-1]
test = vectorizer.transform(revTest)
print(*test.shape)
#получаем разряженные векторы в матрице scipy matrix
#размерность вектора 1*20329
