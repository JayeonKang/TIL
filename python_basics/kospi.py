import requests


from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section').text
soup = BeautifulSoup(response,'html.parser')

#print(response)
#print(type(soup))

kospi = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
print(kospi.text)