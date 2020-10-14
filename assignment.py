#!python3
# Volume Calculator
# Feel free to rename your variables

import os

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
    if shape == cone:
        return [1,"Enter the radius","Enter the height"]
    elif shape == pyramid:
        return [2,"Enter the length","Enter the width","Enter the height"]
    elif shape == cube:
        return [3,"Enter the side length"]
    elif shape == rectangularPrism:
        return [4,"Enter the width","Enter the height","Enter the length"]
    elif shape == triangularPrism:
        return [5,"Enter base side A","Enter base side B","Enter base side C","Enter the height"]
    elif shape == cylinder:
        return [6,"Enter the radius","Enter the height"]
    else:
        return [0,"Invalid shape, try again"]

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
    instructions()

main()