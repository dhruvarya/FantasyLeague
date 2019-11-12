import subprocess as sp
import pymysql
import pymysql.cursors

def registerNewUser(con, cur):
    # global cur
    row = {}
    print("Enter new user's details: ")
    name = (input("Name (Fname Lname): ")).split(' ')
    row["Fname"] = name[0]
    row["Lname"] = name[1]
    row["dob"] = input("Birth Date (YYYY-MM-DD): ")
    row["Capt Player Id"] = int(input("Capt Player Id: "))
    row["current total points"] = int(0)
    row["money_left"] = int(250)
    query = "INSERT INTO `User` VALUES('%s', '%s', 0, %d, %d, %d, '%s')" %(row["Fname"], row["Lname"], row["Capt Player Id"], row["current total points"], row["money_left"], row["dob"])

    cur.execute(query)
    con.commit()
    print("user created")
    return

def createPrivateLge(con, cur):
    # global cur

    query = "INSERT INTO `private_league` VALUES(0)"

    cur.execute(query)
    con.commit()
    print("created private league")
    return

def showPrivateLeague(con, cur):
    print("printing all private leagues")
    query = "SELECT * FROM private_league"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    # print(rows)
    print("Private League Id")
    for row in rows:
        print("'%s'" % (row["pl_id"]))
    return

def showUsersInPrivateLge(con, cur):
    pl_id = int(input("Enter pl id: "))
    query = "SELECT A.first_name, A.last_name, A.current_total_points FROM user_pl_relation AS B INNER JOIN User AS A WHERE A.user_id = B.user_id AND B.pl_id = '%d'" % (pl_id)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    # print(rows)
    print("Private League Id '%d'" % (pl_id))
    for row in rows:
        # print(row)
        print("'%s' '%s' '%s'" % (row["first_name"], row["last_name"], row["current_total_points"]))
    return

def joinPrivateLge(con, cur):
    # global cur
    row = {}
    row["user_id"] = int(input("User_id: "))
    row["pl_id"] = int(input("Enter priv league id: "))
    query = "INSERT INTO `user_pl_relation` VALUES(%d, %d)" %(row["user_id"], row["pl_id"])

    cur.execute(query)
    con.commit()
    print("joined private league")
    return

def deleteAccount(con, cur):
    # global cur
    row = {}
    row["user_id"] = int(input("Enter User id: "))
    query = "DELETE FROM user_pl_relation WHERE user_id=%d"%(row["user_id"])
    cur.execute(query)
    con.commit()
    query = "DELETE FROM user_player_relation WHERE user_id=%d"%(row["user_id"])
    cur.execute(query)
    con.commit()
    query = "DELETE FROM user_club_relation WHERE user_id=%d"%(row["user_id"])
    cur.execute(query)
    con.commit()
    query = "DELETE FROM `User` WHERE user_id=%d" %(row["user_id"])
    cur.execute(query)
    con.commit()
    print("user deleted")
    return

def addPlayer(con, cur):
    # global cur
    row = {}
    print("Enter new player's details: ")
    row["name"] = input("Name: ")
    row["age"] = int(input("age: "))
    row["country"] = input("country: ")
    row["club_id"] = int(input("club id: "))
    row["rating"] = int(input("rating: "))
    row["price"] = int(input("price: "))
    row["type"] = input("Type (a, m, d, g) : ")

    query = "INSERT INTO `football_player` VALUES (0, '%d', '%d', '%d', '%s', '%s','%d')" %(row["price"], row["club_id"], row["rating"], row["country"], row["name"], row["age"])
    cur.execute(query)
    con.commit()
    query = "SELECT player_id FROM football_player ORDER BY player_id DESC LIMIT 1"
    cur.execute(query)
    con.commit()
    newrow = cur.fetchall()
    print(newrow)
    player_id = 0
    for r in newrow:
        player_id = r['player_id']
    if row["type"] == 'a':
        goals = int(input("Goals : "))
        query = "INSERT INTO `attacker` VALUES (%d, %d)" %(player_id, goals)
        cur.execute(query)
        con.commit()
    if row["type"] == 'd':
        tackles = int(input("Tackles : "))
        query = "INSERT INTO `defender` VALUES (%d, %d)" %(player_id, tackles)
        cur.execute(query)
        con.commit()

    if row["type"] == 'm':
        passes = int(input("Passes : "))
        query = "INSERT INTO `midfielder` VALUES (%d, %d)" %(player_id, passes)
        cur.execute(query)
        con.commit()

    if row["type"] == 'g':
        saves = int(input("Saves : "))
        query = "INSERT INTO `goalkeeper` VALUES (%d, %d)" %(player_id, saves)
        cur.execute(query)
        con.commit()


    print("player added")
    return

def showAttackers(con, cur):
    query = "SELECT B.name, A.goals FROM attacker A, football_player B WHERE A.player_id = B.player_id"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    print("player_id\tgoals\n")
    for row in rows:
        print("'%s'\t'%s'" % (row['name'], row['goals']))

def showDefenders(con, cur):
    query = "SELECT B.name, A.tackles FROM defender A, football_player B WHERE A.player_id = B.player_id"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    print("player_id\tdefenders\n")
    for row in rows:
        print("'%s'\t'%s'" % (row['name'], row['tackles']))

def showMidfielders(con, cur):
    query = "SELECT B.name, A.passes FROM midfielder A, football_player B WHERE A.player_id = B.player_id"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    print("player_id\tpasses\n")
    for row in rows:
        print("'%s'\t'%s'" % (row['name'], row['passes']))

def showGoalies(con, cur):
    query = "SELECT B.name, A.saves FROM goalkeeper A, football_player B WHERE A.player_id = B.player_id"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    print("player_id\tsaves\n")
    for row in rows:
        print("'%s'\t'%s'" % (row['name'], row['saves']))

def addClub(con, cur):
    # global cur
    row = {}
    print("Enter new club's details: ")
    row["club_name"] = input("enter club name: ")
    row["club_crest"] = input("club crest: ")
    row["club_rating"] = int(input("club ratings: "))
    row["league_id"] = int(input("League Id: "))

    query = "INSERT INTO `football_club` VALUES (0, '%s', '%s', %d, %d)" %(row["club_name"], row["club_crest"], row["club_rating"], row["league_id"])
    cur.execute(query)
    con.commit()
    print("club added")
    return

def addLge(con, cur):
    # global cur
    row = {}
    print("Enter new league's details: ")
    row["name"] = input("leauge name: ")
    row["country"] = input("league country: ")

    query = "INSERT INTO `league` VALUES (0, '%s', '%s')" %(row["name"], row["country"])
    cur.execute(query)
    con.commit()
    print("league added")
    return

def addMatch(con, cur):
    # global cur
    row = {}
    print("Enter new match's details: ")
    row["club_1_id"] = int(input("enter club id1: "))
    row["club_2_id"] = int(input("enter club id2: "))
    row["match_date"] = input("Match Date (YYYY-MM-DD): ")
    row["club_1_points"] = int(input("enter club1 points: "))
    row["club_2_points"] = int(input("enter club2 points: "))
    row["match_week"] = int(input("enter match week : "))

    query = "INSERT INTO `match` VALUES (%d, %d, '%s', %d, %d, %d)" %(row["club_1_id"], row["club_2_id"], row["match_date"], row["club_1_points"], row["club_2_points"], row["match_week"])

    cur.execute(query)
    con.commit()
    print("match added")
    return

def addBest11(con, cur):
    # global cur
    row = {}
    print("Enter best11 player's details: ")
    row["match_week"] = int(print("enter matchweek: "))
    print("Enter goalkeeper player_id")
    row["goal_id"] = int(input("enter goalkeeper player_id: "))
    print("Enter 4 defenders")
    row["def_1"] = int(input("enter defender 1: "))
    row["def_2"] = int(input("enter defender 2: "))
    row["def_3"] = int(input("enter defender 3: "))
    row["def_4"] = int(input("enter defender 4: "))
    print("Enter 3 midfielders")
    row["mid_1"] = int(input("enter midfielder 1: "))
    row["mid_2"] = int(input("enter midfielder 2: "))
    row["mid_3"] = int(input("enter midfielder 3: "))
    print("Enter 3 attackers")
    row["att_1"] = int(input("enter attacker 1: "))
    row["att_2"] = int(input("enter attacker 2: "))
    row["att_3"] = int(input("enter attacker 3: "))
    query = "INSERT INTO Best11(match_week) VALUES('%d')"%(match_week)
    cur.execute(query)
    con.commit()
    query = "INSERT INTO best11_gkp(match_week, player_id) VALUES('%d', '%d')"%(match_week, row["goal_id"])
    cur.execute(query)
    con.commit()

    for i in range(1, 5):
        query = "INSERT INTO best11_def(match_week, player_id) VALUES('%d', '%d')"%(match_week, row["def_"+str(i)])
        cur.execute(query)
        con.commit()
    for i in range(1, 4):
        query = "INSERT INTO best11_mid(match_week, player_id) VALUES('%d', '%d')"%(match_week, row["mid_"+str(i)])
        cur.execute(query)
        con.commit()
    for i in range(1, 4):
        query = "INSERT INTO best11_att(match_week, player_id) VALUES('%d', '%d')"%(match_week, row["att_"+str(i)])
        cur.execute(query)
        con.commit()
    return

def viewTopUsers(con, cur):
    # global cur
    limit = int(input("Enter Number of Top Users : "))
    query = "SELECT * FROM User ORDER BY current_total_points DESC LIMIT %d"%(limit)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    # print(rows)
    print("UserId UserName current_total_points")
    for row in rows:
        print("'%s' '%s' '%s' '%s'" % (row["user_id"], row["first_name"], row["last_name"], row["current_total_points"]))
    return

def viewTopPlayers(con, cur):
    # global cur
    limit = int(input("Enter Number of Top Players : "))
    query = "SELECT * FROM football_player ORDER BY rating DESC LIMIT %d"%(limit)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    # print(rows)
    print("PlayerId PlayerName PlayerRating ClubId")
    for row in rows:
        print("'%s' '%s' '%s' '%s'" % (row["player_id"], row["name"], row["rating"], row["club_id"]))
    return

def viewTopClubs(con, cur):
    # global cur
    limit = int(input("Enter Number of Top Clubs : "))
    query = "SELECT * FROM football_club ORDER BY club_rating DESC LIMIT %d"%(limit)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    # print(rows)
    print("ClubId ClubName ClubRating LeagueId")
    for row in rows:
        print("'%s' '%s' '%s' '%s'" % (row["club_id"], row["club_name"], row["club_rating"], row["league_id"]))
    
    return

def chooseTeam(con, cur):
    # global cur
    row = {}
    user_id = int(input("Enter User ID : "))
    query = "SELECT money_left FROM User WHERE user_id = '%d'" % (user_id)
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    curr_price = int(newrows[0]["money_left"])
    print("you have '%d' money left" % (curr_price))
    print("Enter team's details: ")
    price = int(0)
    
    row["goal_id"] = int(input("enter goalkeeper player_id: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM goalkeeper) AND player_id = '%d'" % (row["goal_id"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such goalkeeper exists")
        return
    price = price + int(newrows[0]["price"])


    print("Enter 4 defenders")
    row["def_1"] = int(input("enter defender 1: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM defender) AND player_id = '%d'" % (row["def_1"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such defender exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["def_2"] = int(input("enter defender 2: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM defender) AND player_id = '%d'" % (row["def_2"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such defender exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["def_3"] = int(input("enter defender 3: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM defender) AND player_id = '%d'" % (row["def_3"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such defender exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["def_4"] = int(input("enter defender 4: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM defender) AND player_id = '%d'" % (row["def_4"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such defender exists")
        return
    price = price + int(newrows[0]["price"])
    

    print("Enter 3 midfielders")
    row["mid_1"] = int(input("enter midfielder 1: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM midfielder) AND player_id = '%d'" % (row["mid_1"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such midfielder exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["mid_2"] = int(input("enter midfielder 2: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM midfielder) AND player_id = '%d'" % (row["mid_2"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such midfielder exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["mid_3"] = int(input("enter midfielder 3: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM midfielder) AND player_id = '%d'" % (row["mid_3"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such midfielder exists")
        return
    price = price + int(newrows[0]["price"])

    print("Enter 3 attackers")
    row["att_1"] = int(input("enter attacker 1: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM attacker) AND player_id = '%d'" % (row["att_1"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such attacker exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["att_2"] = int(input("enter attacker 2: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM attacker) AND player_id = '%d'" % (row["att_2"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such attacker exists")
        return
    price = price + int(newrows[0]["price"])
    

    row["att_3"] = int(input("enter attacker 3: "))
    query = "SELECT price FROM football_player WHERE player_id IN (SELECT player_id FROM attacker) AND player_id = '%d'" % (row["att_3"])
    cur.execute(query)
    con.commit()
    newrows = cur.fetchall()
    if(len(newrows) == 0):
        print("No such attacker exists")
        return
    price = price + int(newrows[0]["price"])

    if price > curr_price:
        print("you don't have enough money")
        return
    

    query = "INSERT INTO user_player_relation(user_id, player_id) VALUES('%d', '%d')"%(user_id, row["goal_id"])
    cur.execute(query)
    con.commit()
    for i in range(1, 5):
        query = "INSERT INTO user_player_relation(user_id, player_id) VALUES('%d', '%d')"%(user_id, row["def_"+str(i)])
        cur.execute(query)
        con.commit()
    for i in range(1, 4):
        query = "INSERT INTO user_player_relation(user_id, player_id) VALUES('%d', '%d')"%(user_id, row["mid_"+str(i)])
        cur.execute(query)
        con.commit()
    for i in range(1, 4):
        query = "INSERT INTO user_player_relation(user_id, player_id) VALUES('%d', '%d')"%(user_id, row["att_"+str(i)])
        cur.execute(query)
        con.commit()

    print("team selected")
    print("money left: ", curr_price - price)
    query = "UPDATE User SET money_left = money_left - '%d' WHERE user_id = '%d'" % (price, user_id)
    cur.execute(query)
    con.commit()
    return

def chooseClub(con, cur):
    # global cur
    user_id = int(input("Enter User ID: "))
    club_id = int(input("Enter Club ID: "))
    query = "INSERT INTO user_club_relation(user_id, club_id) VALUES('%d', '%d') ON DUPLICATE KEY UPDATE club_id = '%d'" %(user_id, club_id, club_id)
    cur.execute(query)
    con.commit()
    return

def transferPlayerOut(con, cur):
    # global cur
    user_id = int(input("User ID : "))
    player_id = int(input("Player ID : "))

    query = "DELETE FROM user_player_relation WHERE player_id = '%d' AND user_id = '%d'" %(player_id, user_id)    
    cur.execute(query)
    con.commit()

    query = "SELECT price FROM football_player WHERE player_id = '%d'" % (player_id)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    player_price = int(rows[0]["price"])
    print("%d added to your account" % player_price)
    query = "UPDATE User SET money_left = money_left + '%d' WHERE user_id = '%d'" % (player_price, user_id)
    cur.execute(query)
    con.commit()
    return

def transferPlayerIn(con, cur):
    # global cur
    user_id = int(input("User ID : "))
    player_id = int(input("Player ID : "))

    query = "SELECT price FROM football_player WHERE player_id = '%d'" % (player_id)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    player_price = int(rows[0]["price"])

    query = "SELECT money_left FROM User WHERE user_id = '%d'" % (user_id)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    user_price = int(rows[0]["money_left"])


    if player_price > user_price:
        print("you don't have enought money in your account" % player_price)
    
    query = "UPDATE User SET money_left = money_left - '%d' WHERE user_id = '%d'" % (player_price, user_id)
    cur.execute(query)
    con.commit()

    query = "INSERT INTO user_player_relation(user_id, player_id) VALUES('%d', '%d')" %(user_id, player_id)

    cur.execute(query)
    con.commit()

    print("player added to your squad")

    return


def updatePlayer(con, cur):
    # global cur
    row = {}
    print("Enter updated player's details: ")
    player_id = int(input("Enter Player ID : "))
    price = int(input("Price : "))
    club_id = int(input("Club ID :"))
    ranking = int(input("Ranking : "))
    country = input("Country : ")
    name = input("Name : ")
    age = int(input("Age :"))

    query = "UPDATE football_player SET price = '%d', club_id = '%d' , ranking = '%d', country = '%d', name ='%s', age='%d' WHERE player_id = '%d'" %(price, club_id, ranking, country, name, age, player_id)

    cur.execute(query)
    con.commit()
    return

def updateClub(con, cur):
    # global cur
    print("Enter club's details: ")
    club_id = int(input("Id: "))
    club_name = (input("Name : "))
    club_crest = (input("Crest : "))
    club_rating = int(input("Rating : "))
    league_id = int(input("League Id : "))
    query = "UPDATE football_club SET club_name = '%s', club_crest = '%s', club_rating = '%d', league_id = '%d' WHERE club_id = '%d'" %(club_name, club_crest, club_rating, league_id, club_id)

    cur.execute(query)
    con.commit()
    return

def updateLge(con, cur):
    # global cur
    row = {}
    print("Enter updated league's details: ")
    league_id = int((input("League ID : ")))
    country = input("Country: ")
    league_name = (input("League Name : "))

    query = "UPDATE league SET country = '%s', name = '%s' WHERE league_id = '%d'" %(country, league_name, league_id)

    cur.execute(query)
    con.commit()
    return

def updatePlayerRating(con, cur):
    # global cur
    row = {}
    print("Update Players ratings: ")
    player_id = (input("Player id: "))
    new_rating  = (input("New Rating: "))
    query = "UPDATE football_player SET rating = '%d' WHERE player_id = '%d'" %(int(new_rating), int(player_id))
    cur.execute(query)
    con.commit()
    return

def updateClubRating(con, cur):
    print("Update club's ratings: ")
    club_id = input("club id: ")
    new_rating  = (input("New Club Rating: "))
    query = "UPDATE football_club SET rating = '%d' WHERE club_id = '%d'" %(int(new_rating), int(club_id))
    cur.execute(query)
    con.commit()
    return

def updateUserScores(con, cur):
    print("Update user's total_score")
    user_id = int(input("user id: "))
    query = "SELECT SUM(B.rating) FROM user_player_relation A, football_player B WHERE A.player_id = B.player_id AND A.user_id = '%d'" % (user_id)
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    print(rows)
    new_rating = int(rows[0]["SUM(B.rating)"])
    query = "UPDATE User SET current_total_points = current_total_points + '%d' WHERE user_id = '%d'" %(new_rating, user_id)	
    cur.execute(query)
    con.commit()
    return
