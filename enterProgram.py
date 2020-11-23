# this file includes
# user select ID option
# user don't select ID option
# if user select ID, display 
# (1) the number of questions owned and the average score for those questions, 
# (2) the number of answers owned and the average score for those answers, 
# (3) the number of votes registered for the user.
import random

def average(total,results):
    if len(results) == 0:
        return 0
    else:
        return round(total//len(results),2)
    
def init_function(db):
    user_collection = db["users"]
    postCollection = db["Posts"]

    user_id_choice = input("Would you like to select an ID?(y/n): ")
    if(user_id_choice == "y" or user_id_choice=="Y"):
        user_id = input("Please enter your ID number: ")
        results = list(postCollection.find({"OwnerUserId":user_id},{"Id":1,"Title":1,
        "Score":1}))

        total_score = 0
        for i in range(len(results)):
            total_score += results[i]["Score"]
        
        avg_score = average(total_score,results)
            
        if (not results):
            user = {"_id":user_id}
            user_collection.insert_one(user)
        else:
            print("Questions:")
            for result in results:
                print("Post Id: " + str(result["Id"]))
                print("Post Title: " + result["Title"]+"\n")
            print("Average score of your question posts are: " + str(avg_score))
                
        
        
    elif(user_id_choice == "n" or user_id_choice=="N"):
        user_id = random.randint(1,9999)
        user = {"_id":user_id}
        user_collection.insert_one(user)    
        

    else:
        print("Invalid input, please try again: ")
    return user_id
        