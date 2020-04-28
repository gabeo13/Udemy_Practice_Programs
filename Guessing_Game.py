# Import Random Mod
import random
# Generate Opening Credits
print("Hello and Welcome to the Guessing Game Challenge\n\nPresented by Gabriel H. Allen\n\nTry to guess the random number from 1 to 100 and win TACOS!!!")
# Generate Random Number
magic_number = random.randint(1,100)
# Generate guess list for total count
user_guess = [0]
# Compile while loop section for assesing validity of the guess
while True:
    user_input = int(input(" READY.SET.GO!\n Choose Wisely: "))
    
    if user_input < 1 or user_input > 100: 
        print("Party Foul! Try Again: ")
        continue
        
    if user_input == magic_number:
        print(f'HOLY CRAP, WE WON TACOS!!! it only took you {len(user_guess)} tries!!!')     
        break
# adder to guess list
    user_guess.append(user_input)
    
# this part confuses me, but it appears to brute force the end of the list for the boolean check for the very first guess
    if user_guess[-2]:
        if abs(magic_number - user_input) < abs(magic_number - user_guess[-2]):
            print('WARMER')
        else:
            print('COLDER')
# this completes the loop with the final "else"  statement          
    else:
        if abs(magic_number - user_input) <=10:
            print('WARM')
        else:
            print('COLD')
       
        
