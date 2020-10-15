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
    print("\n\n=================================")
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
        print("\nDo you wish to continue?")
        x = input("Yes or No: " ).strip()
        if x == "No" or x =="no":
            y = input("Would you like to replay the instructions? ").strip()
            if y == "Yes" or  y =="yes":
                continue
            elif y == "no" or y == "No":
                break
        elif x == "yes" or x =="Yes":
            break

                
                
    return None

def getParams():
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    # Author: Kenji
    print("\nPossible shapes: cone, pyramid, cube, rectangular prism, triangular prism, cylinder\nMake sure everything is spelled correctly!")
    shape = input("Enter a shape: ")
    if shape == "Cone" or "cone":
        return [1,"Enter the radius: ","Enter the height: "]
    elif shape == "Pyramid" or "pyramid":
        return [2,"Enter the length: ","Enter the width: ","Enter the height: "]
    elif shape == "Cube" or "cube":
        return [3,"Enter the side length: "]
    elif shape == "Rectangular Prism" or "retangular prism":
        return [4,"Enter the width: ","Enter the height: ","Enter the length: "]
    elif shape == "Triangular Prism" or "triangular prism":
        return [5,"Enter base side A: ","Enter base side B: ","Enter base side C: ","Enter the height: "]
    elif shape == "Cylinder" or "cylinder":
        return [6,"Enter the radius: ","Enter the height: "]
    else:
        return [0,"Invalid shape, try again"]

def getInputs(prompts):
    # Will prompt the user for inputs for the shape they want.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    #Author: Peter
    measurments = []
    if prompts[0]==1:
        for x in range (2):
            measurments.append(int(input(prompts[x+1])))
    elif  prompts[0]==2:
        for x in range (3):
           measurments.append(int(input(prompts[x+1])))
    elif  prompts[0]==3:
        for x in range (1):
           measurments.append(int(input(prompts[x+1])))
    elif  prompts[0]==4:
        for x in range (3):
            measurments.append(int(input(prompts[x+1])))
    elif  prompts[0]==5:
        for x in range (4):
           measurments.append(int(input(prompts[x+1])))
    elif  prompts[0]==6:
        for x in range (2):
           measurments.append(int(input(prompts[x+1])))
    return measurments

def calc(x,y):
    # Author: Peter
    if y[0]==1:
            return math.pi * (x[0]**2) * (x[1]/3)
    elif y[0]==2:
           return (x[0]* x[1]* x[2])/3
    elif y[0]==3:
           return x**3
    elif y[0]==4:
            return x[0]* x[1]* x[2]
    elif y[0]==5:
           (1/4*x[3])*math.sqrt((-x[0]**4)+2*(x[0]*x[1]))
    elif y[0]==6:
           return math.pi*(x[0]**2)*x[1]

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    #authors: Peter, Catrina, Kenji
    title()
    instructions()
    print(calc(getInputs(getParams()), getParams()))
main()