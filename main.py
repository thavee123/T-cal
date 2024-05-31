def mainbanner():
    print ("'\033[1;33m'    ████████╗    ██████╗ █████╗ ██╗     ")
    print ("'\033[1;33m'    ╚══██╔══╝   ██╔════╝██╔══██╗██║     ")
    print ("'\033[1;33m'       ██║█████╗██║     ███████║██║     ")
    print ("'\033[1;33m'       ██║╚════╝██║     ██╔══██║██║     ")
    print ("'\033[1;33m'       ██║      ╚██████╗██║  ██║███████╗")
    print ("'\033[1;33m'       ╚═╝       ╚═════╝╚═╝  ╚═╝╚══════╝")
    print()
    print ("'\033[1;32m'                 Created by Thavee ")
    print()          

def main():
    x=print ("'\033[1;32m'[1]Plus") 
    y=print ("'\033[1;32m'[2]Minus")
    z=print ("'\033[1;32m'[3]Multiply")
    l=print ("'\033[1;32m'[4]Divide")   
       
def second ():
    choice=int(input("'\033[1;32m'ENTER YOUR CHOISE :"))

    print ()
    print ()

    fist=int(input('ENTER FIST NUMBER :'))
    second=int(input("ENTER SECOND NUMBER :"))
    print ()

    print ("'\033[1;32m'Loading.............")

    print ()

    if choice==1:
        print (fist+second)
    elif choice==2:
        print (fist-second)
    elif choice==3:
        print (fist*second)
    elif choice==4:
        print (fist/second)
    else:
        print (ERROR)
      

mainbanner ()

print ()
print ()

main ()

print ()

second ()

print ()

print ("DONE")

print ()
