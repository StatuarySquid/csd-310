import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user='root2',
passwd='cybr41018!',
db='pysports')

cursor = connection.cursor()


def display_results(query):
    query="SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id=team.team_id"
    cursor.execute(query)
    rows=cursor.fetchall()
    for query in rows:  
        print('Player ID: {}'.format(query[0]))
        print('First Name: {}'.format(query[1]))
        print('Last Name: {}'.format(query[2]))
        print('Team Name: {}'.format(query[3]))
        print()
    

'''INSERT NEW PLAYER'''
insert_sql = "INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
new_player= ("021", "Smeagol", "Shire Folk", "1")
cursor.execute(insert_sql,new_player)


print('--DISPLAYING PLAYERS AFTER INSERT--')
display_results(insert_sql)


'''UPDATE PLAYER''' 

print('DISPLAYING PLAYERS AFTER UPDATE')
update_sql= "UPDATE player SET player_id= '21',first_name='Gollum', last_name='Ring Stealer', team_id='2' WHERE first_name='Smeagol'"

cursor.execute(update_sql)

display_results(update_sql)

'''DELETE PLAYER'''

print("--DISPLAYING PLAYERS AFTER DELETE")
delete_player= "DELETE FROM player WHERE first_name='Gollum'"

cursor.execute(delete_player)

display_results(delete_player)


connection.close()

input("Click to continue...")