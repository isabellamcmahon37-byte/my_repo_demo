print(" Hello World")

# this is a single line comment 

'''
line 1 
line 2 
line 3
'''

# x=10  crtl + / to comment out 
# y=1
# z=9

#Variables
x = 10 
y = 5.1 
x = "hello"
print(x) 

# math operators 
x = 100
y = 3
z = x / y 
#z = int(z)
z = x // y 
print(z)

min_val = min(10,1)
print(min_val)
raised = 2**4
print(raised)
raised = pow(2,4)
print(raised)

if x<0:
    print("negative")
else: 
    print("positive")

if x<0 and y<0:
    print("both negative")

if x<0 or y<0:
    print("one is negative")

if x<0:
    print("negative")
elif y<0:
    print("negative")
else:
    print("positive")

counter=0 
while counter<10:
    print(counter)
    counter+=1 

for i in range(10):
    print(i)

lst=[1,2,3,4,5]
for i in range(len(lst)):
    print(i, lst[i])

for i in range(1,len(lst)):
    print(i, lst[i])

for i in range(len(lst)-1,-1,-1): # range(start, end, inc) 
    print(i, lst[i])


for i,val in enumerate(lst):
    print(i,val)

for value in lst:
    print(value)

def hello_world(): 
    print("hello world")
hello_world()

def hello(name = "bud"): #default value 
    print("hello", name)
hello("Bob")
hello()

# string slicing 
full_name="Kathleen Malone" 
t=full_name[2]
e=full_name[-1]

first_name=full_name[0:8]
print(first_name) 
last_name=full_name[9:15]
print(last_name)

