import random
import pickle
from time import sleep
from datetime import datetime

class match:

    def play(self):
        ball = -1
        page = -1
        while True:
            print()
            runs = self.score[self.bat][1]
            wick = self.score[self.bat][2]
            who = self.score[self.bat][0]
            target = self.score[not self.bat][1] + 1
            pages = self.pages

            currScore = ""
            currScore += who + ": " + str(runs) + "/" + str(wick)
            print(currScore)

            over = str(int((self.played - self.played % 6) / 6)) + "." + str(self.played % 6) + " overs"
            print(over)
            print()

            if self.isSecInn:
                print("Target: " + str(target))
                print()

            if ball != -1:
                print("Page: " + str(page))
                if ball:
                    print(str(ball) + " runs scored.")
                else:
                    print("OUT!")
                print()

            result = ["You lose by ", "You win by ", ". Better luck next time.", ". Hurray!"]
            res = ""

            if self.isSecInn:
                if runs >= target:
                    res += result[self.bat] + str(self.wickets - wick) + " wicket"
                    
                    if self.wickets - wick > 1:
                        res += "s"

                    res += result[self.bat + 2]

                    print(res)
                    
                    input("Press ENTER to exit...")
                    break
                else:
                    if wick == self.wickets or self.played == self.balls:
                        if runs == target - 1:
                            print("It's a tie!")
                        else:
                            res += result[not self.bat] + str(target - runs - 1) + " run"
                            if target - runs > 2:
                                res += "s"

                            res += result[(not self.bat) + 2]
                                
                            print(res)
                            
                        input("Press ENTER to exit...")
                        break
                
            else:
                if wick == self.wickets or self.played == self.balls:
                    self.isSecInn = True
                    self.played = 0
                    self.bat = not self.bat
                    ball = -1
                    page = -1
                    input("1st innings ends. Press ENTER to play 2nd innings...")
                    continue

            ch = input("Type \n1. n + ENTER to flip book\n2. s + ENTER to save game\n3. press ENTER to quit game\n-> ")

            if ch == "n":
                page = random.randint(1, pages)
                ball = page % 10

                if ball:
                    if ball > 6:
                        ball -= 6
                    self.score[self.bat][1] += ball
                else:
                    self.score[self.bat][2] += 1

                self.played += 1
                
            elif ch == "s":
                self.__save()
                input("Game saved successfully! Press ENTER to continue with game...")
                        
            elif ch == "":
                if self.saved:
                    q = input("\nAre you sure you want to QUIT? Please press (q) to confirm: ")
                    if q == "q":
                        break
                else:
                    q = input("\nAre you sure you want to QUIT without saving? Please press \n(q) to quit without saving\n(s) to save and quit\n-> ")
                    if q == "q":
                        break
                    elif q == "s":
                        self.__save()
                        input("Game saved successfully! Press ENTER to exit game...")
                        break

    def __save(self):
        self.id = input("Enter ID to save game: ")
        
        while len(self.id) < 4:
            self.id = input("User-entered ID must be atleast 4 characters long: ")

        self.id += " "*4 + str(datetime.now())

        with open('games.pkl', 'ab') as games:
            pickle.dump(self, games)

        self.saved = True


    def __init__(self, pages, overs, wickets, bat):
        self.pages = pages
        self.balls = overs * 6
        self.wickets = wickets
        self.bat = bat
        self.score = {True: ["User", 0, 0], False: ["CPU", 0, 0]}
        self.played = 0
        self.isSecInn = False
        self.id = ""
        self.saved = False

print("Welcome to Book Cricket!")
input("Press ENTER to continue...")


print("\n\nEnter number of overs:", end = " ")
flag = -1

while flag == -1:
    try:
        o = int(input())
    except ValueError:
        print("Please enter a positive integer only:", end = " ")
    else:
        if o < 1:
            print("Please enter atleast 1 over:", end = " ")
        else:
            flag = 1

print("\nEnter number of pages:", end = " ")
flag = -1

while flag == -1:
    try:
        p = int(input())
    except ValueError:
        print("Please enter a positive integer only:", end = " ")
    else:
        if p < 10:
            print("Please enter atleast 10 pages:", end = " ")
        else:
            flag = 1

print("\nEnter number of wickets:", end = " ")
flag = -1

while flag == -1:
    try:
        w = int(input())
    except ValueError:
        print("Please enter a positive integer only:", end = " ")
    else:
        if w < 1:
            print("Please enter atleast 1 wicket:", end = " ")
        else:
            flag = 1

print("\n\nToss time!")
print("Flipping coin", end = "")

for i in range(3):
    print(".", end = "")
    sleep(0.5)

toss = random.randint(0, 1)

if toss:
    ch = input("You've won the toss!\nBat or bowl?: ")
    
    while 1:
        if ch.lower() == "bat":
            bat = True
            break
        elif ch.lower() == "bowl":
            bat = False
            break
        else:
            ch = input("Please enter a valid choice: ")

else:
    cch = random.randint(0, 1)
    bat = cch
    print("CPU has won the toss and chosen to", end = " ")

    if cch:
        print("bowl.")
    else:
        print("bat.")

input("Press ENTER to start the match...")
lets = match(p, o, w, bat)
lets.play()







    
        


        

