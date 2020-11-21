# main file that runs both phase1 and phase2
import sys
import phase1 as p1
import enterProgram as init_fun
from pymongo import MongoClient

def main():
    userinput = sys.argv[1]
    # make connection
    client = MongoClient("mongodb://localhost:"+ userinput +"/")
    # database
    db = client["291db"]

    p1.phase_one(userinput,db)
    
    init_fun(db)
    
    

if __name__ == 'main':
    main()
