import requests
from bs4 import BeautifulSoup

# <дата> - <заголовок> - <ссылка>
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')
posts = soup.find_all('article')

for artical in posts:
    head_post = artical.find(class_='post__title').text.strip()
    time_post = artical.find(class_='post__time').text.strip()
    link_post = artical.find(class_='post__title_link').get('href')
    text_post = artical.find(class_='post__body post__body_crop').text.strip()
    for comp_word in KEYWORDS:
        if (comp_word.lower() in head_post.lower()) or (comp_word.lower() in text_post.lower()):
            print(f'Дата: {time_post} | Заголовок: {head_post} | Ссылка: {link_post}')


