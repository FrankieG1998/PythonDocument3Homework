from math import pi

def sq_foot():
    length = float(input('Length? '))
    width = float(input('Width? '))
    return length * width

def circumference():
    radius = float(input('Radius? '))
    return 2 * pi * radius