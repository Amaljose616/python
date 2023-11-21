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

# def is_vowel(char) :
#     all_vowels = 'aeiou'

#     return char in all_vowels

# print(is_vowel('c'))
# print(is_vowel('e'))

# def is_group_member (group_data,n):
#     for value in group_data:
#         if n == value:
#             return True
#         else:
#             return False

# print(is_group_member([1,1,3,32,2,3],3))

# def histogram(items):
#     for n in items:
#         print("*"*n)

# print(histogram([2,3,6,5]))

# a = ""
# def concat(items):
#     for n in items:
#        a = a + str(n)
# return a
# print(concat([1,5,12,2]))

# def concat(list):
#     result = ''
#     for element in list:
#         result += str(element)
#     return result
# print(concat([1,5,2,12]))

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for x in numbers:
#     if x == 237:
#         print(x)
#         break
#     elif x % 2 == 0:
#         print(x)

# color_list_1 = ["white","Black","Red"]
# color_list_2 = ["red","Green"]
# # a = 0

# # for n in color_list_1:
# #     for m in color_list_2:
# #         if n != m:
# #             print(n)

# print(color_list_1.difference(color_list_2))
            
# Create two sets, color_list_1 and color_list_2.
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# # # Print the original elements of the sets.
# # print("Original set elements:")
# # print(color_list_1)
# # print(color_list_2)

# # Calculate and print the difference of color_list_1 and color_list_2.
# # print("\nDifference of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))

# # Calculate and print the difference of color_list_2 and color_list_1.
# # print("\nDifference of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))

# base = int(input("Enter the base of the triangle"))
# height =int(input("Enter the height of the triangle"))

# area = 1/2 * base * height

# print(area)

# a = int(input("Enter the first value :"))
# b = int(input("Enter the second value :"))
# if a > b:
#     if a % 2 == 0:
#         n = a/2
#     else:
#         n = (a+1)/2
# else:
#     if b % 2 == 0:
#         n = b/2
#     else:
#         n = (b+1)/2

# list = [" "]

# for x in range(1,int(n+1)):
#     if a % x == 0:
#         if b % x == 0:
#             h = x
#             list += str(h)
            
# print(list)

# print("GCM of the given two numbers is " + list[-1])
# print("LCM of the give two numbers is " + list[1])

# def lcm(x, y):
#     # Compare 'x' and 'y' to determine the larger number and store it in 'z'.
#     if x > y:
#         z = x
#     else:
#         z = y
    
#     # Use a 'while' loop to find the LCM.
#     while True:
#         # Check if 'z' is divisible by both 'x' and 'y' with no remainder.
#         if (z % x == 0) and (z % y == 0):
#             # If both conditions are met, 'z' is the LCM, so store it in 'lcm' and break the loop.
#             lcm = z
#             break
#         # If the conditions are not met, increment 'z' and continue checking.
#         z += 1
    
#     # Return the calculated LCM.
#     return lcm

# # Calculate and print the LCM of 4 and 6.
# print(lcm(3, 6))
# # Calculate and print the LCM of 15 and 17.
# print(lcm(15, 17))

# def sum(a,b,c):
#     if a == b or b == c or c ==a:
#         total = 0
#     else :
#         total = a + b + c
#     return total
# sum(1,2,3)
# print(sum(1,2,3))

# a = int(input("input a number : "))
# b = int(input("input the second number : "))
# # sum = a + b
# # if 15 <= sum <= 20 :
# #     sum = 20

# # print(sum)

# if a == b or a + b == 5 or a - b == 5 or b - a == 5:
#     print(True)

# x = 4
# y = 3

# result = (x + y) ** 2

# # print(str(x),"+",str(y)+"^"+"2"+"="+str(result))

# print("({} + {})^2) = {}".format(x,y,result))