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

            print("\n" + "*"*40 + "\n")

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
                    
                    input("Press ENTER to return to main menu...")
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
                            
                        input("Press ENTER to return to main menu...")
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

            if ch.lower() == "n":
                page = random.randint(1, pages)
                ball = page % 10

                if ball:
                    if ball > 6:
                        ball -= 6
                    self.score[self.bat][1] += ball
                else:
                    self.score[self.bat][2] += 1

                self.played += 1
                
            elif ch.lower() == "s":
                self.__save()
                input("Game saved successfully! Press ENTER to continue with game...")
                        
            elif ch == "":
                if self.saved:
                    q = input("\nAre you sure you want to QUIT? Please press (q) to confirm: ")
                    if q.lower() == "q":
                        break
                else:
                    q = input("\nAre you sure you want to QUIT without saving? Please press \n(q) to quit without saving\n(s) to save and quit\n-> ")
                    if q.lower() == "q":
                        break
                    elif q.lower() == "s":
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


while True:
    print("\n" + "*"*40 + "\n")
    choice = input("1. (N)ew game\n2. (L)oad game\n3. (R)ules\n4. (Q)uit\n\n->")

    if choice.lower() == "n":
        
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
        new = match(p, o, w, bat)
        new.play()

    elif choice.lower() == "l":
        g = []

        try:
            with open('games.pkl', 'rb') as games:
                while True:
                    try:
                        game = pickle.load(games)
                        g.append(game)
                    except EOFError:
                        break
        except FileNotFoundError:
            input("You currently have no saved games. Press ENTER to return to main menu...")


        if len(g):
            i = 1
            print("Saved games: ")
            for _ in g:
                print(str(i) + ". " + _.id)
                i += 1
                
            
            while True:
                s = input("\nEnter serial no. of game to be loaded, press (d) to remove a save, or press (q) to return to main menu-> ")
                try:
                    s = int(s)
                    if s <= len(g) and s > 0:
                        load = g[s - 1]
                        load.play()
                        break
                    else:
                        print("Game not found!")
                except ValueError:
                    if s.lower() == "q":
                        break
                    elif s.lower() == "d":
                        while True:
                            rem = input("Enter index no. of save to be removed -> ")
                            try:
                                rem = int(rem)
                                if rem <= len(g) and rem > 0:
                                    with open('games.pkl', 'wb') as remove:
                                        for x in range(len(g)):
                                            if x != rem - 1:
                                                pickle.dump(g[x], remove)

                                    input("Save deleted successfully! Press ENTER to continue...")
                                    break
                                else:
                                    print("Game not found!")
                            except ValueError:
                                pass
                            
        else:
            input("You currently have no saved games. Press ENTER to return to main menu...")
                    
    elif choice.lower() == "r":
        with open('rules.txt') as rules:
            r = rules.read()
            input(r)
            
    elif choice.lower() == "q":
        q = input("\nAre you sure you want to QUIT? Please press (q) to confirm: ")
        if q.lower() == "q":
            break

        
        


        

        
        







    
        


        

