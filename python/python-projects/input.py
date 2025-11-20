name=input("Enter your name")
print("Hi " , name)

try: # errors handling 
    num=int(input("Enter a number")) #by default input is a string unless casted 
    print(num)
    num=num*2
    print(num)
except:
    print("You did not enter a number")

with open("movies.txt") as file:
    for line in file:
        print(line.strip())

with open("heights.txt") as file:
    for line in file:
        print(line.strip())
        info=line.strip().split()
        print(info)



