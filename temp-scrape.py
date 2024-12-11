import requests
import selectorlib
from datetime import datetime

URL="https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ' \
    'Safari/537.36'}

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_string("""
    temp:
        css: '#temperatureId'                                                      
    """)
    value = extractor.extract(source)["temp"]
    return value

def store(temp):
    with open("data-temp/data.txt", "a") as file:
        now = datetime.now() 
        date_time = now.strftime("%y-%m-%d-%H-%M-%S")       
        file.write(f"{date_time},{temp}\n")

if __name__ == "__main__":
    source = scrape(URL)
    temp = extract(source)
    store(temp)

