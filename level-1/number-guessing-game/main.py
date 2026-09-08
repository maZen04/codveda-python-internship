import random

difficulty = {
    "easy" : 10,
    "intermediate" : 8,
    "hard" : 6,
    "impossible" : 4
}

min_number, max_number = 1, 100


# user choose the difficulty to define the number of trials (lives).
def choose_difficulty(difficulty):
    choice = input("Choose your difficulty(choose from 1 to 4): \n1-easy\n2-intermediate\n3-hard\n4-impossible\n")

    match choice:
        case "1":
            return difficulty["easy"]
        case "2":
            return difficulty["intermediate"]
        case "3":
            return difficulty["hard"]
        case "4":
            return difficulty["impossible"]
    


def generate_random_number(min_number, max_number):
    return random.randint(min_number, max_number)

def user_guess():
    return input("Your guess is ")

def feedback(random_number, guessed_number):
    if guessed_number < random_number:
        return "Too low"
    elif guessed_number > random_number:
        return "Too High"
    else:
        return "Right Guessed."



def number_guessing_game():

    state = True
    # new session
    while state:
        # new game
        remaining_attempts = 0
        
        while remaining_attempts not in set(difficulty.values()):
            remaining_attempts = choose_difficulty(difficulty)
        
        random_number = generate_random_number(min_number, max_number)

        while remaining_attempts>0:
            print(f"Remaining attempts: {remaining_attempts}")
            while True:
                try:
                    guessed_number = int(user_guess())
                    if 1<=guessed_number<=100:
                        break
                    print("the guessed number should be greater than or equal 1 and smaller than or equal 100.")
                except ValueError:
                    print("the guessed number should be a number silly ^_^ !")
            
            remaining_attempts -= 1
            result = feedback(random_number=random_number,guessed_number=guessed_number)
            print(result)

            if (result == "Right Guessed."):
                choice = input("want to play another game? enter 0 if no.\n")
                if choice=="0":
                    print("thank you for playing with us ^_^")
                    state = False
                break
            
            if remaining_attempts==0:
                print(f"the random number is ... {random_number}\nyou were so close.")
                choice = input("want to play another game? enter 0 if no.\n")
                if choice=="0":
                    print("thank you for playing with us ^_^")
                    state = False
                break
                
        
        print("end game")                


    
    
number_guessing_game()