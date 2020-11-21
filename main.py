# main file that runs both phase1 and phase2
import sys
import phase1 as p1

def main():
    userinput = sys.argv[1]
    p1.phase_one(userinput)
    
    

if __name__ == 'main':
    main()
