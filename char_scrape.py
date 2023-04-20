from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import os
import json
from utility import is_char_link, is_next_link
# original page
# "https://marvel.fandom.com/wiki/Category:Characters?from=A"

def getCharURLs():
  path = 'char_data'
  read_path = os.path.join(path, 'current_page.json')
  with open(read_path, 'r') as f:
    current = json.load(f)

  char_set = set(())
  next_link = current['next_page']
  page_original = current['page_index']
  page_current = current['page_index']

  while next_link != False:
    if page_current - page_original >= 10:
      break
    page_current += 1
    print('On page', page_current)
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

  current['page_index'] = page_current
  current['next_page'] = next_link

  with open(read_path, 'w') as f:
    json.dump(current, f, indent=2)

  write_path = os.path.join(path, f"page{page_original}_page{page_current}.json")
  with open(write_path, 'w') as f:
    json.dump(list(char_set), f, indent=2)

  return

