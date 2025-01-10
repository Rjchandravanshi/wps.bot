import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def translate_website(url):
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    
    languages = ['es', 'fr', 'de', 'zh-cn', 'ar']
    translated_texts = {}
    
    for lang in languages:
        translated_texts[lang] = translator.translate(text, dest=lang).text
        with open(f"translated_{lang}.html", "w", encoding="utf-8") as f:
            f.write(translated_texts[lang])
    
    return languages
