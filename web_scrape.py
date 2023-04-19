from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import re
from utility import *

url1 = 'https://marvel.fandom.com/wiki/Adam_Brashear_(Earth-616)'
url2 ='https://marvel.fandom.com/wiki/Victor_von_Doom_(Earth-616)'
url3 = 'https://marvel.fandom.com/wiki/Peter_Parker_(Earth-616)'
url4 = 'https://marvel.fandom.com/wiki/Kamala_Khan_(Earth-616)'
url5 = 'https://marvel.fandom.com/wiki/Anthony_Stark_(Earth-616)'
url6 = 'https://marvel.fandom.com/wiki/Reed_Richards_(Earth-616)'
url7 = 'https://marvel.fandom.com/wiki/Shen_Xorn_(Earth-616)' #No Quote or Summary
url8 = 'https://marvel.fandom.com/wiki/David_Haller_(Earth-616)' # Quote but no Summary

urls = [url1, url2, url3, url4, url5, url6, url7, url8]


def parseURLs(url): 
  result = requests.get(url)
  html = BeautifulSoup(result.text, 'html.parser')

  character_data = {'Character Endpoint': url.split('/')[-1]}

  basic_list = getBasics(html)
  for el in basic_list:
    character_data.update(el)

  quote_summary = getQuoteSummary(html)
  character_data.update(quote_summary)
  
  return character_data
  

def getQuoteSummary(html):
  quote = html.find(class_='quote')
  if quote == None:
    return {}
  
  next = quote.next_sibling
  summary = ''

  while not isinstance(next, Tag):
    next = next.next_sibling

  while next.attrs.get('id') != 'toc':
    summary += next.text
    next = next.next_sibling
    while not isinstance(next, Tag):
      next = next.next_sibling
    
  data = {'Quote': cleanBrackets(removeNewline(quote.text))}
  if len(summary) > 1:
    data['Summary'] = cleanBrackets(summary)

  return data


def getBasics(html):
  aside = html.find('aside')

  child_nodes = []
  for child in aside.children:
    if isinstance(child, NavigableString): 
      continue
    child_nodes.extend([child.text])

  data = []
  for item in (child_nodes):
    result = cleanBrackets(removeNewline(item))
    if result == '':
      continue
    if not result.startswith(tuple(filters)):
      continue
    for index, filter in enumerate(filters):
      if result.startswith(filter):
        char_data = {filter: filter_functions[index](result)}
        data.append(char_data)
    
  return data



for url in urls:
  character = parseURLs(url)
  for key in character:
    if key == 'Physical Characteristics' or key == 'Name' or key == 'Current Alias':
      print(key + ': ' + character[key])

  print('\n')

