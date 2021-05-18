import array as arr
i = 0
x = 150
a = arr.array ('i', [1,2,3])
b = arr.array ('d', [2.5,3.7,23.76, 24.0])
c = ['sarah','joe','15734','42','a2135']

while x != 0:
    print(x)
    x = x - 10

print ("The integer array is : ", end ="  ")
for i in range (0,3):
    print (a[i], end ="  ")
print ()

i = 0

print ("The double array is : ", end ="  ")
for i in range (0,4):
    print (b[i], end ="  ")
print ()

i = 0

print ("The double array as integers is : ", end ="  ")
for i in range (0,4):
    print (int(b[i]), end ="  ")
print ()

i = 0

print ("The char array is : ", end ="  ")
for i in range (0,5):
    print (c[i], end ="  ")
print ()
