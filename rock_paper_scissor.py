from random import randint
def comp_generator():
    comp_no = randint(1,3)
    if comp_no == 1:
        comp_move= 'r'
    elif comp_no == 2:
        comp_move = 'p'
    else:
        comp_move = 's'
    return comp_move

wins=0 
losses= 0 
ties = 0
print("-"*50)
print ("ROCK PAPER SCISSORS")
print("-"*50)
move = 'r'
while move!='q':
    comp_move = comp_generator()
    print()
    print("Wins =",wins,", Losses =",losses, ", ties =", ties)
    move = input("Enter your move (rock (r) , paper (p) , scissors (s) or quit (q)) = ").lower()
    if move == 'q':
        print ()
        print ("You have", wins,"wins,",losses,"losses, and",ties,"ties.")
        print("Thanks for playing:)")
        break
    if move =='r':
        print (" ROCK vs... ", end = '')
        if comp_move == 'r':
            print ("ROCK ! ")
            ties = ties + 1
            print ("It's a TIE.")
        elif comp_move == 'p':
            print("PAPER ! ")
            losses += 1
            print("You LOSE.")
        else:
            print ("SCISSORS ! ")
            wins+= 1
            print("You WIN.")
       
    elif move == 'p':
        print(" PAPER vs... ", end ='')
        if comp_move == 'r':
            print ("ROCK ! ")
            wins+= 1
            print("You WIN.")
        elif comp_move == 'p':
            print("PAPER ! ")
            ties += 1
            print ("It's a TIE.")
        else:
            print ("SCISSORS ! ")
            losses+= 1
            print("You LOSE.")
        
    elif move == "s":
        print("SCISSORS vs... ", end = '')
        if comp_move == 'r':
            print ("ROCK ! ")
            losses+= 1 
            print("You LOSE.")
        elif comp_move == 'p':
            print("PAPER ! ")
            wins += 1
            print("You WIN.")
        else:
            print ("SCISSORS ! ")
            ties+= 1
            print ("It's a TIE.")
    else:
        print ("Invalid answer:( Try again.")
        continue
   
