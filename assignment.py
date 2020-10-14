#!python3
# Volume Calculator
# Feel free to rename your variables

import os

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Catrina
    # Modified:
    print("\n\n=================================")
    print("Welcome to the Volume Calculator! \n=================================")
    print("\nThis program was created by the Poggers!")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Catrina
    # Modified:
    print("This program has been designed to calculate the volume of your desired shape.")
    print("To use this calculator, you will be directed to choose a shape. Then you will be prompted")
    print("to enter the necessary parameters for the shape. You will be asked to confirm your measurements.")
    print("Then the program will run and you will be given the area of your shape.")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()

intructions()