#this function allow the user to post a question.

import datetime
import random
import pymongo

def post_question(db,current_user):

    postCollection = db['Posts']
    tagCollection = db['Tags']

    title = input('Please enter a title of your question: \n')
    tags = input("Please enter some tags for your post(seprate by space):\n")
    tags_list = tags.split()
    body = input('Please enter your question: \n')


    post_id = random.randint(400728,999999)
    while postCollection.find({"Id":post_id}) == True:
        post_id = random.randint(400728,999999)
    
    for tag in tags_list:
        if len(list(tagCollection.find({"TagName":tag}))) != 0:
            tag_result = list(tagCollection.find({"TagName":tag}))[0]
            tag_count = tag_result['Count']
            
            tag_count += 1
            tagCollection.update_one({"TagName":tag},{ "$set": { "Count": tag_count } } )


        else:
            tag_id = random.randint(5063,9999)
            while tagCollection.find({"Id":tag_id}) == True:
                tag_id = random.randint(5063,9999)

            tagCollection.insert_one(
                {
                "Id": tag_id,
                "TagName": tag,
                "Count": 1})



    print("Posting...")
    if current_user == None:
        question ={
            "Id": post_id,
            "Title":title,
            "Body":body,
            #"OwnerUserId":current_user,
            "CreationDate": datetime.datetime.utcnow(),
            "PostTypeId": "1",
            "Score": 0,
            "ViewCount": 0,
            "AnswerCount": 0,
            "CommentCount": 0,
            "FavoriteCount": 0,
            "ContentLicense": "CC BY-SA 2.5"}
    else:
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
    print("Success!")



