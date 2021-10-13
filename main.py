print("welcome to Food debates where you can see the opinios of others regarding to certain dishes. Lets start easy shall we.") 
#WEB SCRAPING
#Chooes a sub reddit
#Goal: Print out usernames and their comments 
import requests
from bs4 import BeautifulSoup
import lxml

url=("https://www.reddit.com/r/AskReddit/comments/ogzxt1/whats_the_best_burger_chain_in_the_us/")
response=requests.get(url)
soup=BeautifulSoup(response.content,  "html.parser")


for item in soup.select('.Post'):
  try:
    print(item.select('._2mHuuvyV9doV3zwbZPtIPG')[0].get_text())
    print(item.select('_292iotee39Lmt0MkQZ2hPV RichTextJSON-root')[0].get_text())
  except Exception as e:
    #raise e
    print('')
