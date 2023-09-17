from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='cybr41018!',
                                 host='127.0.0.1',
                                 database='pysports')



team_cursor = cnx.cursor()

team_cursor.execute('SELECT team_id, team_name, mascot FROM team')
teams= team_cursor.fetchall()



for team in teams:
    print('Team ID: {}'.format(team[0]))
    print('Team Name: {}'.format(team[1]))
    print('Mascot: {}'.format(team[2]))
    print()


player_cursor= cnx.cursor()

player_cursor.execute('SELECT player_id, first_name, last_name, team_id FROM player')
players= player_cursor.fetchall()

for player in players:
    print('Player ID: {}'.format(player[0]))
    print('First Name: {}'.format(player[1]))
    print('Last Name: {}'.format(player[2]))
    print('Team ID: {}'.format(player[3]))
    print()


cnx.close()    
input('Click something to exit') 

