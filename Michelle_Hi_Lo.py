import random

def displayCurrentCard():
    randomCard = random.randint(0, 13)
    print(f"The card is {randomCard}")
    return randomCard
def displayNextCard():
    randomCard = random.randint(0, 13)
    print(f"The card is {randomCard}")
    return randomCard
def determineWinner(preCard, postCard, choice):
    pointAssignment = None
    if preCard > postCard and choice == "l":
        pointAssignment = 100
    elif preCard > postCard and choice == "h":
        pointAssignment = -75
    elif preCard < postCard and choice == "l":
        pointAssignment = -75
    elif preCard < postCard and choice == "h":
        pointAssignment = 100
    print(f"Point Assignment: {pointAssignment}")
    return pointAssignment
def determineContinuePlaying():
    pass
def main():
    preCard = displayCurrentCard()
    choice = input("Is the next card higher or lower (h or l)? ")
    postCard = displayNextCard()
    pointAssignment = determineWinner(preCard, postCard, choice)
    pointsPlayer1 = 300 + pointAssignment


if __name__ == "__main__":
    main()
