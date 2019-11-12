import subprocess as sp
import pymysql
import pymysql.cursors
from functions import *

optionFunctionMapping = {
    1: registerNewUser,
    2: createPrivateLge,
    3: joinPrivateLge,
    4: deleteAccount,
    5: addPlayer,
    6: addClub,
    7: addLge,
    8: addMatch,
    9: addBest11,
    10: viewTopUsers,
    11: viewTopPlayers,
    12: viewTopClubs,
    13: chooseTeam,
    14: chooseClub,
    15: transferPlayerOut,
    16: transferPlayerIn,
    17: updatePlayer,
    18: updateClub,
    19: updateLge,
    20: updatePlayerRating,
    21: updateClubRating, 
    22: updateUserScores,
    23: showPrivateLeague,
    24: showUsersInPrivateLge,
    25: showAttackers,
    26: showMidfielders,
    27: showDefenders,
    28: showGoalies,
    29: userDetails

}

while(1):
    tmp = sp.call('clear',shell=True)
    username = 'newuser'
    password = 'password'

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='FANTASY',
                cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1: register new user")
                print("2: create private league")
                print("3: join private league")
                print("4: delete Account")
                print("5: add Player")
                print("6: add Club")
                print("7: add League")
                print("8: add Match")
                print("9: add Best 11")
                print("10: view Top Users")
                print("11: view Top Players")
                print("12: view Top Clubs")
                print("13: choose Team")
                print("14: choose Club")
                print("15: Transfer Out Player")
                print("16: Transfer In Player")
                print("17: update Player")
                print("18: update Club")
                print("19: update League")
                print("20: update player ratings")
                print("21: update club ratings")
                print("22: update user ratings")
                print("23: Show Private Leagues")
                print("24: Show users in private League")
                print("25: Show Attackers")
                print("26: Show Midfielders")
                print("27: Show Defenders")
                print("28: Show Goalkeepers")
                print("29: show user details")
                print("0: exit")
                c = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if c==0:
                    exit()
                else:
                    optionFunctionMapping[c](con, cur)
                tmp = input("Enter any key to CONTINUE>")


    except Exception as e:
        # tmp = sp.call('clear',shell=True)
        # print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        print(e)
        tmp = input("Enter any key to CONTINUE>")





