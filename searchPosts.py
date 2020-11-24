from pprint import pprint
import action_vote
import action_listAnswers
import action_answerQuestion

def id_match(id, listofIDs):
    for i in listofIDs:
        if id == str(i):
            return True
    return False

def display_post(post):
    print("ID: ", post['Id'])
    print("Title: ", post['Title'])
    print("Creation Date: ", post['CreationDate'])
    print("Score: ", post['Score'])
    print("Answer Count: ", post['AnswerCount'])
    print('---------------------------------------------')

def searchPosts(db, user):

    postCollection = db['Posts']
    questionPosts = postCollection.find({'PostTypeId': "1"})
    found = []
    viewCount = None

    keyword_choice = input("Enter in space separated keywords: ")
    keywords = keyword_choice.split(" ")



    for word in keywords:
        for post in questionPosts:
            title = post['Title']
            body = post['Body']
            if 'Tags' in post:
                tags = post['Tags']
                if (word in title or word in body or word in tags):
                    found.append(post['Id'])
                    display_post(post)
            else: 
                if (word in title or word in body):
                    found.append(post['Id'])
                    display_post(post)
    if found == []:
        print("No results found")
        return

    id_choice = input("Select a post by ID: ")

    #checking if valid selection, if not goes back to main menu
    boolValidId = id_match(id_choice, found)
    if not boolValidId:
        print("Invalid choice")
        return

    #adding one to the view count
    temp = postCollection.find_one({'Id': id_choice})
    viewCount = int(temp['ViewCount'])
    viewCount += 1
    viewCount = str(viewCount)
    postCollection.update({'Id':id_choice}, {'$set': {'ViewCount':viewCount}})

    #printing all fields
    print("-------------------------------------------------")
    print("You selected ID: ", id_choice)
    pprint(temp)
    print("-------------------------------------------------")

    # action options
    print("(1) Answer Question")
    print("(2) List Answers")
    print("(3) Vote")
    action_input = input("Please select a choice: ")

    #Put part 3,4,5 here
    if action_input == '1':
        action_answerQuestion.answer_question(db,user,id_choice)
    elif action_input == '2':
        action_listAnswers.list_answers(db,user,id_choice)
    elif action_input == '3':
        action_vote.action_vote(db,user,id_choice)
    else:
        print("Invalid enrtry")
        return








