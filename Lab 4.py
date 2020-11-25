# # 1.
# def helloWorld():
#     print("Hello World!")
# # Call it once
# helloWorld()
#
# # Call it 10 times
# for i in range(10):
#     helloWorld()
#
# # 2.
# def hello(name):
#     print(f"Hello, {name}")
#
# # Main program:
# name_input = input("What's your name? ")
# # Greet the person
# hello(name_input)
#
#
# # 3.
# def hello(firstname, lastname):
#     print(f'Hello {firstname} {lastname}')
#     print(f'Hello {lastname} {firstname}')
# # # Main program:
# firstname_input = input("What's your firstname? ")
# lastname_input = input("What's your lastname? ")
# # Greet the person
# hello(firstname_input,lastname_input)
#
# # 4.
# def repeatPhrase(phrase, n):
#     for i in range(n):
#         if i % 2 == 0:
#             print(phrase.lower())
#         else:
#             print(phrase.upper())
# # Main program:
# string = input("Hey, gimme a phrase to repeat: ")
# times = int(input("Repeat for how many times? "))
# repeatPhrase(string,times)
#
# 5.
def timetable(n):
    for s in range(1,n+1):
        for i in range(1,n):
            if i*s < 10:
                print(i*s, end = "    ")
            else:
                print(i * s, end="   ")
        print((i+1)*s)
# Main program:
number = int(input("Gimme a number: "))
timetable(number)

# # 6.
# def perfectcube(n):
#     i = 0
#     if n < 0:
#         n = abs(n)
#     while i**3 <= n:
#         if i**3 == n:
#             return True
#         else:
#             i+= 1
#     return False
# # Main program:
# number = int(input("Gimme a number to check if perfectcube: "))
# print(perfectcube(number))
#
# # 7.
# def biggestOdd():
#     print('Start entering number until 0 to stop:')
#     number = int(input())
#     maxodd = number
#     count = 1
#     while number != 0:
#         number = int(input())
#         if number % 2 != 0:
#             count += 1
#             if count == 2:
# # In case the first odd number is less than the first number (if even)
#                 if maxodd % 2 == 0:
#                     maxodd = number
# # Compare and assign biggestOdd if an odd number is found
#             elif number > maxodd:
#                 maxodd = number
#     if maxodd % 2 == 0:
#         print(0)
#     else:
#         print(maxodd)
#     return
#
# biggestOdd()
#
# # 8.
# def biggestBuried(s):
#     max = -1
#     examine = ""
#     i = 0
#     while i < (len(s)):
#         j = 0
#         examine = s[i+j]
#         while examine.isdigit():
#             j+= 1
#             examine = s[i:i+j]
#             if i+j > len(s)+1:
#                 break
#             else:
#                 if examine.isdigit():
#                     if int(examine) >= max:
#                         max = int(examine)
#         if j == 0:
#             i+=1
#         else:
#             i += j
#     if max == -1:
#         return 0
#     else:
#         return max
# # Test working proof:
# print(biggestBuried('abcd51kkk3kk19ghi'))
# print(biggestBuried('kkk32abce@@-33bb14zzz'))
# print(biggestBuried('this15isast22ring-55'))
# print(biggestBuried('Nope'))
#
# # 9.
# def squareRoot(x, epsilon):
#     low = 0
#     high = max(1,x)
#     count = 0
#     guess = (low+high)/2
#     while abs(guess ** 2 - x) > epsilon:
#         if guess ** 2 > x:
#             high = guess
#         else:
#             low = guess
#         guess = (low+high) /2
#         count += 1
#         if count == 15:
#             break
#     return guess
#
# # Work proof
# print(squareRoot(0.25,0.001))
#
# # 10.
# def decimalToBinary(n):
#     original = n
#     if n == 0:
#         print('0 is the binary of 0')
#         return
#     a = ""
#     while n > 0:
#         a = a+str(n%2)
#         n = n//2
#     print(f'{a[::-1]} is the binary of {original}')
#
# # Main program:
# for i in range(10):
#     decimalToBinary(i)
