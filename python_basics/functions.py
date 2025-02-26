import math

def calculate_area(shape,dimension1,dimension2=0):
    if shape=="circle":
        return math.pi*dimension1**2
    elif shape =="rectangle":
        return dimension1*dimension2
    elif shape=="triangle":
        return 0.5*dimension1*dimension2
    else:
        return"Invalid shape"
    
circle_area =( calculate_area("circle",10))
rectangle_area = calculate_area("rectangle",11,15)
triangle_area = calculate_area("triangle",3,16)

print(f"The area of the circle is :{circle_area:}")
print(f"The area of the rectangle is :{rectangle_area:}")
print(f"The area of the triangle is :{triangle_area:}")