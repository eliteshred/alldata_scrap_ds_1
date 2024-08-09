import requests as rq

from bs4 import BeautifulSoup
from bs4 import NavigableString

bUrl = 'https://books.toscrape.com/'

bHeader = {'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}


bResp = rq.get(url=bUrl, headers= bHeader)

bSoup = BeautifulSoup(bResp.content, 'html.parser')

allarticle = bSoup.find_all('article')
#print(allarticle)

# ftitle = allarticle[0].h3.a.attrs['title']
# #print(ftitle)
      
# frate = allarticle[0].find('p').attrs['class'][1]
# # print(frate)

# fprice = allarticle[0].find('p',attrs={'class': 'price_color'}).getText().split('£')[1]
# #print(fprice)

books = []
for i in range(20):
    book = {
        "title": allarticle[i].h3.a.attrs['title'],
        "rate": (allarticle[i].find('p').attrs['class'][1]),
        "price": allarticle[i].find('p', attrs={'class': 'price_color'}).getText().split('£')[1]
    }
    books.append(book)

for book in books:
    print('All_List_of_books')
    print("Title:", book["title"])
    print("Rate:", book["rate"])
    print("Price:", book["price"])
    print("-" * 20)






