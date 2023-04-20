import os
import json
from web_scrape import parseURLs
from char_scrape import getCharURLs

url1 = 'https://marvel.fandom.com/wiki/Adam_Brashear_(Earth-616)'
url2 = 'https://marvel.fandom.com/wiki/Victor_von_Doom_(Earth-616)'
url3 = 'https://marvel.fandom.com/wiki/Peter_Parker_(Earth-616)'
url4 = 'https://marvel.fandom.com/wiki/Kamala_Khan_(Earth-616)'
url5 = 'https://marvel.fandom.com/wiki/Anthony_Stark_(Earth-616)'
url6 = 'https://marvel.fandom.com/wiki/Reed_Richards_(Earth-616)'
url7 = 'https://marvel.fandom.com/wiki/Shen_Xorn_(Earth-616)' #No Quote or Summary\dl-gen9paldeadexposthomedraft-41001-5jxvekuczlz8ba7afzt6oth5o0u4ut3pw
url8 = 'https://marvel.fandom.com/wiki/David_Haller_(Earth-616)' # Quote but no Summary
url9 = 'https://marvel.fandom.com/wiki/Emma_Frost_(Earth-616)'
url10 = 'https://marvel.fandom.com/wiki/Wanda_Maximoff_(Earth-616)'

urls = [url1, url2, url3, url4, url5, url6, url7, url8]

# for url in urls:
#   character = parseURLs(url)
#   for key in character:
#     print(key + ': ', character[key])

#   print('\n')

# getCharURLs()
path = 'char_data'
read_path = os.path.join(path, 'page0_page10.json')
with open(read_path, 'r') as f:
  my_char_set = json.load(f)
# count = 0
for link in my_char_set:
  # if count > 15:
  #   break
  # count +=1
  try: 
    current_URL = 'https://marvel.fandom.com' + link
    character = parseURLs(current_URL)
    if not 'Quote' in character:
      continue
    for key in character:
      print(key + ':', character[key])
  except:
    continue
  print('\n')

