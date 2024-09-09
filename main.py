import sys
from src.help import displayHelp
from src.process import processStart

def main () :
    if len(sys.argv) > 1 :
        if "-h" in sys.argv or "--h" in sys.argv or "--help" in sys.argv:
            displayHelp()
        elif "-x" in sys.argv :
            processStart()
    else :
        displayHelp()
        sys.exit()

if __name__=="__main__":
    main()