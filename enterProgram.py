# this file includes
# user select ID option
# user don't select ID option
# if user select ID, display 
# (1) the number of questions owned and the average score for those questions, 
# (2) the number of answers owned and the average score for those answers, 
# (3) the number of votes registered for the user.
import random

def enter():

    user_id_choice = input("Would you like to select an ID?(y/n): ")

    if(user_id_choice == "y" or user_id_choice=="Y"):
	    user_id = input("Please enter your ID number: ")
    elif(user_id_choice == "n" or user_id_choice=="N"):
	    user_id = random.randint(1,1000)

