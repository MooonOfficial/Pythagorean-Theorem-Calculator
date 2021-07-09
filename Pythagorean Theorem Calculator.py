from math import sqrt
import time

mode = input("Find : \na. Hypotenuse of triangle \nb. Height of triangle \nc. Base of triangle\n\nChoose a,b, or c\n")
if mode == "a" :
    height = int(input("Height: "))
    base = int(input("Base: "))

    result = sqrt(base * base + height * height)

    print("The result is :")
    print(result)
    time.sleep(5)

if mode == "b" :
    hypotenuse = int(input("Hypotenuse: "))
    base = int(input("Base: "))

    result = sqrt(hypotenuse * hypotenuse - base * base)

    print("The result is :")
    print(result)
    time.sleep(5)

if mode == "c" :
    hypotenuse = int(input("Hypotenuse: "))
    height = int(input("Height: "))

    result = sqrt(hypotenuse * hypotenuse - height * height)

    print("The result is :")
    print(result)
    time.sleep(5)