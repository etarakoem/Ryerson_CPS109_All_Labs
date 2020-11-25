# # 1.
# def Lab_q1():
#     a = ()
#     for i in range(10):
#         input_a = input(f'Enter string {i}/10 ')
#         a = a+(input_a,)
#     for i in range(9,-1,-1):
#         print(f'String {i}/10: {a[i]}')
#     return
# Lab_q1()
#
# 2.
def max(L):
    # Set first maximum element
    maxL = None
    for i in L:
        if type(i)== float and maxL == None:
            maxL = i
            break
    for i in L:
        if type(i) == float and (i>maxL):
            maxL = i
    return maxL

sample_1 = [100.0,100, 'blue', 3.5, 'sugar on the rocks', 7.0,8.0]
sample_2 = [7, 2, 9, 1,9.0,10.0]
print(max(sample_1))
print(max(sample_2))
#
# 3.
# def longest(L):
#     largestyet = L[0]
#     for i in L:
#         if type(i) == str:
#             if len(i) > len(largestyet):
#                 largestyet = i
#     return largestyet
# sample = ['blue', 'red', 'the old barn', 'the white house', 'green']
# print(longest(sample))
#
# # 4.
# import random
# def q_4():
#     L = []
#     T = ()
#     # a) the numbers 1 to 100, inclusive.
#     for i in range(101):
#         L.append(i)
#         T = T+(i,)
#     # b) the odd numbers from 1 to 101, inclusive.
#     for i in range(1,102):
#         if i%2 == 1:
#             L.append(i)
#             T = T + (i,)
#     # c) the squares of numbers from 0 to 49, inclusive
#     for i in range(50):
#         L.append(i**2)
#         T = T + (i**2,)
#     # d) 60 random integers from 0 to 49, where you import random and use random.randrange(0, 50) to give
#     # each value
#     for i in range(60):
#         L.append(random.randint(0,50))
#         T = T + (random.randint(0,50),)
#     # e) 50 zeroes, i.e., [0, 0, ...., 0] and (0, 0, ..., 0). Note, you can use repetition, as you would for a string.
#     for i in range(50):
#         L.append(0)
#         T = T+(0,)
#     print(L)
#     print(T)
#     return
# q_4()
#
# # 5.
# import random
# def q_5():
#     # a) the numbers 1 to 100, inclusive.
#     a = [i for i in range(101)]
#     # b) the odd numbers from 1 to 101, inclusive.
#     b = [i for i in range(102) if i%2 ==1]
#     # c) the squares of numbers from 0 to 49, inclusive
#     c = [i**2 for i in range(50)]
#     # d) 60 random integers from 0 to 49, where you import random and use random.randrange(0, 50) to give
#     # each value.
#     d = [random.randint(0,50) for i in range(60)]
#     # e) 50 zeroes, i.e., [0, 0, ...., 0] and (0, 0, ..., 0). Note, you can use repetition, as you would for a string.
#     e = [0 for i in range(50)]
#     L = a+b+c+d+e
#     print(L)
#     return
# q_5()
#
# # 6.
# import math as m
# def perimeter(poly):
#     all_distance = [
#         m.sqrt(((poly[i+1][0]-poly[i][0])**2+(poly[i+1][1]-poly[i][1])**2))
#         for i in range(len(poly)-1)
#     ]
#     # Adding the first and last point
#     all_distance.append(m.sqrt(((poly[0][0]-poly[-1][0])**2+(poly[0][1]-poly[-1][1])**2)))
#     result = sum(all_distance)
#     return result
# # Simple square all side = 1
# square = [(0,0),(0,1),(1,1),(1,0)]
# print(perimeter(square))
# # Simple pythagoras triangle side 3,4,5
# triangle = [(0,0),(3,0),(0,4)]
# print(perimeter(triangle))
# # Simple rectangle with width,length = 3,4
# rectangle = [(0,0),(3,0),(3,4),(0,4)]
# print(perimeter(rectangle))
#
# 7.
import random
def permulation(L):
    # (0) initialize an empty list P and a copy of L: C = list(L)
    # (1) Use random.randrange(0, len(C)) to get a random index, i
    # (2) remove element i from the list C using pop() and
    # (3) append that element to the new list P
    # (4) repeat steps (1-3) until all the elmeents are transferred from C to P
    # (5) return the new list P
    P = []
    C = list(L)
    i = len(C)
    while i > 0:
        P.append(C.pop(random.randrange(0, len(C))))
        i = len(C)
    print(P)
    return
# 7.1:
print(" 1. Try your function on the sequence range(0, 30), which isn't a list,")
sequence = range(0,30)
permulation(sequence)
# 7.2:
print(" 2. Do that again to see that you get a new permuation")
permulation(sequence)
# 7.3:
print(" 3. Try it on [19, 4, 3, 17] two times.")
permulation([19,4,3,17])
permulation([19,4,3,17])
# 7.4:
print(" 4. Try it on poly = [(0, 0), (20, 0), (20, 10), (0, 10)] two times.")
poly_7 = [(0, 0), (20, 0), (20, 10), (0, 10)]
permulation(poly_7)
permulation(poly_7)

