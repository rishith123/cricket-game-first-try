import random
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
game=1
check=[1,2]
runs=[0,1,2,3,4,5,6]
while(game==1):
    fp=open("High_score.txt","a")
    l=[]
    name=input("enter your name : ")
    print(Fore.RED + Back.GREEN + "")
    input("welcome press enter to continue:")
    to=int(input("press 1 for heads and 2 for tails\n:"))
    if(to not in check):
                while(to not in check):
                    to=0
                    print("you have not entered a number 1 or 2")
                    to=int(input("press again 1 for heads and 2 for tails\n:"))
    toss=random.randint(1,2)
    bat=random.randint(1,2)
    flag=0
    if(toss == 1):
        if(to==1):
            print("the result of the toss is heads you won")
            borb=int(input("press 1 to chose batting and 2 for bowling\n:"))
            if(borb not in check):
                while(borb not in check):
                    borb=0
                    print("you have not entered a number 1 or 2")
                    borb=int(input("press again 1 to chose batting and 2 for bowling\n:"))                    
            if(borb==1):
                flag=0
            else:
                flag=1
        else:
            print("the result of the toss is heads you lost")
            if(bat==1):
                print("computer chose to bat")
                flag=1
            else:
                print("computer chose to bowl")
                flag=0
    else:
        if(to==1):
            print("the result of the toss is tails you lost")
            if(bat==1):
                print("computer chose to bat")
                flag=1
            else:
                print("computer chose to bowl")
                flag=0
        else:
            print("the result of the toss is tails you won")
            borb=int(input("press 1 to chose batting and 2 for bowling\n:"))
            if(borb not in check):
                while(borb not in check):
                    borb=0
                    print("you have not entered a number 1 or 2")
                    borb=int(input("press again 1 to chose batting and 2 for bowling\n:"))                    
            if(borb==1):
                flag=0
            else:
                flag=1
    input("press enter to continue:\n")
    COMPUTERSCORE=0
    PLAYERSCORE=0
    if(flag==0):
        wicket=0
        playerturn=0
        computerturn=0
        total=0
        while(wicket==0):
            print(Fore.BLUE + Back.YELLOW+"YOU ARE NOW BATTING")
            playerturn=int(input("your turn press any number from 0 to 6 : "))
            if(playerturn not in runs):
                while(playerturn not in runs):
                    playerturn=0
                    print("you have not entered a number from 0 to 6")
                    playerturn=int(input("press any number from 0 to 6 again : "))
            computerturn=random.randint(0,6)
            n=playerturn
            if (playerturn==0):
                playerturn = computerturn

            if(n!=computerturn):
                print("you entered:",n)
                print("computer entered: ",computerturn)
                total=playerturn+total
                print("your score is : ",total)
                print("\n")
            else:
                print("YOU ARE OUT")
                print("you entered:",n)
                print("computer entered: ",computerturn)
                wicket=1
                PLAYERSCORE=total
                print("")
                print("your score is",total)
                print("computer needs ",total+1,"to win the match")
                print("\n")
                total=0
            computerturn =0
            playerturn=0
            n=0
        wicket=0
        while(wicket==0 or PLAYERSCORE<total):
            print(Fore.BLACK + Back.WHITE+"YOU ARE NOW BOWLING")
            playerturn=int(input("your turn press any number from 0 to 6 : "))
            if(playerturn not in runs):
                while(playerturn not in runs):
                    playerturn=0
                    print("you have not entered a number from 0 to 6")
                    playerturn=int(input("press any number from 0 to 6 again : "))
            computerturn=random.randint(0,6)
            n=computerturn
            if (computerturn==0):
                computerturn = playerturn

            if(n!=playerturn):
                print("you entered:",playerturn)
                print("computer entered: ",n)
                total=computerturn+total
                print("computer's score is : ",total)
                input("press enter to continue:")
                print("\n")
            else:
                print("COMPUTER IS OUT")
                print("you entered:",n)
                print("computer entered: ",computerturn)
                wicket=1
                COMPUTERSCORE=total
                total=0
                input("press enter to continue:")
                print("\n")
            computerturn =0
            playerturn=0
            n=0
    else:
        wicket=0
        playerturn=0
        computerturn=0
        total=0
        while(wicket==0):
            print(Fore.BLACK + Back.WHITE+"YOU ARE NOW BOWLING")
            playerturn=int(input("your turn press any number from 0 to 6 : "))
            if(playerturn not in runs):
                while(playerturn not in runs):
                    playerturn=0
                    print("you have not entered a number from 0 to 6")
                    playerturn=int(input("press any number from 0 to 6 again : "))
            computerturn=random.randint(0,6)
            n=computerturn
            if (computerturn==0):
                computerturn = playerturn

            if(n!=playerturn):
                print("you entered:",playerturn)
                print("computer entered: ",n)
                total=computerturn+total
                print("computer's score is : ",total)
                input("press enter to continue:")
                print("\n")
            else:
                print("COMPUTER IS OUT")
                print("you entered:",n)
                print("computer entered: ",computerturn)
                wicket=1
                COMPUTERSCORE=total
                print("")
                print("computer's score is",total)
                print("you need ",total+1,"to win the match")
                total=0
                input("press enter to continue:")
                print("\n")
            computerturn =0
            playerturn=0
            n=0
        wicket=0
        while(wicket==0 or COMPUTERSCORE<total):
            print(Fore.BLUE + Back.YELLOW+"YOU ARE NOW BATTING")
            playerturn=int(input("your turn press any number from 0 to 6 : "))
            if(playerturn not in runs):
                while(playerturn not in runs):
                    playerturn=0
                    print("you have not entered a number from 0 to 6")
                    playerturn=int(input("press any number from 0 to 6 again : "))
            computerturn=random.randint(0,6)
            n=playerturn
            if (playerturn==0):
                playerturn = computerturn

            if(n!=computerturn):
                print("you entered:",n)
                print("computer entered: ",computerturn)
                total=playerturn+total
                print("your score is : ",total)
                input("press enter to continue:")
                print("\n")
            else:
                print("YOU ARE OUT")
                print("you entered:",n)
                print("computer entered: ",computerturn)
                wicket=1
                PLAYERSCORE=total
                total=0
                input("press enter to continue:")
                print("\n")
            computerturn =0
            playerturn=0
            n=0
    input(Fore.WHITE + Back.BLACK + "press enter to know the result :\n")
    if(PLAYERSCORE<COMPUTERSCORE):
        print(Back.CYAN + "COMPUTER WON")
        l.append(name + " played one match and lost one match \n")
    elif(PLAYERSCORE==COMPUTERSCORE):
        print(Back.MAGENTA + "THE MATCH HAS TIED")
        l.append(name + " played one match and tied one match \n")
    else:
        print(Back.YELLOW + "YOU WON THE MATCH")
        l.append(name+" played one match and won one match one match \n")
    fp.writelines(l)
    fp.close
    game=0    
    game=int(input(Back.RESET + "enter 1 to play again 0 to stop playing and 2 to know more:"))    
    while(game==2):
        fp=open("High_score.txt")
        strl=fp.readlines()
        for str in strl :
            print(str)
            print('\n')
        game=int(input(Back.RESET + "enter 1 to play again 0 to stop playing and 2 to know more:"))        
input("press enter to exit")
