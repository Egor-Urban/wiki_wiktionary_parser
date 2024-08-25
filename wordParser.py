'''
            Парсер слов с wiktionary

            Описание: Программа для скачивания всех слов с сайта wiktionary, например списка большинства глаголов, сущестчительных и тд.
            Можно просто поменять ссылку и выходной файл для работы с нужной страницей

            ver. 1.7.6 r
            Разработчик: Urban Egor
            Разработано в России
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


if __name__ == "__name__":
    chrome_options = Options()
    service = Service()  # Использование Chrome из папки по умолчанию

    url = "" #Пример: 'https://ru.wiktionary.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5_%D0%B3%D0%BB%D0%B0%D0%B3%D0%BE%D0%BB%D1%8B'

    file = "" # Пример: 'data/pos/Verb.txt'
    btn_name = "" # Пример: 'Следующая страница'

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    with open(file, 'w', encoding='utf-8') as f:
        while True:
            elements = driver.find_elements(By.XPATH, "//*[@id='mw-pages']/div/div/div/ul/li/a")

            if not elements:
                print("Elem. not detect")
                break

            for elem in elements:
                adjective = elem.get_attribute('title')
                print(adjective)
                f.write(f"{adjective}\n")

            try:
                next_button = driver.find_element(By.LINK_TEXT, btn_name)
                next_button.click()
            except:
                print("Btn. not detected")
                break

    driver.quit()
