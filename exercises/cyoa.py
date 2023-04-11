"""For those who can't make decisions!"""
__author__ = "730471008"


points: int = 0
player: str = input("Please enter your name: ")
SMILEY: str = "\U0001F643"


def greet() -> None:
    """You shall be greeted!"""
    activity: str = "Sleep, Watch TV, Read, Get food, Go shopping, Go to a museum"
    print(f"What is up {player}? Welcome to The Decision Maker!{SMILEY}")
    print("Here we will help you make a decision as to what you should do today.")
    print("Your list of options include:")
    print(activity)


def instructions() -> None:
    """How to play!"""
    global player
    print("Based on our carefully and hand curated questionaire, we will be able to tell you how you should best spend your day.")
    print("There will be a tally kept based on your answers to help keep tract of your choices.")
    print("After all the questions have been answered, your activity of the day will be revealed ")


def where(in_or_out: str) -> int:
    """In or out!"""
    global points
    print("Let's get started! First question:")
    location = input("Do you wish to go out or stay in?: ")
    if (location).lower() == "go out":
        points = 0
    else:
        points = 0


def game_time_in() -> None:
    """Time to do something inside!"""
    global points
    print("Let's find something to do inside")
    while points == 0:
        sleep = input("Are you tired? ")
        if (sleep).lower() == "yes": 
            print("It is our best suggestion that you take a nap! ")
            do_it = input("Do you wish to sleep? ")
            if (do_it).lower() == "yes":
                    print("That is the end of the game! Thank you for playing and enjoy your nap!")
                    return points
            else:
                if (do_it).lower() == "no":
                    print("Ok cool! Let's find you something else!")
                else:
                    if (do_it).lower() != "yes" or "no":
                        print("That is not a valid answer choice, please answer yes or no!")
                points += 1
        else:
            points += 1
    while points == 1:
        read = input("Are you currently reading or have any books you have been looking at starting? ")
        if (read).lower() == "yes":
            print("Then you should read that book! ")
            word = input("Do you want to read a book? ")
            if (word).lower() == "yes":
                print("That is the end of the game! You should definetly read a book! Thank you for playing!")
                return points
            else:
                if (word).lower() == "no":
                    print("No worries! Let's see what else we have!")
                else:
                    if (word).lower() != "yes" or "no":
                        print("That is not a valid answer choice, please answer yes or no!")
                points += 1
        else:
            points += 1
    while points == 2:
        movie = input("Have you seen your favorite movie or tv show in the last two months? ")
        if (movie).lower() == "yes":
            print("Then you should watch that!")
            period = input("Do you want to watch it? ")
            if (period).lower() == "yes":
                print("That is the end of the game! Enjoy your movie or TV show!")
                return points
            else:
                if (period).lower() == "no":
                    print("Right on, next option here we come!")
                else:
                    if (period).lower() != "yes" or "no":
                        print("That is not a valid answer choice, please answer yes or no!")
                points += 1
        else:
            print("Sorry, we do not have any other indoor activity suggestions. Maybe try playing again and checking out the out of your home activities! ")
            points += 1


def game_time_out() -> None:
    """Outside options!"""
    global points
    print("Let's find something to do out of the house")
    points = 0
    while points == 0:
        food = input("Are you hungry? ")
        if (food).lower() == "yes":
            print("Go get some food! Hot people eat when they are hungry!")
            again = input("Do you want to get food?")
            if (again).lower() == "yes":
                print("That is the end of the game! Enjoy your food!")
                return points
            else:
                if (again).lower == "no":
                    print("Totally cool, let's keep looking!")
                else:
                    if (again).lower() != "yes" or "no":
                        print("That is not a valid answer choice, please answer yes or no!")
                points += 1
        else:
            points += 1
    while points == 1:
        shopping = input("Do you enjoy retail therapy? ")
        if (shopping).lower() == "yes":
            print("Get in loser, we are going shopping!")
            fun = input("Do you wish to go shopping? ")
            if (fun).lower() == "yes":
                print("That is the end of the game! Buy something nice!")
                return points
            else:
                if (fun).lower() == "no":
                    print("Shopping can be stressful, let's find you something else!")
                else:
                    if (fun).lower() != "yes" or "no":
                        print("That is not a valid answer choice, please answer yes or no!")
                points += 1
        else:
            points += 1
    while points == 2:
        museum = input("Do you enjoy museums? ")
        if (museum).lower() == "yes":
            print("Then you should go to a museum! ")
            great = input("Is that what you want to do? ")
            if (great).lower() == "yes":
                print("Then that is the end of the game! Hope you enjoy your museum!")
            else:
                if (great).lower() == "no":
                    print("I don't have any other options, maybe try flipping a coin or going for a drive! ")
                else:
                    if (great).lower() != "yes" or "no":
                        print("That is not a valid answer choice, please answer yes or no!")
                points += 1
        else:
            print("I don't have any other options, maybe try flipping a coin or going for a drive!")
            points += 1


def outro() -> None:
    """Exit the game!"""
    global player
    print(f"Thank you for playing {player}, this was fun!")
    print("We hope that if you selected an activity, you enjoy it!")
    print("Play again soon!")

                              
def main() -> None:
    """Game time!"""
    global points
    points = 0
    greet()
    instructions()
    print("Let's get started! First question:")
    location = input("Do you wish to go out or stay in?: ")
    if (location).lower() == "go out":
        game_time_out()
    else:
        game_time_in()
    outro()


if __name__ == "__main__":
    main()