print('Welcome to the Premier League quiz!')

playing = input("do you want to play the Premier League quiz? ")

if playing.lower() != "yes":
    quit()
    
print("alright, let's play!")
score = 0

answer = input("Who won the most Premier League titles? ")
if answer == "Manchester United":
    print("Correct!")
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
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Who are the defending champions? ")
if answer == "Manchester City":
    print("Correct! End of quiz!")
    score += 1
else:
    print("Incorrect. End of quiz!")
    
print("You got " + str(score) + " questions correct!")
print(str((score / 4) * 100) + "%" + " of your answers were correct!")