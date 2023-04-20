from web_scrape import parseURLs
from char_scrape import *

url1 = 'https://marvel.fandom.com/wiki/Adam_Brashear_(Earth-616)'
url2 = 'https://marvel.fandom.com/wiki/Victor_von_Doom_(Earth-616)'
url3 = 'https://marvel.fandom.com/wiki/Peter_Parker_(Earth-616)'
url4 = 'https://marvel.fandom.com/wiki/Kamala_Khan_(Earth-616)'
url5 = 'https://marvel.fandom.com/wiki/Anthony_Stark_(Earth-616)'
url6 = 'https://marvel.fandom.com/wiki/Reed_Richards_(Earth-616)'
url7 = 'https://marvel.fandom.com/wiki/Shen_Xorn_(Earth-616)' #No Quote or Summary
url8 = 'https://marvel.fandom.com/wiki/David_Haller_(Earth-616)' # Quote but no Summary
url9 = 'https://marvel.fandom.com/wiki/Emma_Frost_(Earth-616)'
url10 = 'https://marvel.fandom.com/wiki/Wanda_Maximoff_(Earth-616)'

urls = [url1, url2, url3, url4, url5, url6, url7, url8]

urls = [url9, url10]


# for url in urls:
#   character = parseURLs(url)
#   for key in character:
#     print(key + ': ', character[key])

#   print('\n')

my_char_set = getCharURLs(startURL)

# # count = 0
# for link in my_char_set:
#   try: 
#     current_URL = 'https://marvel.fandom.com' + link
#     character = parseURLs(current_URL)
#     for key in character:
#       print(key + ':', character[key])
#   except:
#     continue
  
#   # if count > 15:
#   #   break
#   # count +=1

#   print('\n')

for link in my_char_set:
    print(link)