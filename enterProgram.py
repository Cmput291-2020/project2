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
        return round(total/len(results),2)


def handle_input():

    user_id = input("please enter number: ")
    while not user_id.isdigit():
        user_id = input("invalid input, please enter number: ")
    return user_id


def display_answer(postCollection,user_id):
    answer_results = list(postCollection.find({"OwnerUserId":user_id,"PostTypeId":"2"}))
    answer_num = len(answer_results)
    print("\nNumber of answers: "+str(answer_num))
    total_score = 0
    for i in range(len(answer_results)):
        total_score += answer_results[i]["Score"]
        
    avg_score = average(total_score,answer_results)

    print("Average score of answers: " + str(avg_score))


def display_question(postCollection,user_id):
    question_results = list(postCollection.find({"OwnerUserId":user_id,"PostTypeId":"1"}))
    question_num = len(question_results)
    print("\nNumber of questions: "+str(question_num))
    total_score = 0
    for i in range(len(question_results)):
        total_score += question_results[i]["Score"]
        
    avg_score = average(total_score,question_results)

    print("Average score of questions: " + str(avg_score))


def display_votes(voteCollection,user_id):
    votes = voteCollection.count_documents({"UserId":user_id})

    print("\nVotes registered: " + str(votes))



def init_function(db):
    postCollection = db["Posts"]
    voteCollection = db['Votes']

    user_id_choice = input("Would you like to select an ID?(y/n): ")
    while user_id_choice not in "yYnN":
        user_id_choice = input("Invalid input, please try again: ")
    
    if(user_id_choice == "y" or user_id_choice=="Y"):
        user_id = handle_input()
        result = list(postCollection.find({"OwnerUserId":user_id}))
        if (len(result)==0):
            print("rejected")
            return False

        else:
            display_question(postCollection,user_id)
            display_answer(postCollection,user_id)
            display_votes(voteCollection,user_id)
        return user_id
                
        
        
    else:
        return None


        