import random
import sys

lis = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#Display the contents of board
def displayBoard():
    print("", lis[0], "|", lis[1], "|", lis[2])
    print("-----------")
    print("", lis[3], "|", lis[4], "|", lis[5])
    print("-----------")
    print("", lis[6], "|", lis[7], "|", lis[8])

#Sample Board
def displaySampleBoard():
    print("", '1', "|", '2', "|", '3')
    print("-----------")
    print("", '4', "|", '5', "|", '6')
    print("-----------")
    print("", '7', "|", '8', "|", '9')

#Player making there choice
def playersChoice():
    tmp = (int(input('Enter Your Choice : ')))
    if (lis[tmp - 1] == ' '):
        lis[tmp - 1] = 'X'
    else:
        print('\n*** Invalid Move ***\n')
        playersChoice()

#Generate random number
def ranGen():
    return random.randint(0,9)

#Computer making its choice
def compChoice():
    flg = 0
    if(isFull()):
        return
    else:
        winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in winners:
            if (lis[i[0]] == 'O' and lis[i[1]] == 'O' and lis[i[2]] == ' '):
                lis[i[2]] = 'O'
                flg = 1
                break
            elif (lis[i[0]] == 'O' and lis[i[2]] == 'O' and lis[i[1]] == ' '):
                lis[i[1]] = 'O'
                flg = 1
                break
            elif (lis[i[1]] == 'O' and lis[i[2]] == 'O' and lis[i[0]] == ' '):
                lis[i[0]] = 'O'
                flg = 1
                break
        if (flg == 0):
            for i in winners:
                if (lis[i[0]] == 'X' and lis[i[1]] == 'X' and lis[i[2]] == ' '):
                    lis[i[2]] = 'O'
                    flg = 1
                    break
                elif (lis[i[0]] == 'X' and lis[i[2]] == 'X' and lis[i[1]] == ' '):
                    lis[i[1]] = 'O'
                    flg = 1
                    break
                elif (lis[i[1]] == 'X' and lis[i[2]] == 'X' and lis[i[0]] == ' '):
                    lis[i[0]] = 'O'
                    flg = 1
                    break
        if (flg == 0):
            while (True):
                x = ranGen()
                if (lis[x - 1] == ' '):
                    lis[x - 1] = 'O'
                    break

#winning conditions
def win():
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for li in winners:
        if (lis[li[0]] == lis[li[1]] == lis[li[2]] and lis[li[2]] != ' '):
            if (lis[li[2]] == 'X'):
                return 'X'
            else:
                return 'O'

#To check IS FULL
def isFull():
    flg=1
    for i in lis:
        if(i==' '):
            flg=0
            break
    return flg

#Ask 1st or 2nd player
def whoWillGoFirst():
    c = input('Press : \nI - If you want to make first move \nC - If you want computer to make first move\n').upper()
    return c

#Player making first move
def plyFirst():
    while (True):
        playersChoice()
        compChoice()
        if (win() == 'X'):
            displayBoard()
            print('\n***** You Won *****')
            break
        if (win() == 'O'):
            displayBoard()
            print('\n***** You Lost *****')
            break
        if (isFull() == 1):
            displayBoard()
            print('\n***** Draw *****')
            break
        displayBoard()

#Computer making first move
def comFirst():
    compChoice()
    displayBoard()
    while (True):
        playersChoice()
        compChoice()
        if (win() == 'X'):
            displayBoard()
            print('\n***** You Won *****')
            break
        if (win() == 'O'):
            displayBoard()
            print('\n***** You Lost *****')
            break
        if (isFull() == 1):
            displayBoard()
            print('\n***** Draw *****')
            break
        displayBoard()


displaySampleBoard()
while(True):
    if(whoWillGoFirst() == 'I'):
        plyFirst()
    else:
        comFirst()
    if(input('\nPress : \nY - Rematch\nN - Exit\n').upper() == 'N' ):
        break
    else:
        lis = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


