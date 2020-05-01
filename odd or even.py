import random
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

game=1
check=[1,2]
runs=[0,1,2,3,4,5,6]

while(game==1):#till the player wants to play                              

    print(Fore.BLACK + Back.BLUE + "")
    name=input("enter your name : ")#take the player's name
    print(Fore.RED + Back.GREEN + "")
    input("welcome press enter to continue:")
    to=int(input("press 1 for heads and 2 for tails\n:"))#for toss player's chocie assigned to "to"

    if(to not in check):#if player enters invalid number

                while(to not in check):#till the player enters the right number

                    to=0
                    print("you have not entered a number 1 or 2")#error massage
                    to=int(input("press again 1 for heads and 2 for tails\n:"))

    toss=random.randint(1,2)#to randomly genrate the output of the toss
    bat=random.randint(1,2)#to randomly choose batting or balling for the computer
    flag=0#if the player will bat or ball

    if(toss == 1):#if the result of the toss is heads

        if(to==1):#if the player has chosen heads

            print("the result of the toss is heads you won")
            borb=int(input("press 1 to chose batting and 2 for bowling\n:"))#batting or bowling choice of the player assigned to borb

            if(borb not in check):#if the player enters invalid number

                while(borb not in check):#till the player enters a valid number

                    borb=0
                    print("you have not entered a number 1 or 2")#error message
                    borb=int(input("press again 1 to chose batting and 2 for bowling\n:"))                    

            if(borb==1):#if the choice of the player is batting

                flag=0#player will bat first

            else:

                flag=1#else player will bowl first as per his choice

        else:#if the player has chosen tails

            print("the result of the toss is heads you lost")

            if(bat==1):#if the coice of the computer is to bat

                print("computer chose to bat")
                flag=1#the player will bowl

            else:#if the choice of the computer is to ball

                print("computer chose to bowl")
                flag=0#the player will bat

    else:#if the result of the toss is tails

        if(to==1):#if the player has chosen heads

            print("the result of the toss is tails you lost")

            if(bat==1):#if the choice of the computer is to bat

                print("computer chose to bat")
                flag=1#the player will bowl

            else:#if the choice of the computer is to bowl

                print("computer chose to bowl")
                flag=0#the player will bat

        else:#if the player has chosen tails 

            print("the result of the toss is tails you won")
            borb=int(input("press 1 to chose batting and 2 for bowling\n:"))#batting or bowling choice of the player assigned to borb

            if(borb not in check):#if the player enters an invalid number

                while(borb not in check):#till the player enters a valid number

                    borb=0
                    print("you have not entered a number 1 or 2")#error massage
                    borb=int(input("press again 1 to chose batting and 2 for bowling\n:"))                    

            if(borb==1):#if the player has chosen to bat

                flag=0#player will bat

            else:

                flag=1#else player will bowl

    input("press enter to continue:\n")
    COMPUTERSCORE=0#initial scores of player and the computer is zero
    PLAYERSCORE=0

    if(flag==0):#if the player will bat

        wicket=0#initially the wicket is zero
        playerturn=0#players entry is zero
        computerturn=0#computers generated number 
        total=0#score of the batsman

        while(wicket==0):#till the wicket is taken

            print(Fore.BLUE + Back.YELLOW+"YOU ARE NOW BATTING")
            playerturn=int(input("your turn press any number from 0 to 6 : "))#player's entry

            if(playerturn not in runs):#if the player enters invalid number

                while(playerturn not in runs):#till the player enters a valid number

                    playerturn=0
                    print("you have not entered a number from 0 to 6")#error message
                    playerturn=int(input("press any number from 0 to 6 again : "))

            computerturn=random.randint(0,6)#computer's genrated number
            n=playerturn#assign player's entry to a temporary variable n

            if (playerturn==0):#if the player has played a defance

                playerturn = computerturn#player's turn becomes computer turn

            if(n!=computerturn):#if the players number and the computer's number is not same

                print("you entered:",n)
                print("computer entered: ",computerturn)
                total=playerturn+total#the player's score is updated
                print("your score is : ",total)#display player's score
                print("\n")

            else:#if the computer's number and the player's number is the same

                print("YOU ARE OUT")
                print("you entered:",n)
                print("computer entered: ",computerturn)
                wicket=1#wicket is updated
                PLAYERSCORE=total#player's total score is upgraded
                print("")
                print("your score is",total)
                print("computer needs ",total+1,"to win the match")#display the target
                print("\n")
                total=0#reset total

            computerturn =0#reset computer's genrated number
            playerturn=0#reset player's enterd number
            n=0#reset temporary variable

        wicket=0#reset the wicket

        while(wicket==0 and PLAYERSCORE>=total):#till the wicket is taken or the total of the computer is more than the target

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

    else:#if the player will bowl first

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

        while(wicket==0 and COMPUTERSCORE>=total):

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

    f= open("score.txt","r")# to read the previously existing data
    temp=f.read().split(",")
    f.close()

    point=0#mark to put if the player has any prior info
    mplayed=mwin=mloss=mtie=0#matches played won lost and tied initially taken zero

    if name in temp:#if the player already has prior data

             point=temp.index(name)

             mplayed=temp[point+1]#existing data updated to the variables
             mwin=temp[point+2]
             mloss=temp[point+3]
             mtie=temp[point+4]
             
             mplayed=int(mplayed)             
             mwin=int(mwin)
             mloss=int(mloss)
             mtie=int(mtie)

             del temp[point]
             del temp[point+1]
             del temp[point+2]

    print("\n")
    print(Fore.WHITE + Back.BLACK)
    input("press enter to know the result :\n")

    if(PLAYERSCORE<COMPUTERSCORE):#if the computer has won

        print(Back.CYAN) 
        print("COMPUTER WON")
        mplayed+=1#update the players data
        mwin+=0
        mloss+=1
        mtie+=0

    elif(PLAYERSCORE==COMPUTERSCORE):#if the match has tied

        print(Back.CYAN)
        print("THE MATCH HAS TIED")
        mplayed+=1#update the players data
        mwin+=0
        mloss+=0
        mtie+=1

    else:#if the player has won 

        print(Back.CYAN)
        print("YOU WON THE MATCH")
        mplayed+=1#update player's info
        mwin+=1
        mloss+=0
        mtie+=0

    mplayed=str(mplayed)#convert the variables back to string to update into the file
    mwin=str(mwin)
    mloss=str(mloss)
    mtie=str(mtie)

    f= open("score.txt","a+")#updating the player's info into the file
    sample= name+","+mplayed+","+mwin+","+mloss+","+mtie+",\n"
    f.writelines(sample)
    f.close    

    game=0
    print("\n")
    print(Back.BLACK)
    game=int(input("enter 1 to play again 0 to stop playing and 2 to know high scores:"))#to know what the player wants to do next    

    while(game==2):#if the player has selected to know the high scores

        print("\n")
        f= open("score.txt","r")
        l=f.read().split("\n")
        f.close

        for dis in l:

                     print(dis)

        print("\n")   
        input("press enter to continue:")
        print("\n")
        print(Back.BLACK)
        game=int(input("enter 1 to play again 0 to stop playing and 2 to know more:"))        
        print("\n")
input("press enter to exit:")
