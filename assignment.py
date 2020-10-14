#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(prompts):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    if prompts[0]==1:
        for x in range (3):
            measurments[x+1] = int(input())
            print("   ")
    elif  prompts[0]==2:
        for x in range (3):
            measurments[x+1] = int(input())
            print("   ")
    elif  prompts[0]==3:
        for x in range (1):
            measurments[x+1] = int(input())
            print("   ")
    elif  prompts[0]==4:
        for x in range (3):
            measurments[x+1] = int(input())
            print("   ")
    elif  prompts[0]==5:
        for x in range (4):
            measurments[x+1] = int(input())
            print("   ")
    elif  prompts[0]==6:
        for x in range (2):
            measurments[x+1] = int(input())
            print("   ")
            

    measurements
    
    return measurements
def cube(s):
    return s**3
def Cylinder(r,h):
    return math.pi*(r**2)*h
def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()

main()
