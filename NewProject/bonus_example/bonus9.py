try:
    width = float(input("Enter a rectangle width: "))
    length = float(input("Enter a rectangle length: "))
    if width == length :
        exit("THat look like a square")
    area=length*width
    print(area)
except ValueError:
    print("Enter a valid number")