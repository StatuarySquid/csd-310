import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user='root2',
passwd='cybr41018!',
db='pysports')




cursor = connection.cursor()

query="SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id=team.team_id"

join=cursor.execute(query)
rows=cursor.fetchall()

print('--DISPLAYING PLAYING RECORDS--')
for join in rows:
    print('Player ID: {}'.format(join[0]))
    print('First Name: {}'.format(join[1]))
    print('Last Name: {}'.format(join[2]))
    print('Team Name: {}'.format(join[3]))
    print()

connection.close()

input('Press  any key continue...')
