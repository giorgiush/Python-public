# a = input().split(" ")
# print(max(a))
# for i in range(0, len(a)):
#     a[i] = int(a[i])
# print(sum(a))

      # FIND THE HIGHEST NUMBER
# number_list = input("Enter numbers:\n").split()
# for n in range(0, len(number_list)):           #range does NOT include the last number
#     number_list[n] = int(number_list[n])
#
#     # hard way
# # for number in number_list:
# #     items = 0
# #     for index in range(0, len(number_list)):
# #         if number >= number_list[index]:
# #             items += 1
# #             if items == len(number_list):
# #              print(f"The highest number is {number}")
#     # easy way
# highest = 0
# for number in number_list:
#     if number > highest:
#         highest = number
# print(f"The highest number is {highest}")


#range(start:1, stop:10, step:3)  #range does NOT include the last number





          # PASSWORD GENERATOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("PASSWORD GENERATOR")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input(f"How many symbols?\n"))
nr_numbers = int(input(f"How many numbers?\n"))

password = []
random_password = []

for i in range(0, nr_letters):
    password.append(letters[random.randint(0, 51)])

for i in range(0, nr_numbers):
    password.append(numbers[random.randint(0, 9)])

for i in range(0, nr_symbols):
    password.append(symbols[random.randint(0, 8)])

for i in range(0, nr_numbers+nr_symbols+nr_letters):
    random_password.append(password[random.randint(0, nr_letters+nr_symbols+nr_numbers)-1])

# print(''.join(random_password))
# print(*random_password, sep='')

random.shuffle(password)
print(''.join(password))
