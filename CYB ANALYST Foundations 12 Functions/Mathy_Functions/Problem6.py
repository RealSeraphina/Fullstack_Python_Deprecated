# Define a function named area_of_triangle, 
# which takes two arguments as integers, base, 
# and height and returns the area of a triangle 
# of those dimensions. 
# Note: The formula for area of a triangle is base times height divided by 2

def area_of_triangle(base, height):
    area = (base * height) / 2
    return area

def main():
    print(str(area_of_triangle(3,4)))

if __name__ == "__main__":
    main()