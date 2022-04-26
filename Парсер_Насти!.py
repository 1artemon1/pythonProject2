from bs4 import BeautifulSoup as BS
import requests

import pandas as pd
#если брать страницы по 200 отз на каждой, то в итоге будет 4к отзывов, часть будет повторяться из-за нескольких жанров у фильма

genres = [3, 13, 19, 17, 20, 12, 8, 6, 15, 16, 7, 21, 14, 9, 10, 11, 4, 1, 2, 5] #по алфавиту
df = pd.DataFrame(columns = ["NameR", "NameEng", "Year", "Genre", "Grade", "Review"])


for genre in genres:
  req =requests.get('https://www.kinopoisk.ru/reviews/type/comment/genre/'+ str(genre) + '/period/month/perpage/50/#list') # получаем содержимое стр'
  html = BS(req.content, 'html.parser') 
# создаём объект BS, который нужен для приёма данных через req.content, сообщаем, что это html документ
  reviewItems = html.find_all(class_= "reviewItem userReview")
  for item in reviewItems:
    name_full = item.find(class_="film").find("b").text.strip()
    nameEng = name_full[:-6] # назв на англ
    year = name_full[-5:-1] # год
    nameR = item.find(class_="film").find("span").text.strip() # назв на русском
    review = item.find(class_="brand_words").find("p").text.strip() # отзыв
    grade = None #оценка
    if item.find(class_='response good') != None:
      grade = 1
    if item.find(class_='response bad') != None:
      grade = -1

    new_row = {"NameR" : nameR,"NameEng" : nameEng, "Year" : year, "Genre" : str(genre), "Grade" :grade, "Review" : review}
    df.loc[len(df.index)] = new_row #добавляем строку

    
df.to_csv("file.csv")
