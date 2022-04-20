print('Welcome to the Premier League quiz!')

playing = input("do you want to play the Premier League quiz? Consists of 10 questions. If you know your Football, you should probably get all 10 right! ")

if playing.lower() != "yes":
    quit()

print("Alright, let's play!")
score = 0

answer = input("Who won the most Premier League titles? ")
if answer == "Manchester United":
    print("Correct! Well, that might change soon. Welp.")
    score += 1
else:
    print("Incorrect.")

answer = input("How many teams play in the Premier League? ")
if answer == "20":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("How many teams get relegated each season? ")
if answer == "3":
    print("Correct! Fulham makes a return every other season, lol")
    score += 1
else:
    print("Incorrect.")

answer = input("Who are the defending champions? ")
if answer == "Manchester City":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input(
    "Arsenal were unbeaten from May 7, 2003 – October 16, 2004. How many games were they unbeaten for? "
)
if answer == "49":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Who ended Arsenal's 49 game unbeaten run? ")
if answer == "Manchester United":
    print("Correct! Is that a bird? Is that a plane? NO! IT'S A PIZZA!!!" )
    score += 1
else:
    print("Incorrect.")

answer = input(
    "Who is the longest serving manager in Premier League history? ")
if answer == "Sir Alex Ferguson":
    print("Correct!" )
    score += 1
else:
    print("Incorrect. If you got this wrong, please quit.")

answer = input(
    "Who holds the record for most goals scored in Premier League? ")
if answer == "Alan Shearer":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input(
    "Which team scored the most goals in a single season? Also mention the number of goals and season, separated by comma. "
)
if answer == "Manchester City, 106, 2017-18":
    print("Correct! Truckload of goals, Pep!")
    score += 1
else:
    print("Incorrect.")

answer = input(
    "Who holds the record for most games played in Premier League? Also mention the number of games played, separated by comma. "
)
if answer == "Gareth Barry, 653":
    print("Correct! Grandpa Garry. End of quiz!")
    score += 1
else:
    print("Incorrect. End of quiz!")

print("You got " + str(score) + " questions correct!")
print(str((score / 10) * 100) + "%" + " of your answers were correct!")
