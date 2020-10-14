#!python3
# Volume Calculator
# Feel free to rename your variables


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
    print("This program has been designed to calculate the volume of your desired shape.")
    print("To use this calculator you will:")
    print("Step 1: You will choose a shape.")
    print("Step 2: You will be prompted to enter the necessary parameters for the shape. ")
    print("Step 3: You will be asked to confirm your measurements.")
    print("Step 4: The program will run and you will be given the area of your shape.")
    x = input("Do you wish to continue? Yes or No").strip()
        if x == "Yes" or x == "yes":
            continue
        if x = "No" or x == "no":
            y = input("Would you like to replay the instructions?")
            if y == "No" or "no":
                continue
            else:
                
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
    instructions()
main()
