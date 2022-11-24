# Created By: Spencer Scarlett
# Created: Nov 12, 2022
# This is a program that generates the COS table from angles 0 to 360
 
import math
 
# Function
def cos_table():
    # To change the font and bold
    print("\33[1m")
 
    counter = 0
    # While true from 0 - 360
    while counter != 361:
 
        # To convert a number to COS value
        current = round(math.cos(counter), 4)
 
        # Displays outcome
        print(f"Cos value {counter} = {current}")
 
        # Too move on to the next number and repent the process
        counter = counter + 1
 
 
def main():
    # To call the above function to use
    cos_table()
 
 
if __name__ == "__main__":
    main()
 
