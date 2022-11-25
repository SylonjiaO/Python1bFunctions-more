#Function Examples

def CircleArea():
    try:
        radius=float(input("Enter Radius of the circle: "))
        area=3.14*radius*radius
        print("Area of a Circle= %.2f" %area)
    except ValueError:
        print("Sorry A Numerical Value was Expected")
    finally:
        print("Thank you, End of Program")

def RectangleArea(length, breadth):
    area=length*breadth
    print("Total Area of the rec= %.2f" %area)

def TriangleArea(base=5 , height=10): #specified args are default values
    area=.5*base*height
    return area
    
