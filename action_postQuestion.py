#this function allow the user to post a question.

import datetime
import random

def post_question(db,current_user):
    user_collection = db["users"]
    postCollection = db['Posts']

    title = input('Please enter a title of your question: \n')
    body = input('Please enter your question: \n')
    post_id = random.randint(400728,999999)
    if postCollection.find({"Id":post_id}):
        post_id = random.randint(400728,999999)
    

    print("inserting")

    question ={
            "Id": post_id,
            "Title":title,
            "Body":body,
            "OwnerUserId":current_user,
            "CreationDate": datetime.datetime.utcnow(),
            "PostTypeId": "1",
            "Score": 0,
            "ViewCount": 0,
            "AnswerCount": 0,
            "CommentCount": 0,
            "FavoriteCount": 0,
            "ContentLicense": "CC BY-SA 2.5"}

    
    postCollection.insert_one(question)
    print("successful")



