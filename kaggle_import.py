import psycopg2
import csv

#  поля заповнити власними значеннями
username = ''
password = ''
database = ''
host = ''
port = '5432'
file_name = 'Genshin_Impact_All_Character_Stat.csv'
tables = [
    'Personage',
    'Weapon',
    'Feature',
    'Main_role'
]

query1 = '''
DROP TABLE IF EXISTS Personage_new
'''

query2 = '''
CREATE TABLE Personage_new
(
	pers_name		char(30) NOT NULL,
	pers_weapon		char(20) NOT NULL,
	pers_feature	char(20) NOT NULL,
	pers_main_role	char(20) NULL,
	CONSTRAINT PK_Personage_new PRIMARY KEY (pers_name)
);
'''

query3 = '''
DELETE FROM Personage_new
'''

query4 = '''
INSERT INTO Personage_new(pers_name, pers_weapon, pers_feature, pers_main_role) 
VALUES(%s, %s, %s, %s)
'''

connct = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with connct:
    curr_lane = connct.cursor()
    curr_lane.execute(query1)
    curr_lane.execute(query2)
    curr_lane.execute(query3)
    with open(file_name, 'r') as file:
        my_reader = csv.DictReader(file)
        prev_row = []
        for row in my_reader:
            if prev_row == row['Character']:
                continue
            else:
                values = (row['Character'],
                          row['Weapon'],
                          row['Element'],
                          row['Main role']
                          )
                prev_row = row['Character']
            curr_lane.execute(query4, values)
    connct.commit()
file.close()
