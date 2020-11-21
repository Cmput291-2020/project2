#this function allow the user to post a question.

import datetime
import random

def post_question(db,current_user):
    user_collection = db["users"]
    title = input('Please enter a title of your question: \n')
    body = input('Please enter your question: \n')
    post_id = random.randint(1,9999)
    result = db.find({"Id":post_id})
    while result:
        post_id = random.randint(1,9999)
        result = db.find({"Id":post_id})


    question = [
        {
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
            "ContentLicense": "CC BY-SA 2.5"
        }
    ]
    
    user_collection.insert_one(question)



