import Geometry

print("Calculating Area of a Circle")
Geometry.CircleArea()

#test RectangleArea()
print("Calculating Area of a Rectangle")
rlength=float(input("Enter length: "))
rbreadth=float(input("Enter breadth: "))
Geometry.RectangleArea(rlength, rbreadth)

#test TriangleArea()
print("Calculating Area of a Triangle")
tbase=float(input("Enter base: "))
theight=float(input("Enter height: "))
result=Geometry.TriangleArea(tbase, theight)
print("Total Area of the Triangle= %.2f" %result)
newresult=Geometry.TriangleArea(8)
print("New Area Of Triangle=%.2f"%newresult)
##y=math.sqrt(23)

for x in range (1,10,3):
