from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import re
from utility import *

def parseURLs(url): 
  result = requests.get(url)
  html = BeautifulSoup(result.text, 'html.parser')

  character_data = {'Character Endpoint': url.split('/')[-1]}

  basic_list = getBasics(html)
  for el in basic_list:
    character_data.update(el)

  quote_summary = getQuoteSummary(html)
  character_data.update(quote_summary)
  character_data['Physical Characteristics'] = parsePhysical(character_data['Physical Characteristics'])

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

