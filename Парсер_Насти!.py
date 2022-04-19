from bs4 import BeautifulSoup as BS
import requests
import warnings
import pandas as pd
#если брать страницы по 200 отз на каждой, то в итоге будет 4к отзывов, часть будет повторяться из-за нескольких жанров у фильма
warnings.filterwarnings('ignore')

df = pd.DataFrame({"NameR", "NameEn", "Year", "Genre","Review"}) 


genres = [3, 13, 19, 17, 20, 12, 8, 6, 15, 16, 7, 21, 14, 9, 10, 11, 4, 1, 2, 5] #по алфавиту

#reviewItems = html.find_all(class_= "reviewItem userReview")
for genre in genres:
  req = requests.get('https://www.kinopoisk.ru/reviews/type/comment/sort/date/period/month/feature/all/genre/'+ str(genre) + '/') # получаем содержимое стр'
  html = BS(req.content, 'html.parser') 
# создаём объект BS, который нужен для приёма данных через req.content, сообщаем, что это html документ
  reviewItems = html.find_all(class_= "reviewItem userReview")
  for item in reviewItems:
    name_full = item.find(class_="film").find("b").text.strip()
    nameEng = name_full[:-6] # назв на англ
    year = name_full[-5:-1] # год
    nameR = item.find(class_="film").find("span").text.strip() # назв на русском
    review = item.find(class_="brand_words").find("p").text.strip() # отзыв
    grade = "-" #оценка
    if item.find(class_='response good') != None:
      grade = "response good"
    if item.find(class_='response bad') != None:
      grade = "response bad"
    print(nameR, nameEng, year, genre, grade)
    new_row = {"NameR" : nameR, "NameEn" : nameEng, "Year" : year, "Genre" : genre, "Review" : review}
    df.append(new_row, ignore_index=True)

print(df) #кажется, пока не получилось данные сохранить 