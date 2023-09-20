import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user='root2',
passwd='cybr41018!',
db='pysports')

def display_results(x):

    for x in rows:  
        print('Player ID: {}'.format(x[0]))
        print('First Name: {}'.format(x[1]))
        print('Last Name: {}'.format(x[2]))
        print('Team Name: {}'.format(x[3]))
        print()
    
'''INNER JOIN FOR CORRECT FORMAT'''
cursor = connection.cursor()
query="SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id=team.team_id"

cursor.execute(query)
rows=cursor.fetchall()


'''INSERT NEW PLAYER'''
insert_sql = "INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
new_player= ("021", "Smeagol", "Shire Folk", "1")
cursor.execute(insert_sql,new_player)
connection.commit()

print('--DISPLAYING PLAYERS AFTER INSERT--')
display_results(insert_sql)


'''UPDATE PLAYER''' 

print('DISPLAYING PLAYERS AFTER UPDATE')
update_sql= "UPDATE player SET player_id= '21', team_id='2' WHERE first_name='Smeagol'"

display_results(update_sql)

'''DELETE PLAYER'''

print("--DISPLAYING PLAYERS AFTER DELETE")
delete_player= "DELETE FROM player WHERE first_name='Smeagol'"

display_results(delete_player)


connection.close()

input("Click to continue...")