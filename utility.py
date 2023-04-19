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