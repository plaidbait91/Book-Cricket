#include<iostream.h>

#include<conio.h>

#include<stdio.h>

#include<process.h>

#include<string.h>

#include<stdlib.h>

#include<dos.h>

#include<fstream.h>

class match {
  int balls, played, nop, allout, atbat, inn2;
  int score[2][2]; char id[11];
  public:
  match(int = 0, int = 0, int = 0, int = 0);
  int totalBall();
  int playedBall(int = 0);
  int pages();
  int cpuBat();
  int isInning2();
  void changeInning();
  int currScore(int = 0);
  int currWickets(int = 0);
  int otherScore();
  int allOut();
  void setId(char[]);
  int matchId(char[]);
};

match::match(int no, int ov, int out, int bat) {
  nop = no;
  balls = ov * 6;
  atbat = bat;
  allout = out;
  played = 0;
  inn2 = 0;
  for (int i = 0; i < 2; i++)
    for (int j = 0; j < 2; j++) score[i][j] = 0;
}

int match::allOut() {
  return allout;
}

int match::totalBall() {
  return balls;
}

int match::playedBall(int k) {
  played += k;
  return played;
}

int match::pages() {
  return nop;
}

int match::cpuBat() {
  return atbat;
}

int match::isInning2() {
  return inn2;
}

void match::changeInning() {
  atbat++;
  atbat %= 2;
  played = 0;
  inn2 = 1;
}

int match::currScore(int a) {
  score[atbat][0] += a;
  return score[atbat][0];
}

int match::currWickets(int b) {
  score[atbat][1] += b;
  return score[atbat][1];
}

int match::otherScore() {
  return score[1 - atbat][0];
}

void startscr() {
  char str[][100] = {
    "C++ Book Cricket",
    "By Srikant Tangirala,",
    "Abhilash Jena and Saahen Sharma",
    "Class XII - E"
  };
  int i, j;
  textcolor(RED);

  clrscr();
  for (i = 0, j = 30; str[0][i] != '\0'; j++, i++) {
    gotoxy(j, 12);
    cprintf("%c", str[0][i]);
    delay(50);
  }

  delay(2500);
  textcolor(LIGHTRED);
  for (j = 27, i = 0; str[1][i] != '\0'; j++, i++) {
    gotoxy(j, 12);
    cprintf("%c", str[1][i]);
    delay(50);
  }

  textcolor(WHITE);
  for (j = 22, i = 0; str[2][i] != '\0'; j++, i++) {
    gotoxy(j, 13);
    cprintf("%c", str[2][i]);
    delay(50);
  }

  textcolor(GREEN);
  for (j = 30, i = 0; str[3][i] != '\0'; j++, i++) {
    gotoxy(j, 14);
    cprintf("%c", str[3][i]);
    delay(50);
  }

  gotoxy(22, 16);
  textcolor(WHITE);
  cprintf("Press any key to start playing...");
  getch();

}

void endscr() {
  clrscr();
  char end[][100] = {
    "Thank you for playing!",
    "XII - E forever :D"
  };
  int i, j;

  textcolor(LIGHTRED);
  for (i = 0, j = 30; end[0][i] != '\0'; i++, j++) {
    gotoxy(j, 12);
    cprintf("%c", end[0][i]);
    delay(50);
  }

  delay(1000);
  textcolor(LIGHTBLUE);
  for (i = 0, j = 31; end[1][i] != '\0'; i++, j++) {
    gotoxy(j, 13);
    cprintf("%c", end[1][i]);
    delay(50);
  }

  gotoxy(30, 15);
  cout << "Press any key to exit...";
  getch();
  exit(0);
}

void match::setId(char i[]) {
  strcpy(id, i);
}

int match::matchId(char i[]) {
  if(strcmp(id, i) == 0) return 1;
  else return -1;
}

void play(match m) {
  int c, page, ball = -1;

  while (1) { //Let the match begin!
    clrscr();
    if (m.cpuBat()) cout << "CPU: ";
    else cout << "You: ";
    cout << m.currScore() << "/" << m.currWickets() << endl;
    cout << m.playedBall() / 6 << "." << m.playedBall() % 6 << " overs." << endl;

    if (m.isInning2()) cout << "Target: " << m.otherScore() + 1 << endl;
    cout << "\n";

    if (ball != -1) {
      cout << "Page: " << page << endl;
      if (ball != 0) cout << ball << " runs scored.";
      else cout << "OUT!";
      cout << "\n\n";
    }

    if (m.isInning2()) { //If 2nd innings

      if (m.currScore() > m.otherScore()) { //If target reached
	if (!m.cpuBat()) cout << "You won!!\n\n";
	else {
	  cout << "You lost. Better luck next time!\n\n";
	}
	delay(2000);
	cout << "Press any key to return to main menu...";
	getch();
	break;
      } else if (m.currScore() == m.otherScore()) { //If scores level
	if (m.currWickets() == m.allOut() || m.playedBall() == m.totalBall()) { //Is the innings over?
	  cout << "It's a tie!\n\n";
	  delay(2000);
	  cout << "Press any key to return to main menu...";
	  getch();
	  break;
	}
      } else {
	if (m.currWickets() == m.allOut() || m.playedBall() == m.totalBall()) {
	  if (m.cpuBat()) cout << "You won!!\n\n";
	  else {
	    cout << "You lost. Better luck next time!\n\n";
	  }
	  delay(2000);
	  cout << "Press any key to return to main menu...";
	  getch();
	  break;
	}
      }

    } else { //If 1st innings
      if (m.currWickets() == m.allOut() || m.playedBall() == m.totalBall()) {
	m.changeInning();
	ball = -1;
	cout << "1st Innings has ended.\n";
	delay(2000);
	cout << "Press any key to progress to 2nd innings...";
	getch();
	continue;
      }
    }

    cout << "1. Next ball\n2. Save Game\n3. Exit\n\n";
    cout << "-> ";
    cin >> c;

    switch (c) {
    case 3:
      cout << "\nDo you really want to exit?";
      cout << "\nPress 'y' to exit or press any other key to return to game...";
      char ex = getch();
      if (ex == 'y' || ex == 'Y') endscr();
      break;
    case 1:
      page = random(m.pages());
      ball = page % 10;

      if (ball > 0) m.currScore(ball);
      else m.currWickets(1);
      m.playedBall(1);
      break;
    case 2:
      fstream save;
      match t; char tem[11];
      int flag = 1;
      cout << "\nEnter name of game save(max. len 10): ";
      gets(tem); m.setId(tem);
      save.open("games.dat", ios::binary | ios:: in );
      if (save) {
	while (!save.eof()) {
	  save.read((char * ) & t, sizeof(t));
	  if (save.eof()) break;
	  if (t.matchId(tem) == 1) {
	    flag = -1;
	    break;
	  }
	}
      }
      if (flag == 1) {
	save.close();
	save.open("games.dat", ios::binary | ios::app);
	save.write((char * ) & m, sizeof(m));
	cout << "\nGame saved successfully!";
      } else {
	cout << "\nA game already exists with that ID!";
      }
      save.close();
      cout << "\nPress any key to return to game...";
      getch();
      break;
    }

  }
}

void main() {
  int ch;
  randomize();
  startscr();

  do {
    clrscr();
    cout << "1. New Game\n2. Load Game\n3. Rules\n4. Exit\n\n";
    cout << "Enter Choice: ";
    cin >> ch;

    switch (ch) {
    case 4:
      endscr();
    case 1:
      clrscr();
      int no, ov, out, bat;

      cout << "Enter length of book(min. 10 pages): ";
      do {
	cin >> no;
	if (no < 10) cout << "\nToo few pages! The book should be atleast 10 pages long: ";
      } while (no < 10);

      cout << "Enter no. of overs(min. 1): ";
      do {
	cin >> ov;
	if (ov < 1) cout << "\nToo few overs! Atleast 1 over per inning: ";
      } while (ov < 1);

      cout << "Enter no. of wickets per innings: ";
      do {
	cin >> out;
	if (out < 1) cout << "\nYou must have atleast one wicket per inning: ";
	if (out > 10) cout << "\nYou cannot have more than 10 wickets per inning: ";
      } while (out < 1 || out > 10);

      clrscr();
      int t;
      cout << "Toss time!\n\n";
      delay(700);
      cout << "Flipping coin";
      for (int i = 0; i < 3; i++) {
	cout << ".";
	delay(700);
      }
      t = random(2);

      if (t) {
	char c[5];
	cout << "\nYou won the toss!";
	delay(500);
	cout << "\nBat or bowl?: ";

	do {
	  gets(c);
	  if (strcmpi(c, "bat") == 0) {
	    bat = 0;
	    break;
	  } else if (strcmpi(c, "bowl") == 0) {
	    bat = 1;
	    break;
	  } else cout << "\nInvalid input. Please enter valid input(bat/bowl): ";
	} while (strcmpi(c, "bat") != 0 && strcmpi(c, "bowl") != 0);

      } else {
	int c = random(2);
	cout << "\nCPU won the toss and chose to ";
	if (c) {
	  cout << "bowl.";
	  bat = 0;
	} else {
	  cout << "bat.";
	  bat = 1;
	}
	delay(3000);
      }

      match m(no, ov, out, bat);
      play(m);
      break;

    case 2:
      fstream load;
      int flag = -1, k = 0;
      match l;
      char search[11];
      clrscr();
      load.open("games.dat", ios::binary | ios:: in );

      if (load) {
	while (!load.eof()) {
	  load.read((char * ) & l, sizeof(l));
	  if (load.eof()) break;
	  k++;
	}
      }
      load.close();

      if (k > 0) {
	cout << "There are currently " << k << " games saved to the database.";
	cout << "\nEnter name of saved game: ";
	gets(search);
	load.open("games.dat", ios::binary | ios:: in );
	if (load) {
	  while (!load.eof()) {
	    load.read((char * ) & l, sizeof(l));
	    if (load.eof()) break;
	    if (l.matchId(search) == 1) {
	      flag = 1;
	      break;
	    }
	  }
	}

	if (flag == 1) {
	  cout << "\nGame loaded successfully!";
	  cout << "\nPress any key to begin game...";
	  getch();
	  play(l);
	} else {
	  cout << "\nSave game not found!\nPress any key to return to main menu...";
	  getch();
	}
	load.close();
      } else {
        cout << "There are currently no games saved to the database.";
        cout << "\nPress any key to return to main menu...";
        getch();
      }
      break;
    case 3:
      fstream rules;
      char x[150];

      clrscr();
      rules.open("rules.txt", ios:: in );
      while (!rules.eof()) {
        rules.getline(x, 150, '\n');
        cout << x << endl;
        if (rules.eof()) break;
      }
      getch();
      break;
    }
  } while (ch != 4);

}