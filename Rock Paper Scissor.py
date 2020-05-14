#there we import the randon module
import random

#make list of your choice
List=['rock','paper','scissor']
check=1

#declaration of the player score initially
score1=0

#declaration of the computer score
score2=0


#looping under user valid input
while(check!=2):
    #computer choose randomly any choice
    a=random.choice(List)


    #take the input from user
    b=input("enter your choice :-(rock,paper, scissor)")
    print("computer choice",a)



    if b not in list:
            print("invalid choice, try again")


    elif(a==b):
        print("this match is tie...try again")
    elif(a=='rock'and b=='paper'):
        print("you won")
        score1+=1
    elif(a=='rock'and b=='scissor'):
        print("computer won")
        score2+=1
    elif(a=='paper'and b=='rock')   :
        print("computer won")
        score2+=1
    elif(a=='paper'and b=='scissor'):
        print("you won")
        score1+=1        
    elif(a=='scissor'and b=='rock'):
        print("you won")
        score1+=1
    elif(a=='scissor'and b=='rock'):
        print("computer won")
        score2+=1


    #give the user choice    
    print("choose:\n1)play again  \n2)exit\n")
    choose=int(input("your turn"))
#if the choose exit then total the score of both user and computer
print("your score is:",score1)
print("computer score is:",score2)


#after coming out of the while loop
print("Thanks for playing")






















        
