from doctest import master
import re

# Use brackets to compile regular expression pattern into groups
phregex = re.compile(r'\((\d\d\d)\)-(\d\d\d)-(\d\d\d\d)')

# search method is used to find single pattern in a string
matchObject = phregex.search('call me tonight (999)-959-5154 or 916-752-4168')

# | is a pipe character

batRegex = re.compile(r'bat(man|mobile|ball)')
mo = batRegex.search("I'm batball")
print(mo.group())

message = 'call me tonight 999-959-5154 or 916-752-4168'

# use this to compile
phregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Use brackets to compile regular expression pattern into groups
phregex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

# search method is used to find single pattern in a string
matchObject = phregex.search(message)

# To find all the pattern in a string
# This findall method returns result as a list
matchObjects = phregex.findall(message)

print(matchObject.group())

# If I supposed to print only first group
print(matchObject.group(1))

for i in range(0,len(matchObjects)):
    print(matchObjects[i])


# To check presence of regular expression in string one or zero time
batRegex = re.compile(r'bat(wo)?man')
mo = batRegex.search('I"m a batwoman')

# To check zero or more that zero pattern in a string
# We use * operator
batRegex = re.compile(r'bat(wo)*man')
mo = batRegex.search('I"m a batwowoman')

print(mo.group())
# To check one or more than one pattern in a string
# We use + operator
batRegex = re.compile(r'bat(wo)+man')
mo = batRegex.search('I"m a batwoman')


# To check exact number of string presence in regular expression
# We use {min_presence,max_presence} number pattern
batRegex = re.compile(r'bat(wo){2,5}man')
mo = batRegex.search('I"m a batwowoman')
print(mo.group())


# To check exact number of string presence in regular expression
# An expression may or may not present in the string for that use ? symbol

phoneNumber = re.compile(r'((\d\d\d-)?\d\d\d-?\d\d\d\d(,)?){3}')
mo = phoneNumber.search('my numbers are 989-989-9999,999-959-7777,343-5858')
print(mo.group())

# Greedy and Non-Greedy matching

# This finds all the number present in the sequence on string
numRegex = re.compile(r'\d{3,5}')
mo = numRegex.search('Hello it is greedy matching 12345')


# This finds only first three pattern present in the sequence on string
numRegex = re.compile(r'\d{5}?')
mo = numRegex.search('Hello it is non-greedy matching 12345')

print(mo.group())


# caret symbol is used to neglect the character
beginWith = re.compile(r'^hello')
mo = beginWith.search('hello')
print(mo.group())

# $ symbol is opposite to ^ symbol
# To find whether the pattern is present at the end of the string
endsWith = re.compile(r'hello$')
mo = endsWith.search('hi hello')
print(mo.group())

# . symbol is used to to find any string or letter 
cat = re.compile(r'.at')
# To detect more than one character mathcing pattern
cat = re.compile(r'.{2}at')
mo = cat.findall('hello bat mrat or cat')
print(mo)

# .* character
evy = re.compile(r'everything (.*)')
print(evy.findall('everything is being searched'))

both = re.compile(r'^\d+$')
print(both.findall("56789393"))

# Substitute functions in python
nameRegEx = re.compile(r'Agent (\w)\w+')
names = nameRegEx.findall('Agent tina met Agent daddy')
# To replace a particular expression from string
# use expression.sub('replacing string', 'whole string')
name = nameRegEx.sub('ME',"Agent tina met Agent daddy")

names = nameRegEx.sub(r'Agent \1*****',"Agent tina met Agent daddy")

vowelRegex = re.compile(r'[^aieou]',re.I)

pRegex = re.compile(r'''
    \d\d\d  #area code
    -   # first seperator
    \d\d\d  #next 3
    -   # second seperator
    \d\d\d\d    #last 4 digits
''', re.VERBOSE)
print(pRegex.findall('My number is 999-895-9296'))
