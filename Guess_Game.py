storage = "mr emmanuel"

x = 1
trials = 5

print("``````````````````````````````````````")
print("[WELCOME TO JUMANJI WORD GAME]")
print("``````````````````````````````````````")
print("1. CLICK START!")
print("2. EXIT.")

decision =  int(input())

for x in range(1,6):
        try:
                
                if decision == 1:
                        print("```````````````````````````````````````````````````````````")
                        
                        print("HINT! {The HOD Of Software Engineering Department} {Guess should be in lowercase} ")
                        
                        
                        print("```````````````````````````````````````````````````````````")
                        
                        guess = str(input("MAKE A GUESS: "))    
                
                        if guess == storage:
                                
                                print("```````````````````````````````````````````````````````````")
                                
                                print("You Guessed Correctly")
                                break
                                
                                print("```````````````````````````````````````````````````````````")
                        
                        elif guess != storage:
                                
                                print("```````````````````````````````````````````````````````````")
                                
                                print("You Guessed Wrongly")
                                trials = trials - 1
                                print(f"You have {trials} number of guesses left")
                                
                                print("```````````````````````````````````````````````````````````")
                
                elif decision == 2:
                        break
                
        except ValueError:
                print("```````````````````````````````````````````````````````````")
                print("Wrong input, try again")
                trials = trials - 1    
                print(f"You have {trials} guess left")
                print("```````````````````````````````````````````````````````````")
               
                
                            
        
if trials == 0:
        print("You Have Ran Out Of Guesses")
        print("GAME OVER!")
    
    




