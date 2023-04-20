from bs4 import BeautifulSoup, NavigableString, Tag
import requests
from utility import is_char_link, is_next_link

startURL = 'https://marvel.fandom.com/wiki/Category:Characters?from=A'

def getCharURLs(start):
    char_set = set(())
    next_link = start

    page_count = 0

    while next_link != False:
      if page_count > 15:
        break
      page_count += 1

      req = requests.get(next_link)
      html = BeautifulSoup(req.text, 'html.parser')

      char_tags = html.find_all('a', href=is_char_link)
      for tag in char_tags:
        href = tag['href']
        char_set.add(href)

      next_link_tag = html.find('a', class_=is_next_link)
      if isinstance(next_link_tag, Tag):
        next_link = next_link_tag['href']
      else:
        next_link = False

    return char_set

# my_char_set = getCharURLs(startURL)
# for link in my_char_set:
#    print(link)
