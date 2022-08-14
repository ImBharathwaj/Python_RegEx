import re

"""
    RegEx for Phone Number
"""

# phone number patterns
# 990-9090, 444-555-6666, (555)-555-5555,(666) 777-9989, 777-879 ext. 1234, 777-989 x1234
phone = re.compile(r'''
    (((\d\d\d)|- (\(\d\d\d)\))?   # Area code
    (\s|-)?
    \d\d\d
    -
    \d\d\d\d
    (((ext(\.)?\s)|x)(\d{2,5}))?)
''',re.VERBOSE)

print(phone.findall('this is my phone number 999-808-9339'))
