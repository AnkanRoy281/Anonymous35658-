import requests
from bs4 import BeautifulSoup

def get_webpage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error:", response.status_code)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def display_webpage(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())

if __name__ == "__main__":
    url = input("Enter the URL of the webpage: ")
    webpage_content = get_webpage(url)
    if webpage_content:
        display_webpage(webpage_content)
