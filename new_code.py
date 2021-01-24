import random
import pickle
from time import sleep
from datetime import datetime

class Player:

    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.played = 0
        self.bowled = 0
        self.wickets = 0
        self.conceded = 0
        self.out = False


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
                    print("OUT!\n")
                    if self.bat and wick != self.wickets:
                        side = self.score[True][3]

                        for i in range(self.wickets + 1):
                            if not side[i].out and i not in self.pair:
                                print(str(i + 1) + ") " + side[i].name)

                        print("\nPick the next batsman by index number:", end = " ")
                        flag = -1

                        while flag == -1:
                            try:
                                nex = int(input())
                            except ValueError:
                                print("Please enter an integer only:", end = " ")
                            else:
                                if (nex > self.wickets + 1 or nex <= 0) or (nex - 1 in self.pair or side[nex - 1].out):
                                    print("Please enter a valid index number:", end = " ")
                                else:
                                    flag = 1
                                    nex -= 1

                        for i in range(2):
                            if side[self.pair[i]].out:
                                break

                        self.pair[i] = nex
                        
            else:
                if self.bat and self.played == 0 and self.played != self.balls:
                    side = self.score[True][3]
                    
                    for i in range(self.wickets + 1):
                        print(str(i + 1) + ") " + side[i].name)

                    print("\nPick the striker by index number:", end = " ")
                    flag = -1

                    while flag == -1:
                        try:
                            striker = int(input())
                        except ValueError:
                            print("Please enter an integer only:", end = " ")
                        else:
                            if striker > self.wickets + 1 or striker <= 0:
                                print("Please enter a valid index number:", end = " ")
                            else:
                                flag = 1
                                striker -= 1

                    print("\nPick the non-striker by index number:", end = " ")
                    flag = -1

                    while flag == -1:
                        try:
                            nonstriker = int(input())
                        except ValueError:
                            print("Please enter an integer only:", end = " ")
                        else:
                            if nonstriker > self.wickets + 1 or nonstriker <= 0:
                                print("Please enter a valid index number:", end = " ")
                            else:
                                flag = 1
                                nonstriker -= 1

                    self.pair[0] = striker
                    self.pair[1] = nonstriker

            if self.played % 6 == 0 and self.played != self.balls:
                if (ball != -1 and self.played) or (not self.played):
                    if not self.bat:
                        side = self.score[True][3]

                        print()
                        for i in range(self.wickets, -1, -1):
                            if i != self.bowler:
                                print(str(11 - i) + ") " + side[i].name)

                        print("\nSelect bowler for next over by index number:", end = " ")
                        flag = -1

                        while flag == -1:
                            try:
                                temp = int(input())
                            except ValueError:
                                print("Please enter an integer only:", end = " ")
                            else:
                                if temp > self.wickets + 1 or temp <= 0 or 11 - temp == self.bowler:
                                    print("Please enter a valid index number:", end = " ")
                                else:
                                    flag = 1
                                    temp = 11 - temp

                        self.bowler = temp

                    else:
                        temp = self.bowler

                        while temp == self.bowler:
                            temp = random.randint(6, 10)
                            
                        self.bowler = temp

                          
            print()
            bat1 = self.score[self.bat][3][self.pair[0]]
            bat2 = self.score[self.bat][3][self.pair[1]]
            bowl = self.score[not self.bat][3][self.bowler]

            if wick != self.wickets:
                print(bat1.name + " " + str(bat1.runs) + "(" + str(bat1.played) + ")", end = "")
                if not self.strike:
                    print("*", end = "")
                print("    ", end = "")
                
                print(bat2.name + " " + str(bat2.runs) + "(" + str(bat2.played) + ")", end = "")
                if self.strike:
                    print("*", end = "")
            else:
                print(self.score[self.bat][3][self.pair[not self.strike]].name + " " + str(self.score[self.bat][3][self.pair[not self.strike]].runs) + "(" + str(self.score[self.bat][3][self.pair[not self.strike]].played) + ")*", end = "")

            print("\n")

            b = str(int((bowl.bowled - bowl.bowled % 6) / 6)) + "." + str(bowl.bowled % 6)
            print(bowl.name + " " + str(bowl.wickets) + "/" + str(bowl.conceded) + " (" + b + ")\n")
            

            win = " win by "
            result = [". Hurray!", ". Better luck next time."]
            res = ""

            if self.isSecInn:
                if runs >= target:
                    res += who + win + str(self.wickets - wick) + " wicket"
                    
                    if self.wickets - wick > 1:
                        res += "s"

                    res += result[not self.bat]

                    print(res)
                    
                    input("Press ENTER to return to main menu...")
                    break
                else:
                    if wick == self.wickets or self.played == self.balls:
                        if runs == target - 1:
                            print("It's a tie!")
                        else:
                            res += self.score[not self.bat][0] + win + str(target - runs - 1) + " run"
                            if target - runs > 2:
                                res += "s"

                            res += result[self.bat]
                                
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
                    self.bowler = -1
                    self.pair = [0, 1]
                    self.strike = 0
                    input("1st innings ends. Press ENTER to play 2nd innings...")
                    continue

            ch = input("Type \n1. n + ENTER to flip book\n2. s + ENTER to save game\n3. press ENTER to quit game\n-> ")

            if ch.lower() == "n":
                page = random.randint(1, pages)
                ball = page % 10

                self.played += 1
                self.score[self.bat][3][self.pair[self.strike]].played += 1
                self.score[not self.bat][3][self.bowler].bowled += 1

                if ball:
                    if ball > 6:
                        ball -= 6
                    self.score[self.bat][1] += ball
                    self.score[self.bat][3][self.pair[self.strike]].runs += ball
                    self.score[not self.bat][3][self.bowler].conceded += ball
                    
                    if ball % 2:
                        self.strike = not self.strike
                else:
                    self.score[self.bat][2] += 1
                    self.score[self.bat][3][self.pair[self.strike]].out = True
                    self.score[not self.bat][3][self.bowler].wickets += 1
                    
                    if self.score[self.bat][2] != self.wickets:
                        if not self.bat:
                            self.pair[self.strike] = self.score[self.bat][2] + 1
                    else:
                        continue
                    

                if self.played % 6 == 0 and self.played:
                    self.strike = not self.strike

                
            elif ch.lower() == "s":
                self.__save()
                ball = -1
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
                        ball = -1
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


    def __init__(self, pages, overs, wickets, bat, u, c):
        self.pages = pages
        self.balls = overs * 6
        self.wickets = wickets
        self.bat = bat
        self.score = {True: [u, 0, 0, []], False: [c, 0, 0, []]}
        self.played = 0
        self.isSecInn = False
        self.id = ""
        self.saved = False

        f1 = open(f'res\{u}.txt')
        team1 = f1.read().splitlines()
        for name in team1:
            self.score[True][3].append(Player(name))

        f2 = open(f'res\{c}.txt')
        team2 = f2.read().splitlines()
        for name in team2:
            self.score[False][3].append(Player(name))

        f1.close()
        f2.close()
        
        self.pair = [0, 1]
        self.strike = 0
        self.bowler = -1


print("Welcome to Book Cricket!")
input("Press ENTER to continue...")


while True:
    print("\n" + "*"*40 + "\n")
    choice = input("1. (N)ew game\n2. (L)oad game\n3. (R)ules\n4. (Q)uit\n\n->")

    if choice.lower() == "n":

        teams = ["England", "India", "New Zealand", "Australia", "South Africa", "Pakistan", "Bangladesh", "Sri Lanka", "West Indies", "Afghanistan"]
        print()
        for i in range(len(teams)):
            print(str(i + 1) + ". " + teams[i])

        print("\nEnter index no. of your team:", end = " ")
        flag = -1
        while flag == -1:
            try:
                user = int(input())
            except ValueError:
                print("Invalid input. Please try again:", end = " ")
            else:
                if user <= len(teams) and user > 0:
                    flag = 1
                else:
                    print("Invalid input. Please try again:", end = " ")

        print("\nEnter index no. of CPU team:", end = " ")
        flag = -1
        while flag == -1:
            try:
                cpu = int(input())
            except ValueError:
                print("Invalid input. Please try again:", end = " ")
            else:
                if cpu <= len(teams) and cpu > 0:
                    if cpu != user:
                        flag = 1
                    else:
                        print("Please choose a different team for CPU:", end = " ")
                else:
                    print("Invalid input. Please try again:", end = " ")

        user = teams[user - 1]
        cpu = teams[cpu - 1]
                
        
        print("\nEnter number of overs:", end = " ")
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
                elif w > 10:
                    print("Please enter atmost 10 wickets:", end = " ")
                else:
                    flag = 1

        print("\n\nToss time!")
        print("Flipping coin", end = "")

        for i in range(3):
            print(".", end = "")
            sleep(0.5)

        toss = random.randint(0, 1)

        if toss:
            ch = input(user + " has won the toss and chosen to ___\nBat or bowl?: ")
            
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
            print(cpu + " has won the toss and chosen to", end = " ")

            if cch:
                print("bowl.")
            else:
                print("bat.")

        input("Press ENTER to start the match...")
        new = match(p, o, w, bat, user, cpu)
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
                                    with open('games.pkl', 'wb') as r:
                                        for x in range(len(g)):
                                            if x != rem - 1:
                                                pickle.dump(g[x], r)

                                    g.remove(g[rem - 1])
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
