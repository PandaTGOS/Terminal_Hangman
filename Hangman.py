import random as ran
import os
import time

fails=0
guesses=set()
L=[]
LG=[]

def PrintTitle():
    print(r''' .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ''')


def win():
    print(r''' __      __  ______   __    __        __       __  ______  __    __        __ 
/  \    /  |/      \ /  |  /  |      /  |  _  /  |/      |/  \  /  |      /  |
$$  \  /$$//$$$$$$  |$$ |  $$ |      $$ | / \ $$ |$$$$$$/ $$  \ $$ |      $$ |
 $$  \/$$/ $$ |  $$ |$$ |  $$ |      $$ |/$  \$$ |  $$ |  $$$  \$$ |      $$ |
  $$  $$/  $$ |  $$ |$$ |  $$ |      $$ /$$$  $$ |  $$ |  $$$$  $$ |      $$ |
   $$$$/   $$ |  $$ |$$ |  $$ |      $$ $$/$$ $$ |  $$ |  $$ $$ $$ |      $$/ 
    $$ |   $$ \__$$ |$$ \__$$ |      $$$$/  $$$$ | _$$ |_ $$ |$$$$ |       __ 
    $$ |   $$    $$/ $$    $$/       $$$/    $$$ |/ $$   |$$ | $$$ |      /  |
    $$/     $$$$$$/   $$$$$$/        $$/      $$/ $$$$$$/ $$/   $$/       $$/ ''')
    print()

def lose():
    print(r''' __      __  ______   __    __        __         ______    ______   ________ 
/  \    /  |/      \ /  |  /  |      /  |       /      \  /      \ /        |
$$  \  /$$//$$$$$$  |$$ |  $$ |      $$ |      /$$$$$$  |/$$$$$$  |$$$$$$$$/ 
 $$  \/$$/ $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |$$ \__$$/ $$ |__    
  $$  $$/  $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |$$      \ $$    |   
   $$$$/   $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ | $$$$$$  |$$$$$/    
    $$ |   $$ \__$$ |$$ \__$$ |      $$ |_____ $$ \__$$ |/  \__$$ |$$ |_____ 
    $$ |   $$    $$/ $$    $$/       $$       |$$    $$/ $$    $$/ $$       |
    $$/     $$$$$$/   $$$$$$/        $$$$$$$$/  $$$$$$/   $$$$$$/  $$$$$$$$/ ''')
    print()


def curstatus():               #Displays Current status of man
    global fails

    if fails==0:
        print("")

    elif fails==1:
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    
    elif fails==2:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")

    elif fails==3:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|        __    ")
        print("|       |  |   ")
        print("|        --    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")

    elif fails==4:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|        __    ")
        print("|       |  |   ")
        print("|        --    ")
        print("|         |    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")

    elif fails==5:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|        __    ")
        print("|       |  |   ")
        print("|      \ --    ")
        print("|       \ |    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")

    elif fails==6:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|        __    ")
        print("|       |  |   ")
        print("|      \ --  / ")
        print("|       \ | /  ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")

    elif fails==7:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|        __    ")
        print("|       |  |   ")
        print("|      \ --  / ")
        print("|       \ | /  ")
        print("|         |    ")
        print("|        /     ")
        print("|       /      ")
        print("|              ")
        print("|              ")

    elif fails==8:
        print("|---------     ")
        print("|              ")
        print("|              ")
        print("|        __    ")
        print("|       |  |   ")
        print("|      \ --  / ")
        print("|       \ | /  ")
        print("|         |    ")
        print("|        / \   ")
        print("|       /   \  ")
        print("|              ")
        print("|              ")

    elif fails==9:
        print("|---------     ")
        print("|        |     ")
        print("|        |     ")
        print("|        __    ")
        print("|       |  |   ")
        print("|      \ --  / ")
        print("|       \ | /  ")
        print("|         |    ")
        print("|        / \   ")
        print("|       /   \  ")
        print("|              ")
        print("|              ")
        print("\nLAST CHANCE !!!")
    
    elif fails==10:
        print("|---------     ")
        print("|        |     ")
        print("|        |     ")
        print("|        __    ")
        print("|       |  |   ")
        print("|      \ --  / ")
        print("|       \ | /  ")
        print("|         |    ")
        print("|        / \   ")
        print("|       /   \  ")
        print("|              ")
        print("|              ")


def wordstatus():
    global LG
    for i in LG:
        print(i,end="")
    print()


def main():
    global fails
    global guesses
    global L
    global LG

    PrintTitle()

    answer=""
    with open('words.txt', 'r') as fh:     #Getting a word
        data = fh.readlines()
        answer = ran.choice(data)
        answer=answer.upper()

    L = list(answer)
    L.pop()                     #Removes "\n" from list
    for i in L:
        LG.append(' _ ')
    print()


    print("Looking for a nice word...")                       #Just For Show
    time.sleep(2)
    input("GOT THE WORD ! PRESS ENTER TO START !")

    while True:
        os.system('cls')
        PrintTitle()
        curstatus()
        print()
        print("Guesses =",guesses)
        print()
        wordstatus()
        print()


        if fails==10:                                         #CHECKING IF GAME SHOULD GO ON OR NOT
            lose()
            print("GAME OVER")
            print("YOU KILLED AN INNOCENT MAN !\n")
            print("THE WORD WAS :")
            for i in L:
                print(i,end="")
            break

        elif ' _ ' in LG:
            print()
        else:
            win()
            print("YOU GOT THE WORD !")
            print("THE WORD IS:-")
            wordstatus()
            break


        letter=input("ENTER GUESS LETTER: ")                 #Asking for Guess letter if game's still going on
        letter=letter.upper()

        if len(letter)==1:                                   #Checking if only one letter is entered
            counter=0
            for i in range(len(L)):
                if letter==L[i] and letter not in guesses:   #Checking for multiple occurances of letter
                    LG.pop(i)
                    LG.insert(i, letter)
                    counter+=1                               #Increases if letter guesses is correct

            if counter==0:
                print("WRONG GUESS !")                       #Checking for wrong guess
                fails+=1

            guesses.add(letter)

        else:
            print("Invalid Input ! Enter Only 1 Letter !")
            time.sleep(2)
            continue


#__main__
os.system('cls')
main()