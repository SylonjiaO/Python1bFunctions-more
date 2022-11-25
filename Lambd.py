#Lambda Implementation

cube=lambda x: x**3
##mynum=int(input("Enter Your No :"))
##result=cube(mynum)
##print("Cube=%d"%result)

mylist=[12,5,-8,4,17,7,10,-3]
result=tuple(map(cube, mylist)) #no loop has to be created
print("Cube Results Are: ")
print(result) #map works in the deeper part of the memory for speed
#you have to convert map to a type list to view the values 

