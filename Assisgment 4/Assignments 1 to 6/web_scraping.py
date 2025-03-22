from bs4 import BeautifulSoup
import requests

def web_scraping():
    # user_input= input('Enter the the link of github user')
    user_input = "https://github.com/RaoHamzaTariq/"

    response = requests.get(user_input)
    soup = BeautifulSoup(response.content,'html.parser')
    profile_img=soup.find('img')['src']
    print(profile_img)

web_scraping()