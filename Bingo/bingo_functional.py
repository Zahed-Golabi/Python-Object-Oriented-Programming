from random import randint


rand_number = randint(0, 20)
guess = 4
name = input("Please enter your name: ")

def check_answer(answer):
    """
    check user answer guess
    """
    if answer == rand_number:
        return (True, "Bingo!")
    
    elif answer > rand_number:
        return (False, "Choose smaller number!")
    
    elif answer < rand_number:
        return (False, "Choose bigger number!")
    
    else:
        return (None, "Please insert a valid number")
    


while True:
    if guess == 0:
        print("You are out of choice!")
        break

    input_answer = int(input("Please enter your guess: "))
    result = check_answer(input_answer)

    if result[0] == False:
        print(f"You should {result[1]}")

    elif result[0] == True:
        print(result[1])
        break

    else:
        print(result[1])

    guess -= 1
        

    
