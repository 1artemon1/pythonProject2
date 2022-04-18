import bs4
import csv
import requests
from bs4 import BeautifulSoup
from film import Films

PAGES = 30
# URL = 'https://www.kinopoisk.ru/reviews/type/comment/period/month/'
HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.75 Safari/537.36 '
}


def get_html(url, params=None):
    try:
        html = requests.get(url, params=params, headers=HEADERS)
    except Exception as e:
        print(f'Error : {e}')
        return
    return html


def parser(soup: bs4.BeautifulSoup, list_of_films: list):
    films = soup.findAll('div', {'itemtype': "http://schema.org/Review"})
    for film in films:
        name = film.find('span', {'itemprop': 'name'}).text.replace(u'\xa0', ' ')
        text = film.find('span', {'itemprop': 'reviewBody'}).text.replace(u'\xa0', ' ').replace(u'\x97', '-').replace(
            u'\x85', ' ')
        response = film['class']
        list_of_films.append(Films(name=name, text=r'{}'.format(text), response=response).Tuple())


def main():
    list_of_films = []
    for i in range(1, PAGES + 1):
        html = get_html(f'https://www.kinopoisk.ru/reviews/type/comment/period/month/page/{i}/#list')
        soup = BeautifulSoup(html.text, 'lxml', multi_valued_attributes=None)
        parser(soup, list_of_films)
    with open("kinopoisk.csv", 'w') as data:
        writer_csv = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer_csv.writerow(('НАЗВАНИЕ', 'ОТЗЫВ', 'ОЦЕНКА'))
        writer_csv.writerows(list_of_films)
    print(list_of_films)


if __name__ == '__main__':
    main()
