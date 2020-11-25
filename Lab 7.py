'''
Write a recursive function trim(s) in q6.py,
which returns a string which is the same as string s, but with no blanks at the front or end of the string.
For example trim('   dog   ') returns 'dog'.
Example 2: trim('    cat in the hat') returns 'cat in the hat'.
Notice that blanks that are not at the beginning or end are left as they are.
Example 3: trim('')  and trim('       ') both return the empty string.
You must use recursion.
Do not use built in functions that trim, like rtrim().
'''
def trim(s):
    # Base case:
    if s == '':
        return s
    if s[0] == ' ':
        begin = 1
    if s[-1] == ' ':
        end = -1
    else:
        end = len(s)-1
    if (s[0] != ' ' and s[end] != ' '):
        return s
    else:
        while True:
            return trim(s[begin:end])

'''
Write a function trim(s) in q5.py, 
which returns a string which is the same as string s, but with no blanks at the front or end of the string.  
For example trim('   dog   ') returns 'dog'.  
Example 2: trim('    cat in the hat') returns 'cat in the hat'.  
Notice that blanks that are not at the beginning or end are left as they are.  
Example 3: trim('')  and trim('       ') both return the empty string.  
Do not use recursion and do not use built in functions that trim, like rtrim(). 
'''
# def trim(s):
#     if s == '' or (s.count(' ') == len(s)):
#         return ''
#     begin = 0
#     end = len(s)
#     if s[0] == ' ':
#         for i in s:
#             if i != ' ':
#                 begin = s.index(i)
#                 break
#     if s[-1] == ' ':
#         for i in s[-1]:
#             if i != ' ':
#                 end = s.index(i)
#
#     return s[begin:end]

#
# example1 = '   dog   '
# example2 = '    cat in the hat'
# example3 = '      '
# # print(f"'{trim(example1)}' from original: '{example1}'")
# # print(f"'{trim(example2)}' from original: '{example2}'")
# print(f"'{trim(example3)}' from original: '{example3}'")
# # print(example1.count(' '))

import unittest
# --------------------------------------------------------------
# Sum = 1/1 + 1/2 + 1/3 + ... + 1/n
# --------------------------------------------------------------
def series0(epsilon) :
    '''
    Return the value of n such that the above sum is
    within epsilon of 4.23.
    For example,
    if epsilon is 4, then return 1, since 1 the first term is within 4 of 4.23
    if epsilon is 3, then return 2, since 1 + 1/2 = 1.5 is within 3 of 4.23
    '''
    sum = 1
    n = 1
    target = 4.23
    while abs(sum-target)>epsilon:
        n+=1
        sum += 1/n
    print(sum)
    return n

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(series0(4), 1)
 def test2(self):
  self.assertEqual(series0(3), 2)
 def test3(self):
  self.assertEqual(series0(1), 14)
 def test4(self):
  self.assertEqual(series0(0.5), 23)
 def test5(self):
  self.assertEqual(series0(0.01), 38)


if __name__ == '__main__':
 unittest.main(exit=True)




# --------------------------------------------------------------
# The End
# --------------------------------------------------------------