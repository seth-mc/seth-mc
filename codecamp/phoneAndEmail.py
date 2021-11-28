#! /usr/bin/env/python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegeX = re.compile(r'''
# 345-454-1010, 223-4040, (304) 282-2929, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?       # area code (optional)
(\s|-)                           # first separator
\d\d\d                           # first 3 digits
-                                # another seperator
\d\d\d\d                         # last 4 digits
(((ext(\.)?\s)|x)                 # extension word part (optional)
(\d{2,5}))?                        # extension number part (optional)
)
''', re.VERBOSE)


# Create a regex for emails
emailRegeX = re.compile(r'''
# some.+_thing@something.com, edu, gov,

[a-zA-Z0-9_.+]+       # name part
@                     # @ symbol
[a-zA-Z0-9_.+]+      # domain name part
''', re.VERBOSE)
# Get text off the clipboard
text = pyperclip.paste()

# extract the email and phone numbers
extractedPhone = phoneRegeX.findall(text)
extractedEmail = emailRegeX.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# copy found numbers and emails back to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
