import re

def cleanBrackets(string):
    return re.sub("\[(.*?)\]", '', string)

def reduceNewline(string):
    return re.sub("(\n)+", '\n', string)

def removeNewline(string):
    return re.sub("(\n)+", '', string)

filters = [
  'Name',
  'Current Alias',
  'Physical Characteristics',
  'Origin',
  'Personal',
  'Creators'
]

def parseName(s):
    return s.replace('Name', '')

def parseAlias(s):
    return s.replace('Current Alias', '')

def parseChar(s):
    return s.replace('Physical Characteristics', '')

def parseOrigin(s): 
    return s.replace('Origin and Living Status', '').replace('Origin', '', 1)

def parsePersonal(s):
    return s.replace('Personal Information', '')

def parseCreators(s):
    return s.replace('Creators and Appearances', '').replace('Creators', '', 1).replace('First', ', First Appearance in ', 1)

filter_functions = [
    parseName,
    parseAlias,
    parseChar,
    parseOrigin,
    parsePersonal,
    parseCreators
]


def parseMetric(s):
    result = ''
    create = False
    index = 0
    while s[index] != ')':
        if create:
            result += s[index]
        if s[index] == '(':
            create = True
        index += 1
    
    result = result.split(' ')[0]
    result = float(result)
    return result


def parsePhysical(s): 
    result = {}
    try:
        # result['Gender'] = s.split('Gender', 1)[1].split('Height', 1)[0]
        result['Gender'] = re.split('(H|E)', s.split('Gender', 1)[1])[0]
    except:
        result['Gender'] = None
    try:
        chunk = s.split('Height', 1)[1].partition(')')
        result['Height(m)'] = '' + chunk[0] + chunk[1]
        result['Height(m)'] = parseMetric(result['Height(m)'])
    except:
        result['Height(m)'] = None
    try:
        result['Weight(kg)'] = s.split('Weight', 1)[1].split('Eyes', 1)[0]
        result['Weight(kg)'] = parseMetric(result['Weight(kg)'])
    except:
        result['Weight(kg)'] = None
    try:
        result['Eyes'] = s.split(':', 1)[1].split('Hair', 1)[0]
    except:
        result['Eyes'] = None
    try:
        result['Hair'] = s.split('Hair', 1)[1].split('Unusual Features')[0]
    except:
        result['Hair'] = None
    if result['Eyes'] != None and result['Eyes'].startswith('No Eyes'):
        result['Eyes'] = None
    if result['Hair'] != None and result['Hair'].startswith('No Hair'):
        result['Hair'] = None
    try:
        result['Unusual Features'] = s.split('Unusual Features', 1)[1]
    except:
        result['Unusual Features'] = None

    return result


def is_char_link(link):
    if link == None:
        return False
    elif link.startswith('/wiki') and link.endswith('616)'):
        return True
    return False


def is_next_link(class_name):
        class_str='pagination-next'
        if class_name == None:
          return False
        elif class_str in class_name:
          return True
        return False