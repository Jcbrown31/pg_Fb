import random

number = random.randint(0,3)

words = ["cat","The office","shoe","dragon"]
hint1 = ["chase mice","Michael Scott","laces","breathes fire"]
hint2 = ["meow","Dunder Mifflin","soles","flies"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess my secret word!")
    print("Type 'hint1','hint2', 'first letter', or 'give up' for answer ")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print (hint2[number])

    elif guess == "first letter":
        print (secretword[0])

    elif guess == "give up":
        print ("Wow. You gave up.")
        print ("you failed " + str(counter) + " times")
        break

    else:
        print("Try again.")
        counter += 1
