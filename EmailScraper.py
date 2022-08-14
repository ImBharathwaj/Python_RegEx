import re

"""
    RegEx for Email Scrapping
"""

# Email Scraping
email = re.compile('''
    [a-zA-Z0-9+_.]+
    @
    [a-zA-Z0-9+_.]+
''',re.VERBOSE)

print(email.findall('nothing is my mail bharathwaj@udemy.com'))
