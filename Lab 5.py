# 1.
def add(a,b):
    if b == 1:
        return a+1
    else:
        return add(a,b-1)+1
print(add(16,9)) # Return 25

# 2.
def log2(x):
    if x <= 1:
        return 0
    else:
        return log2(x/2)+1
print(log2(2048)) # Return 11
import math as mt # Compare with Python's built in log2(x)
print(mt.log2(2048)) # Return 11.0

# 3.
def reverse(string):
    # Base case returns the last words
    if len(string) == 0:
        return string
    # General case returns the first letter, from back
    else:
        return reverse(string[1:])+string[0]
print(reverse('Who let the dogs out?')) # Return '?tuo sgod eht tel ohW'

# 4.
def power(x,n):
    # Base case return 1 as x^0 == 1
    if n == 0:
        return 1
    # General case return x times x
    else:
        return x*power(x,n-1)

print(power(2,11)) # print 2048

# 5.
def power(x,n):
    global countcalls
    # Base case return 1 as x^0 == 1
    if n <= 0:
        # Print the expected countcalls global variable outside of the function.
        print('--------------------------------------------------')
        print(f'expected {countcalls} time(s) of calling function')
        return 1
    # General case return x times x
    else:
        countcalls+=1
        return x*power(x,n-1)

countcalls = 0
print('Resutl of 5 to the power of 10 is ',power(5,10))
countcalls = 0
print('Resutl of 2 to the power of 10 is ',power(2,10))
countcalls = 0
print('Resutl of 5 to the power of 0 is ',power(5,0))

# 6.
def powerHalf(x,n):
    global countcalls
    # Base case return 1 as x^0 == 1
    if n <= 0:
        # Print the expected countcalls global variable outside of the function.
        print('--------------------------------------------------')
        print(f'expected {countcalls} time(s) of calling function')
        return 1
    # General case return whole value square if even power to reduce the function time calls
    if (n%2) == 0:
        countcalls+=1
        return powerHalf(x,n/2)**2
    # Otherwise return x times x if odd power
    else:
        countcalls += 1
        return powerHalf(x,n-1)*x
countcalls = 0 # Countcalls before was 10 at Q5
print("Result of 5 to the power of 10 is ",powerHalf(5,10)) # Countcalls is half as before
countcalls = 0 # Countcalls before was 10 at Q5
print("Result of 2 to the power of 10 is ",powerHalf(2,10)) # Count call is half as before
countcalls = 0
print("Result of 5 to the power of 0 is ",powerHalf(5,0))

# 7.
# Reading from a file
f = open('kdpF.txt') # opens a file for reading
line = f.readline() # reads a single line
print("First line was :",line)
seq = ''
for line in f : # reading the rest of the lines
    seq = seq + line
seq = seq.replace('\n', '') # removing the newline characters
seq = seq.upper()
print("DNA sequence after extract from file: ",seq)

def gcContent(sequence):
    print(f'% of either C or G is: {(sequence.count("C")/(len(sequence)) +sequence.count("G") / (len(sequence)))*100}%')

gcContent(seq) # Easily print out the result


