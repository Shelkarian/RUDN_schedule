import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://portal.rudn-sochi.ru/login/index.php'

response = requests.get(LOGIN_URL)

soup = BeautifulSoup(response.text, 'lxml')
csrf_token = soup.find('input', attrs={'name': 'logintoken'})['value']

data = {
    'username': 'cug249mat',
    'password': '',
    'logintoken': csrf_token,

}

login = requests.post(LOGIN_URL, data=data)

result = requests.get('https://portal.rudn-sochi.ru/course/view.php?id=3660')
print(result.text)
if result.status_code == 200:
    print('Вроде работает..?')
else:
    print('А вроде нет...')