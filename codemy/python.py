# secret_number = 4
# guess_number = 3
# count = 0
# num = 0
# while count < guess_number:
#     num = int(input("input the guess number"))
#     count += 1
#     if num == secret_number:
#         print('You win!')
#         break
# else:
#     print('sorry none of your guesses were right!')

# # Help = input('>')


# # while True:
# #      if Help == 'help' or Help == 'Help':
# #         reply = input("""Start - to start car
# #         Stop - to stop
# #         Quit - to quit 
# #           """)
# #         if reply == 'start':
# #             print('the car is started ready to go')
# #         elif reply == 'stop':
# #             print('The car is stopped')
# #         elif reply == 'quit':
# #             print('program quited')
# #             exit()
# #         else:
# #             print('invalid command! ')
    
# command = " "
# started = False

# print('Type help to get help')
# while True:
    
#     command = input(">>> ").lower()
#     if command == 'start':
#         if started:
#             print('car is already started')
#         else:
#             started = True   
#             print('car started..')
#     elif command == 'stop':
#         if not started:
#             print('car is already stopped')
#         else:
#             started = False
#             print('car stopped')
#     elif command == 'help':
#         print("""
# Start - to start the car
# Stop - To stop the car
# Quit - to quit
#         """)
#     elif command == 'quit':
#         break
#     else:
#         print('sorry this is not understood!')

for x in range(2):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
number2 = [2, 2, 2, 2, 2, 9]

for x_count in number2:
    #print('x' * x_count)
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers3 = [1, 2,2, 2, 3, 4, 4, 6, 4 ,7]
maximum = numbers3[0]

for x in numbers3:
    if x > maximum:
        maximum= x
print(f'the maximum number is: {maximum}')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[2][2]) 

for row in matrix:
    for item in row:
        print(item)

matrix.pop()
# matrix.clear()
print(matrix)
print(numbers3.index(7))
print(numbers3.count(2))
numbers3.sort()
print(numbers3)
numbers3.reverse()
print(numbers3)
num = numbers3.copy()
numbers3.append(10)
print(num)
print(numbers3)

uniques = []
for n in numbers3:
    if n not in uniques:
        uniques.append(n)
print(uniques)

# unpacking list and turples
cordinates = (1, 2, 3)
cordinates_list = [4, 2, 7]

x, y, z = cordinates

a, b, c = cordinates_list

print(c)

customer = {
    "name": "Olarinde Alli",
    'age': 222, 
    "is_verified":True
}
customer['name'] = 'Barokah'
print(customer.get('name', 'Olarinde Umar'))

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three"
# }  
# # output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, '!') + " "
# print(output)

# message = input(">>> ")
# words = message.split(" ")
# emojis = {
#     ":)": " "
# }

# print(words)
import pyautogui
import time
i = 0
while i < 3:
    pyautogui.typewrite("Hello ")
    time.sleep(3)
    pyautogui.press('Enter')
    i += 1