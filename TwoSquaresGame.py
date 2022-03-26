# By Ethar Raid
# Two squares game
sq1 = "⬜"
sq2 = "⬜"
sq3 = "⬜"
sq4 = "⬜"
sq5 = "⬜"
sq6 = "⬜"
sq7 = "⬜"
sq8 = "⬜"
sq9 = "⬜"
sq10 = "⬜"
sq11 = "⬜"
sq12 = "⬜"
sq13 = "⬜"
sq14 = "⬜"
sq15 = "⬜"
sq16 = "⬜"
print("Welcome to the two squares game")
print("Rules are as follows: 1-Players must take in turns to fill two parallel boxes either horizontally or vertically")
print("2-Boxes are numbered from top to bottom. First row being 1 2 3 4")
print("Second row being 5 6 7 8")
print("Third row being 9 10 11 12")
print("Fourth being 13 14 15 16")
print("3-Last player with no free boxes available loses and the other player wins")
print("Enjoy!")


def boxes():
    print(sq1, sq2, sq3, sq4)
    print(sq5, sq6, sq7, sq8)
    print(sq9, sq10, sq11, sq12)
    print(sq13, sq14, sq15, sq16)
boxes()


# This function handles the first player's turn
def firstTurn():
    global sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9, sq10, sq11, sq12, sq13, sq14, sq15, sq16
    player1 = input("Player1 please type any numbers from 1-16 and then press enter to fill the squares' respective number: ")
    p1 = input("enter the second number: ")
    if player1 == "1" and p1 == "2":
        sq1 = "⬛"
        sq2 = "⬛"
    if player1 == "2" and p1 == "1":
        sq1 = "⬛"
        sq2 = "⬛"
    if player1 == "1" and p1 == "5":
        sq1 = "⬛"
        sq5 = "⬛"
    if player1 == "5" and p1 == "1":
        sq1 = "⬛"
        sq5 = "⬛"
    if player1 == "2" and p1 == "6":
        sq2 = "⬛"
        sq6 = "⬛"
    if player1 == "6" and p1 == "2":
        sq2 = "⬛"
        sq6 = "⬛"
    if player1 == "2" and p1 == "3":
        sq2 = "⬛"
        sq3 = "⬛"
    if player1 == "3" and p1 == "2":
        sq2 = "⬛"
        sq3 = "⬛"
    if player1 == "3" and p1 == "7":
        sq3 = "⬛"
        sq7 = "⬛"
    if player1 == "7" and p1 == "3":
        sq3 = "⬛"
        sq7 = "⬛"
    if player1 == "3" and p1 == "4":
        sq3 = "⬛"
        sq4 = "⬛"
    if player1 == "4" and p1 == "3":
        sq3 = "⬛"
        sq4 = "⬛"
    if player1 == "4" and p1 == "8":
        sq4 = "⬛"
        sq8 = "⬛"
    if player1 == "8" and p1 == "4":
        sq4 = "⬛"
        sq8 = "⬛"
    if player1 == "5" and p1 == "6":
        sq5 = "⬛"
        sq6 = "⬛"
    if player1 == "6" and p1 == "5":
        sq5 = "⬛"
        sq6 = "⬛"
    if player1 == "5" and p1 == "9":
        sq5 = "⬛"
        sq9 = "⬛"
    if player1 == "9" and p1 == "5":
        sq5 = "⬛"
        sq9 = "⬛"
    if player1 == "6" and p1 == "7":
        sq6 = "⬛"
        sq7 = "⬛"
    if player1 == "7" and p1 == "6":
        sq6 = "⬛"
        sq7 = "⬛"
    if player1 == "6" and p1 == "7":
        sq6 = "⬛"
        sq7 = "⬛"
    if player1 == "6" and p1 == "10":
        sq6 = "⬛"
        sq10 = "⬛"
    if player1 == "10" and p1 == "6":
        sq6 = "⬛"
        sq10 = "⬛"
    if player1 == "7" and p1 == "11":
        sq7 = "⬛"
        sq11 = "⬛"
    if player1 == "11" and p1 == "7":
        sq7 = "⬛"
        sq11 = "⬛"
    if player1 == "7" and p1 == "8":
        sq7 = "⬛"
        sq8 = "⬛"
    if player1 == "8" and p1 == "7":
        sq7 = "⬛"
        sq8 = "⬛"
    if player1 == "8" and p1 == "12":
        sq8 = "⬛"
        sq12 = "⬛"
    if player1 == "12" and p1 == "8":
        sq8 = "⬛"
        sq12 = "⬛"
    if player1 == "9" and p1 == "13":
        sq9 = "⬛"
        sq13 = "⬛"
    if player1 == "13" and p1 == "9":
        sq9 = "⬛"
        sq13 = "⬛"
    if player1 == "9" and p1 == "10":
        sq9 = "⬛"
        sq10 = "⬛"
    if player1 == "10" and p1 == "9":
        sq9 = "⬛"
        sq10 = "⬛"
    if player1 == "10" and p1 == "14":
        sq10 = "⬛"
        sq14 = "⬛"
    if player1 == "14" and p1 == "10":
        sq10 = "⬛"
        sq14 = "⬛"
    if player1 == "10" and p1 == "11":
        sq10 = "⬛"
        sq11 = "⬛"
    if player1 == "11" and p1 == "10":
        sq10 = "⬛"
        sq11 = "⬛"
    if player1 == "11" and p1 == "15":
        sq11 = "⬛"
        sq15 = "⬛"
    if player1 == "15" and p1 == "11":
        sq11 = "⬛"
        sq15 = "⬛"
    if player1 == "11" and p1 == "12":
        sq11 = "⬛"
        sq12 = "⬛"
    if player1 == "12" and p1 == "11":
        sq11 = "⬛"
        sq12 = "⬛"
    if player1 == "12" and p1 == "16":
        sq12 = "⬛"
        sq16 = "⬛"
    if player1 == "16" and p1 == "12":
        sq12 = "⬛"
        sq16 = "⬛"
    if player1 == "13" and p1 == "14":
        sq13 = "⬛"
        sq14 = "⬛"
    if player1 == "14" and p1 == "13":
        sq13 = "⬛"
        sq14 = "⬛"
    if player1 == "14" and p1 == "15":
        sq14 = "⬛"
        sq15 = "⬛"
    if player1 == "15" and p1 == "14":
        sq14 = "⬛"
        sq15 = "⬛"
    if player1 == "15" and p1 == "16":
        sq15 = "⬛"
        sq16 = "⬛"
    if player1 == "16" and p1 == "15":
        sq15 = "⬛"
        sq16 = "⬛"
    boxes()
    if player1 == p1:
        print("You can't enter the same number twice")
        firstTurn()
    if int(player1) not in range(1, 17):
        print("Please enter a valid number")
        firstTurn()


# This function handles the second player's turn
def secondTurn():
    global sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9, sq10, sq11, sq12, sq13, sq14, sq15, sq16
    player2 = input("Player2 please type any numbers from 1-16 and then press enter to fill the squares' respective number:  ")
    p2 = input("enter the second number:  ")
    if player2 == "1" and p2 == "2":
        sq1 = "⬛"
        sq2 = "⬛"
    if player2 == "2" and p2 == "1":
        sq1 = "⬛"
        sq2 = "⬛"
    if player2 == "1" and p2 == "5":
        sq1 = "⬛"
        sq5 = "⬛"
    if player2 == "5" and p2 == "1":
        sq1 = "⬛"
        sq5 = "⬛"
    if player2 == "2" and p2 == "6":
        sq2 = "⬛"
        sq6 = "⬛"
    if player2 == "6" and p2 == "2":
        sq2 = "⬛"
        sq6 = "⬛"
    if player2 == "2" and p2 == "3":
        sq2 = "⬛"
        sq3 = "⬛"
    if player2 == "3" and p2 == "2":
        sq2 = "⬛"
        sq3 = "⬛"
    if player2 == "3" and p2 == "7":
        sq3 = "⬛"
        sq7 = "⬛"
    if player2 == "7" and p2 == "3":
        sq3 = "⬛"
        sq7 = "⬛"
    if player2 == "3" and p2 == "4":
        sq3 = "⬛"
        sq4 = "⬛"
    if player2 == "4" and p2 == "3":
        sq3 = "⬛"
        sq4 = "⬛"
    if player2 == "4" and p2 == "8":
        sq4 = "⬛"
        sq8 = "⬛"
    if player2 == "8" and p2 == "4":
        sq4 = "⬛"
        sq8 = "⬛"
    if player2 == "5" and p2 == "6":
        sq5 = "⬛"
        sq6 = "⬛"
    if player2 == "6" and p2 == "5":
        sq5 = "⬛"
        sq6 = "⬛"
    if player2 == "5" and p2 == "9":
        sq5 = "⬛"
        sq9 = "⬛"
    if player2 == "9" and p2 == "5":
        sq5 = "⬛"
        sq9 = "⬛"
    if player2 == "6" and p2 == "7":
        sq6 = "⬛"
        sq7 = "⬛"
    if player2 == "7" and p2 == "6":
        sq6 = "⬛"
        sq7 = "⬛"
    if player2 == "6" and p2 == "7":
        sq6 = "⬛"
        sq7 = "⬛"
    if player2 == "6" and p2 == "10":
        sq6 = "⬛"
        sq10 = "⬛"
    if player2 == "10" and p2 == "6":
        sq6 = "⬛"
        sq10 = "⬛"
    if player2 == "7" and p2 == "11":
        sq7 = "⬛"
        sq11 = "⬛"
    if player2 == "11" and p2 == "7":
        sq7 = "⬛"
        sq11 = "⬛"
    if player2 == "7" and p2 == "8":
        sq7 = "⬛"
        sq8 = "⬛"
    if player2 == "8" and p2 == "7":
        sq7 = "⬛"
        sq8 = "⬛"
    if player2 == "8" and p2 == "12":
        sq8 = "⬛"
        sq12 = "⬛"
    if int(player2) == 12 and int(p2) == 8:
        sq8 = "⬛"
        sq12 = "⬛"
    if player2 == "9" and p2 == "13":
        sq9 = "⬛"
        sq13 = "⬛"
    if player2 == "13" and p2 == "9":
        sq9 = "⬛"
        sq13 = "⬛"
    if player2 == "9" and p2 == "10":
        sq9 = "⬛"
        sq10 = "⬛"
    if player2 == "10" and p2 == "9":
        sq9 = "⬛"
        sq10 = "⬛"
    if player2 == "10" and p2 == "14":
        sq10 = "⬛"
        sq14 = "⬛"
    if player2 == "14" and p2 == "10":
        sq10 = "⬛"
        sq14 = "⬛"
    if player2 == "10" and p2 == "11":
        sq10 = "⬛"
        sq11 = "⬛"
    if player2 == "11" and p2 == "10":
        sq10 = "⬛"
        sq11 = "⬛"
    if player2 == "11" and p2 == "15":
        sq11 = "⬛"
        sq15 = "⬛"
    if player2 == "15" and p2 == "11":
        sq11 = "⬛"
        sq15 = "⬛"
    if player2 == "11" and p2 == "12":
        sq11 = "⬛"
        sq12 = "⬛"
    if player2 == "12" and p2 == "11":
        sq11 = "⬛"
        sq12 = "⬛"
    if player2 == "12" and p2 == "16":
        sq12 = "⬛"
        sq16 = "⬛"
    if player2 == "16" and p2 == "12":
        sq12 = "⬛"
        sq16 = "⬛"
    if player2 == "13" and p2 == "14":
        sq13 = "⬛"
        sq14 = "⬛"
    if player2 == "14" and p2 == "13":
        sq13 = "⬛"
        sq14 = "⬛"
    if player2 == "14" and p2 == "15":
        sq14 = "⬛"
        sq15 = "⬛"
    if player2 == "15" and p2 == "14":
        sq14 = "⬛"
        sq15 = "⬛"
    if player2 == "15" and p2 == "16":
        sq15 = "⬛"
        sq16 = "⬛"
    if player2 == "16" and p2 == "15":
        sq15 = "⬛"
        sq16 = "⬛"
    boxes()
    if player2 == p2:
        print("You can't enter the same number twice")
        secondTurn()
    if int(player2) not in range(1, 17):
        print("Please enter a valid number")
        secondTurn()



x = 0
y = 0
firstTurn()
x += 1
secondTurn()
y += 1
firstTurn()
x += 1
secondTurn()
y += 1
firstTurn()
x += 1
secondTurn()
y += 1
firstTurn()
x += 1
if x == 4:
    print("Player1 wins!")
    exit()
else:
    secondTurn()
secondTurn()
y += 1
if y == 4:
    print("Player2 wins!")
    exit()