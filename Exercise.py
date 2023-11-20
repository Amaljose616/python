# To find the radius of a circle

# radius = float(input("Enter the radius of the circle: " ))
# import math
# pie = math.pi

# area = radius**2*pie

# print("The area of the circle is :"+ str(area))

# first_name = input("Enter the first name: ")
# last_name = input("Enter the last name: ")
# print(last_name+" "+first_name)

# values = input("Input some comma-separated numbers: ")
# list = values.split(",")
# tuple = tuple(list)
# print('List: ',list)
# print('Tuple :',tuple)

# file_name=input("Enter the file name :")
# list = file_name.split(".")
# print(list[1])

# color_list = input("Enter the color list as comma separted :")
# list = color_list.split(",")
# length = len(list)

# print("first_color:",list[0],"last_color:",list[length-1])

# exam_st_date = (11,12,2024)

# print("The examination will start from : %i / %i / %i" % exam_st_date)

# number = int(input("Enter the number :"))

# sum = number + int(str(number)+str(number)) + int(str(number)+str(number)+str(number))

# print(sum)

# def function(number):
#     print(number)

# function(12)

# print(abs.__doc__)

# import calendar

# yy = 2023
# mm = 11

# print(calendar.month(yy,mm))

# print("""
#       a string that you "don't" have to escape
#       This
#       is a ...... multi-line
#       heredoc string ------> example
#       """)

# from datetime import date

# first_Date = date(2024,7,2)
# last_Date = date(2024,7,11)

# print(first_Date)
# delta = last_Date - first_Date

# print(delta)

# radius = float(input("Enter the radius of the sphere : "))

# import math

# pie = math.pi

# volume = 4/3 * pie * radius**3

# print(volume)

# num = int(input("Enter the number"))

# if num > 17 :
#     result = (num - 17) * 2
# else :
#     result = (17 - num)

# print(result)

# num = int(input("Enter the number"))

# if 900 <= num <= 1000:
#     print("The number within 100 0f 1000")
# elif 1900 <= num <= 2100:
#     print("The number within 100 of 2000")
# else :
#     print("The number is not in the range")

# num1 = int(input("Enter three numbers : ")) 
# num2 = int(input("\t\t\t"))
# num3 = int(input("\t\t\t"))

# if num1 == num2 == num3 :
#     sum = (num1*3*2)
# else :
#     sum = num1 + num2 + num3
# print(sum)

# def sum_thrice(x,y,z):
#     sum = x + y + z
#     if x == y == z:
#         sum = sum * 3
#     return sum
# print (sum_thrice(3,3,3))

# def new_string(text):
#     if len(text) >= 2 and text[:2] == "Is":
#         return text
#     else :
#         return "Is" + text

# print(new_string("Isempty"))
# print(new_string("array"))

# print(".test"*3)

# num = int(input("Enter the number : "))

# def even_odd(value):
#     if value == 0:
#         print("The given number is zero")
#     elif value % 2 == 0 :
#         print("The given number is an even number")
#     else:
#         print("The given number is an odd number")

# even_odd(num)

# values = input("Enter the number as comma seperated :")

# numbers = values.split(",")

# length = len(numbers)
# a = 0

# for x in range(0, length):
#     if numbers[x] == "4":
#         a += 1

# print("Number of 4's in the input is :" + str(a))

# text = input("Enter the text :")

# print(text[:2] * 2)

def is_vowel(char) :
    all_vowels = 'aeiou'

    return char in all_vowels

print(is_vowel('c'))
print(is_vowel('e'))