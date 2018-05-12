from bs4 import BeautifulSoup
import requests
from idiom_database import Idiom, session

IDIOM_URL = "https://www.phrases.org.uk/idioms/a-z/full-list.html"

source = requests.get(IDIOM_URL).text

soup = BeautifulSoup(source, "html.parser")

idiom_links = []

for a in soup.find_all('p', class_="list-group-item-text"):
    all_link = a.find_all('a')
    for all in all_link:
        link = all['href']
        idiom_links.append(link)

for idiom in idiom_links:
    IDIOM_BASE_URL = "https://www.phrases.org.uk"
    idiom_source = requests.get(IDIOM_BASE_URL + idiom).text
    soup_idiom = BeautifulSoup(idiom_source, "html.parser")

    for a in soup_idiom.find_all("div", class_="idiom-container"):
        idiom_word = a.find('div', class_="idiom").text
        idiom_meaning = a.find('div', class_="idiom-meaning").text
        idiom_example = a.find('div', class_="idiom-example").text

        idiom_word = idiom_word.replace("\"", "").strip()
        query_idiom = session.query(Idiom)
        idiom_val = query_idiom.filter_by(word=idiom_word).first()
        if idiom_val:
            print(str(idiom_word.encode('utf-8')) + " --- Already exists")
            continue

        try:
            idiom_db = Idiom(word=idiom_word, meaning=idiom_meaning, example=idiom_example)
            session.add(idiom_db)
            session.commit()
            print(str(idiom_word.encode('utf-8')) + " --- Completed")
        except Exception as e:
            print(str(e) + " --- Exception in " + str(idiom_word.encode('utf-8')))
            continue

    print(str(idiom.encode('utf-8')) + " --- Completed")
