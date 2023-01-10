import random

def random_num_generator(range_amount):
    number = random.randint(0,range_amount)
    return number
    
def easy(lives):
    obj_number = random_num_generator(10)
    while lives != 0 :
        print(f"You got {lives} guesses.")
        try:
            guess = int(input("Guess the number: ")) #expect value error here
            if guess == obj_number:
                return True
            if guess < obj_number:
                print("Your guess is too short!")
            if guess > obj_number:
                print("Your guess is too big!")
            lives -= 1
        except:
            print("Please enter an actual number.")
    if lives == 0:
        print(f"The number you failed to guess was: {obj_number}")
        return False

def mid(lives):
    obj_number = random_num_generator(50)
    while lives != 0 :
        print(f"You got {lives} guesses.")
        try:
            guess = int(input("Guess the number: ")) #expect value error here
            if guess == obj_number:
                return True
            if guess < obj_number:
                print("Your guess is too short!")
            if guess > obj_number:
                print("Your guess is too big!")
            lives -= 1
        except:
            print("Please enter an actual number.")
    if lives == 0:
        print(f"The number you failed to guess was: {obj_number}")
        return False

def hard(lives):
    obj_number = random_num_generator(100)
    while lives != 0 :
        print(f"You got {lives} guesses.")
        try:
            guess = int(input("Guess the number: ")) #expect value error here
            if guess == obj_number:
                return True
            if guess < obj_number:
                print("Your guess is too short!")
            if guess > obj_number:
                print("Your guess is too big!")
            lives -= 1
        except:
            print("Please enter an actual number.")
    if lives == 0:
        print(f"The number you failed to guess was: {obj_number}")
        return False

def impossible(lives):
    obj_number = random_num_generator(100)
    while lives != 0 :
        print(f"You got {lives} guesses.")
        try:
            guess = int(input("Guess the number: ")) #expect value error here
            if guess == obj_number:
                return True
            if guess < obj_number:
                print("Your guess is too short!")
            if guess > obj_number:
                print("Your guess is too big!")
            lives -= 1
        except:
            print("Please enter an actual number.")
    if lives == 0:
        print(f"The number you failed to guess was: {obj_number}")
        return False

if __name__ == "__main__":
    i = 0
    print("Welcome to the number generator game!")
    while i < 1:
        difficulty = input("Please enter difficulty ('e': easy, 'm': medium, 'h': hard, 'i': impossible): ") #expect logic error here
        if difficulty in ['e','m','h','i']:
            if difficulty == 'e':
                result = easy(7)
                if result == True:
                    print("You got it!")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: #caught stupid here
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0     
                else:
                    print("You ran out of guesses before you got the answer. What a shame.")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: 
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0
            if difficulty == 'm':
                result = mid(10)
                if result == True:
                    print("You got it!")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: #caught stupid here
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0     
                else:
                    print("You ran out of guesses before you got the answer. What a shame.")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: 
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0
            if difficulty == 'h':
                result = hard(5)
                if result == True:
                    print("You got it!")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: #caught stupid here
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0     
                else:
                    print("You ran out of guesses before you got the answer. What a shame.")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: 
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0
            if difficulty == 'i':
                result = hard(1)
                if result == True:
                    print("You got it!")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: #caught stupid here
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0     
                else:
                    print("You ran out of guesses before you got the answer. What a shame.")
                    again = input("Would you like to try again? (Y/N): ").lower() #expect users being stupid
                    if again in ['y','n']: 
                        if again == 'n':
                            print("Goodbye and gg.")   
                            i = 1
                        else:
                            i = 0
        else:
            print("That was not one of the choices.")
