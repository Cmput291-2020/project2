# phase 1, building a document store
"""
Phase 1: Building a document store
Write a program that reads the three json files (as named above) in the current directory and constructs a collection for each.
Your program will take as input a port number under which the MongoDB server is running, 
will connect to the server and will create a database named 291db (if it does not exist). 
Your program then will create three collections named Posts, Tags and Votes respectively for Posts.json, Tags.json and Votes.json. 
If those collections exist, your program should drop them and create new collections.
Your program for this phase ends after building these collections. 
As you may notice in the sample data, the fields of a record are not fixed and some records have more or less fields than others.

Groups of size 3 will need, as part of their program for Phase 1, 
to extract all terms of length 3 characters or more in title and body fields of Posts, 
add those terms as an array named terms to Posts collection, and build an index on those terms.
Assume a term is an alphanumeric character string, and that terms are separated by white spaces and/or punctuations. 
Also as part of their program for Part 2, they will need to use this index when searching the title and body fields in the next phase.
"""
import json
import ijson
from pymongo import MongoClient
import pymongo
import os.path


def strListMaker(str, currList):

    newStr = str.split(" ")

    for word in newStr:
        if(len(word) >= 3) and word not in currList:
            currList.append(word)
    return currList


#creating client connection
client = MongoClient("mongodb://localhost:27017/")
# database
db = client["PROJECT2"]


# file names
files_str_list = ["Posts", "Tags", "Votes"]


print("Inputting post data...")
# add posts
postCollection = db['Posts']
postCollection.drop()
with open('Posts.json', 'r') as f:
    objs = ijson.items(f, 'posts.row.item')
    cols = list(objs)
postCollection.insert_many(cols)


print("updating array")
# fields = postCollection.find({},{'_id':1, 'Title':1, 'Body': 1})


# theList = []
#
# for doc in postCollection.find({"Title": {'$exists': True}}):
#     theList = strListMaker(doc['Title'], theList)
#     postCollection.update_one({'_id':doc['_id']}, {"$set": {"terms": theList}})
#
# for doc in postCollection.find({"Body": {'$exists': True}}):
#     theList = strListMaker(doc['Body'], theList)
#     postCollection.update_one({'_id':doc['_id']}, {"$set": {"terms": theList}})





print("Inputting votes data...")
# add votes
voteCollection = db['Votes']
voteCollection.drop()
with open('Votes.json', 'r') as f:
    objs = ijson.items(f, 'votes.row.item')
    cols = list(objs)
voteCollection.insert_many(cols)


print("Inputting tags data...")
# add tags
tagCollection = db['Tags']
tagCollection.drop()
with open('Tags.json', 'r') as f:
    objs = ijson.items(f, 'tags.row.item')
    cols = list(objs)
tagCollection.insert_many(cols)


