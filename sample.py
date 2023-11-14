# first_member = input("Enter father name :")
# second_member = input("Enter Mothers name :")
# third_member = input("Enter next member name :")
# fourth_member = input("Enter the last member name :")
# family = [first_member,second_member,third_member,fourth_member]
# Output = "In you family there is " +  str(len(family)) + " members. And the members are" + str(family)
# print(Output)

# if len(family)==4 :
#     print("family having 4 members")
# else :
#     print("The number of members in the family is not 4")

# name = "amal"
# names = ["am","arj","ded","des"]
# print(name[3])
# names += ["sed"]
# names.append("hello")
# new = input("enter new value")
# names.append(new)
# names[0] = "udemy"
# print(names)

# num = int(input("enter a new number "))
# if num < 0 :
#     print("The entered number is a negative number")
# elif num == 0 :
#     print("the entered number is zero")
# else :
#     print("The entered number is a positive number")
# i = 1
# while i<=10 :
#     print(i)
#     i+=1
# else :
#     print("Loop ended")

# menu = ["porotta","Biriyani","Rice","Mandhi","Pathiri"] 
# menu[2] + "h"
# print(menu)
# for x in menu :
#     print(x)

# menu = int(input("Enter your selection number"))

# if menu == 1 :
#     print("You have ordered Porotta")
# elif menu == 2 :
#     print("You have ordered Biriyani")
# elif menu == 3 :
#     print("You have ordered Rice")
# elif menu == 4 :
#     print("You have ordered Mandhi")
# else :
#     print("You have ordered Pathiri")

# row = int(input("Enter the number of rows"))
# a = "*"
# count = 1
# while row > 0:
#     print(""*row+a*count)
#     row = row -1
#     count = count + 1

# num = int(input("Enter the number of lines"))
# numStar = 1
# numSpace = num - 1
# while num > 0:
#     print(""*numSpace+"*"*numStar+"\t"*numSpace+"\n")
#     numSpace = numSpace - 1
#     numStar = numStar + 2
#     num = num - 1

# num = int(input("Enter the number of rows"))
# count = 1
# while num > 0 :
#     print(""*num + "*"*count)
#     num -= 1
#     count += 1

# while num < 10 :
#     print (num)
#     num += 1

# files = ["CIA.mp4","Moosa.mp3","marvel.mp4"]
# for x in files :
#     # print(len(x))
#     # if files[len(x) - 1] == 3:
#     #     print(x)
#     # a = len(x) - 1
#     # print[a]
#     # print(files[a])
#     print(x[0:-4])

# for x in range(19):
#     print(x)

# multi = int(input("Which numbers multiplication you want : "))
# num = int(input("Limit for the number : "))
# for x in range(num) :
#     print(multi * num)
#     num -= 1

number = int(input("Enter the number of multiplication table: "))
limit = int(input("Enter the limit"))
a = 1
# for limit in range(1,limit+1):
#     print(limit,'X',number,'=',number * limit)
for x in range(1,limit + 1, number):
    print(a,'X',number,'=',x)
    a += 1