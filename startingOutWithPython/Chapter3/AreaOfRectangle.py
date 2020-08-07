length_of_rectangle_one=int(input("Enter the lenth of the first rectangle: "))
width_of_rectangle_one=int(input("Enter the width of the first rectangle: "))

length_of_rectangle_two=int(input("Enter the lenth of the second rectangle: "))
width_of_rectangle_two=int(input("Enter the width of the second rectangle: "))

area_of_rectangle_one=length_of_rectangle_one*width_of_rectangle_one
area_of_rectangle_two=length_of_rectangle_two*width_of_rectangle_two

if(area_of_rectangle_one==area_of_rectangle_two):
    print("The two rectangles have equal areas.")
elif(area_of_rectangle_one>area_of_rectangle_two):
    print("Rectangle one has greater area.")
else:
    print("Rectangle two has greater area")