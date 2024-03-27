import requests
from bs4 import BeautifulSoup

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Sec-Fetch-Site': 'same-origin',
  'Cookie': 'ingress-session-key=1711539788.195.171.370309|c81450cf7ec59afd5378489bed00d6c1; tmr_detect=0%7C1711536181738; tmr_lvid=2856009d6c9fbfd35fea5102729f29a7; tmr_lvidTS=1711489591752; _ym_d=1711489592; _ym_isad=2; _ym_uid=1711489592806536551; flocktory-uuid=373ac45b-15ef-45d1-80f7-7209182728f1-5',
  'Sec-Fetch-Dest': 'document',
  'Accept-Language': 'ru',
  'Sec-Fetch-Mode': 'navigate',
  'Host': 'dominopizza.ru',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
  'Referer': 'https://www.google.com/',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}


url = 'https://dominopizza.ru'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

container = soup.find_all('div', class_='product-card-content')

datas = []
for i in container:
    name = i.find('div', class_='product-name').text
    description = i.find('div', class_='description-container').text
    price = i.find('div', class_= 'price').text
    datas.append((name, description, price))
