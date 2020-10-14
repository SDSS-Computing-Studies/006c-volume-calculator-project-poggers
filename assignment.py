#!python3
# Volume Calculator
# Feel free to rename your variables

import math
import os

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Catrina
    # Modified:
    print("\n=================================")
    print("Welcome to the Volume Calculator! \n=================================")
    print("\nThis program was created by the Poggers!\n")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Catrina
    # Modified:
    while True:
        print("This program has been designed to calculate the volume of your desired shape.")
        print("To use this calculator you will:")
        print("Step 1: You will choose a shape.")
        print("Step 2: You will be prompted to enter the necessary parameters for the shape. ")
        print("Step 3: You will be asked to confirm your measurements.")
        print("Step 4: The program will run and you will be given the area of your shape.")
        print("Do you wish to continue?")
        x = input("Yes or No: " ).strip()
        if x == "No":
            y = input("\nWould you like to replay the instructions? ")
            if y is "Yes":
                print("\n")
                continue
            else:
                print("\n\n")
                break
        elif x == "Yes":
            print("\n\n")
            break
     
    return None

def getParams():
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    # Author: Kenji
    #Modifier: Catrina
    print("Shape Options: cone, cube, cylinder, retangular rism, pyramid, sphere, triangular prism")
    shape = input("Enter a shape: ").strip()
    if shape == "cone":
        return [1,"Enter the radius: ","Enter the height: "]
    elif shape == "pyramid":
        return [2,"Enter the length: ","Enter the width: ","Enter the height: "]
    elif shape == "cube":
        return [3,"Enter the side length: "]
    elif shape == "rectangular prism":
        return [4,"Enter the width: ","Enter the height: ","Enter the length: "]
    elif shape == "triangular prism":
        return [5,"Enter base side A: ","Enter base side B: ","Enter base side C: ","Enter the height: "]
    elif shape == "cylinder":
        return [6,"Enter the radius: ","Enter the height: "]
    else:
        return [0,"Invalid shape, try again"]

def getInputs(prompts):
    # Will prompt the user for inputs for the shape they want.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurments = []
    if prompts[0]==1:
        for x in range (3):
            measurments.append(int(input(prompts[x+1])))
            print("\n")
    elif  prompts[0]==2:
        for x in range (3):
            measurments[x+1] = int(input())
            print("\n")
    elif  prompts[0]==3:
        for x in range (1):
            measurments[x+1] = int(input())
            print("\n")
    elif  prompts[0]==4:
        for x in range (3):
            measurments[x+1] = int(input())
            print("\n")
    elif  prompts[0]==5:
        for x in range (4):
            measurments[x+1] = int(input())
            print("\n")
    elif  prompts[0]==6:
        for x in range (2):
            measurments[x+1] = int(input())
            print("\n")
    print(measurments)
    return measurments
    

def cube(s):
    return s**3

def Cylinder(r,h):
    return math.pi*(r**2)*h

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    getInputs(getParams())

main()
