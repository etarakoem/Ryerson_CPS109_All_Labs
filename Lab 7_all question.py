import unittest
def largestoffour(a,b,c,d):
    max = a
    if b>=c>=d>=max:
        max = b
    elif c>=b>=d>=max:
        max = c
    elif d>=c>=b>=max:
        max = d
    return max

class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(largestoffour(1,2,3,4),4)
 def test2(self):
  self.assertEqual(largestoffour(0,5,5,0),0)
 def test3(self):
  self.assertEqual(largestoffour(0,0,0,1),1)

if __name__ == '__main__':
 unittest.main(exit=True)

def q2(list):
    sum = 0
    for i in list:
        if i != 'Quit':
            sum += i
    return sum

