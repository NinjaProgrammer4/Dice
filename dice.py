def main():
    import random
    number = random.randint(1, 6)
    lucky_number = random.randint(4, 6)

    print("I am a dice and i will roll for you.")
    user_input = input("Type 'roll' to roll me and type 'smash roll' to get a lucky number : ")

    if user_input=="roll":
        print("Rolling...")
        print(number)

    elif user_input=="smash roll":
        print(lucky_number)

    else:
        print("Sorry you have entered wrong spelling. Please start the program again.")

main()
input()