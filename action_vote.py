import datetime
import random

def action_vote(db, current_user, pid):
    votesCollection = db['Votes']

    vote_id = str(random.randint(9999999,99999999999))
    while votesCollection.find({"Id":vote_id}) == True:
        vote_id = str(random.randint(9999999,99999999999))


    current_time = datetime.datetime.utcnow()
    
    # if user has an id
    if current_user != None:
        votes_collect = votesCollection.find({"$and":[{"PostId":pid},{"UserId":current_user}]})
        votes = []
        for i in votes_collect:
            votes.append(i)

        if len(votes) > 0:
            print("You have already voted...")
            return
        else:
            answer = {
            "Id": vote_id,
            "PostId": pid,
            "VoteTypeId": "2",
            "UserId": current_user,
            "CreationDate": current_time
            }

            print("Inserting...")
            votesCollection.insert_one(answer)
            print("Voted successful")
    # if user has no uid
    else:
        answer = {
            "Id": vote_id,
            "PostId": pid,
            "VoteTypeId": "2",
            "CreationDate": current_time
        }

        print("Inserting...")
        votesCollection.insert_one(answer)
        print("Voted successful")



    
    