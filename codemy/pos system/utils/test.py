import re
test = 'alpha11'
alnum = '1234567890qwertyuioplkjhgfdsazxcvbnm'
new = list(test)
new_alnum = list(alnum)
# print(new)
# if test.isalpha() or test.isnumeric():
#     print('true')
em= []
for l in new:
    if l not in new_alnum:
        print('incorrect password')
    else:
        print('corect')
        break

def check_pass():
    password = input("Enter your password ")
    while True:
        if not re.findall('[0-9]', password):
            return "make sure your password contain numbers"
        elif not re.findall('[Aa-zZ]', password):
            return  "make sure your password contain letters"
        else:
            return "your password is fine"
            break
password = 'aaa'
pattern = re.compile(r"")
pattern = re.compile(r'[A-Za-z0-9]')
result = pattern.match(password)
if result:
    print('a valid result')
else:
    print('not valid')
print(not password.isalpha())
# check_pass()