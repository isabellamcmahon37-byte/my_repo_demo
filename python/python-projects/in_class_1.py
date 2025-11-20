for i in range(1,21):
    if i % 3 ==0:
        print(i)

counter = 1
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum = sum + counter
    else:
        sum = sum
    counter+=1
print(sum)

numbers = [5,8,2,15,10,3,7]

for num in numbers:
    if num>5:
        print(num, end=" ")
print()

lst=[1,2,3,4,5]
lst2=[]
lst2.append(lst[0])
for i in range(1,len(lst)):
    lst2.append(lst2[i-1]+lst[i])
print(lst2)

#functions 
def swap(lst):
    tmp=lst[0]
    lst[0]= lst[len(lst)-1]
    lst[len(lst)-1]= tmp

lst=[0,3,8,4,5]
swap(lst)
print(lst)