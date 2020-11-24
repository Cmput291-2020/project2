import action_vote
import pprint

def list_answers(db,current_user,searched_pid):

    postCollection = db['Posts']

    answers = []
    thereisaccept = False
    question = postCollection.find_one({"Id": searched_pid})
    accepted_id = ""
    if "AcceptedAnswerId" in question  :
        accepted_id = str(question["AcceptedAnswerId"])
        thereisaccept = True

    for i in postCollection.find({"ParentId":searched_pid}):
        if str(i["Id"]) == accepted_id:
            accepted_post = i
        else:
            answers.append(i)

    if "AcceptedAnswerId" in question  :
        answers.insert(0, accepted_post)
    
    if len(answers) == 0:
        print("There are no answers yet!")
        return

    print("Here are the answers recevied:\n")
    # print body, creation date and the score
    for i in range(len(answers)):
        post = answers[i]

        if i == 0 and thereisaccept:
            print("* <1> answer *")
        else:
            print("<"+str(i+1)+"> answer")
            

        # print body
        print("Body: ",post["Body"][:80])

        # print creation date
        print("Creation Date: ",post["CreationDate"])
       
        # print the score
        print("Score:", post["Score"], "\n")

    
    a = int(input( '''
        -------- BACK TO MAIN --------- Press 0 ---------------------------------
        --- SELECT AN ANSWER YOU WOULD LIKE TO SEE THE FIELDS (BETWEEN 1 - '''+str(i+1)+''') ---
        '''))

    post = answers[i-1]

    if a == 0:
        return
    else:
        print("-----------")
        pprint.pprint(post)
        print("-----------")
    
    vote = input("Would you like to vote on this answer?(y/n): ")
    if vote.lower() == "y":
        pid_chosen = answers[a-1]["Id"]
        return action_vote.action_vote(db, current_user, pid_chosen)
    else: 
        print("Return to main...")
        return
    


        


