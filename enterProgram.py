# this file includes
# user select ID option
# user don't select ID option
# if user select ID, display 
# (1) the number of questions owned and the average score for those questions, 
# (2) the number of answers owned and the average score for those answers, 
# (3) the number of votes registered for the user.
import random

def init_function(db):
    user_collection = db["users"]
    running = True
    while running:
        user_id_choice = input("Would you like to select an ID?(y/n): ")
        if(user_id_choice == "y" or user_id_choice=="Y"):
            user_id = input("Please enter your ID number: ")
            results = user_collection.find({"_id":user_id})

            if (not results):
                user = {"_id":user_id}
                user_collection.insert_one(user)
            else:
                for result in results:
                    print(result)
            break
        
        
        elif(user_id_choice == "n" or user_id_choice=="N"):
            user_id = random.randint(1,9999)
            user = {"_id":user_id}
            user_collection.insert_one(user)    
            break

        else:
            print("Invalid input, please try again: ")
    return user_id
        