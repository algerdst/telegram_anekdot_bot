import math
import random

import requests
from bs4 import BeautifulSoup

user_agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
}

filter_words=['украин', 'война','россия','путин','лукашенко','митинг', 'специальная военная операция']

categories = {
    'Детские': 'https://anekdoty.ru/detskie/',
    'Про программистов': 'https://anekdoty.ru/pro-programmistov/',
    'Тупые, но смешные': 'https://anekdoty.ru/tupo-no-smeshno/',
    'Про жену': 'https://anekdoty.ru/pro-zhenu/',
    'Короткие': 'https://anekdoty.ru/korotkie/',
    'Для взрослых': 'https://anekdoty.ru/pro-vzroslyh/',
    'Разные анекдоты': 'https://anekdoty.ru/samye-smeshnye/',
    'Анекдоты про Вовочку': 'https://anekdoty.ru/pro-vovochku/',
    'Анекдоты про подростков': 'https://anekdoty.ru/pro-podrostkov/',
    'Анекдоты про маму': 'https://anekdoty.ru/pro-mamu/',
}

def get_joke(cat):
    try:
        # Выбор категории
        url = categories[cat]

        # Запрос на первую страницу к категории
        response = requests.get(url, headers=user_agent)
        soup = BeautifulSoup(response.text, 'lxml')

        # Получение количества анекдотов в категории
        total_jokes_in_category = soup.find(class_='pagination-holder-current-page').text

        # Получение количества страниц в категории
        pages_in_category = math.ceil(int(total_jokes_in_category) / 20)

        # Получение рандомной страницы в категории
        random_page = random.randint(1, pages_in_category)

        # Запрос к рандомной странице
        if random_page==1:
            link=url
        else:
            link = f"{url}{random_page}/"
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        all_jokes = soup.find(class_='item-list').find_all(class_='holder-body')

        # Получение рандомной шутки
        count_jokes = len(all_jokes)
        index_random_joke = random.randint(0, count_jokes-1)
        joke = all_jokes[index_random_joke]
        joke=joke.text
        for word in filter_words:
            if word in joke.lower():
                joke=joke.lower().replace(word, '')
        return joke
    except:
        joke='Шутка удалена, давайте выберем другую'
