# main file that runs phase2
import sys
#import phase1 as p1
import enterProgram
import action_postQuestion
import searchPosts
from pymongo import MongoClient

def main():
    userinput = sys.argv[1]
    # make connection
    client = MongoClient("mongodb://localhost:"+ userinput +"/")

    # database
    db = client["291db"]

    #p1.phase_one(db,userinput) #phase 1 reads the json files

    current_user = enterProgram.init_function(db) #init_fun create and return user
    while current_user == False:
        current_user = enterProgram.init_function(db)

    while True:
        display_page = '''
        ---------Exit-------------------Press 0---------
        ---------Post Question----------Press 1---------
        ---------Search Question--------Press 2---------
        '''

        user_choice = input(display_page)
        if user_choice == '1':
            #user can post question
            action_postQuestion.post_question(db,current_user)

        elif user_choice == '2':
            searchPosts.searchPosts(db, current_user)

        elif user_choice =="0":
            print('Goodbye')
            sys.exit()
            
        
        #elif 
            
    
        else:
            print('Invalide input. Please try again.')


    

    
    

if __name__ == '__main__':
    main()
