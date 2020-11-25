import datetime
import random
import pymongo

def answer_question(db,current_user,searched_pid):
    postCollection = db['Posts']

    body = input('Please enter your answer: \n')

    post_id = str(random.randint(100000000,99999999999))
    while postCollection.find({"Id":post_id}) == True:
        post_id = str(random.randint(100000000,99999999999))


    current_time = datetime.datetime.utcnow()

    answer = {
        "Id": post_id,
        "PostTypeId": "2",
        "ParentId": searched_pid,
        "CreationDate": current_time,
        "Score": 0,
        "Body": body,
        "OwnerUserId": current_user,
        "LastActivityDate": current_time,
        "CommentCount": 0,
        "ContentLicense": "CC BY-SA 2.5"
      }

    print("inserting...")
    postCollection.insert_one(answer)
    print("successful")
