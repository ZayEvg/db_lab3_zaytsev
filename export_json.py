import psycopg2
import json

#  поля заповнити власними значеннями
username = ''
password = ''
database = ''
host = ''
port = ''
file_name = 'Zaytsev_DB.json'
tables = [
    'Personage',
    'Weapon',
    'Feature',
    'Main_role'
]
my_data = {}
connct = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with connct:
    curr_lane = connct.cursor()
    for table_name in tables:
        curr_lane.execute('SELECT * FROM ' + table_name)
        rows = []
        fields = [el[0] for el in curr_lane.description]
        for row in curr_lane:
            rows.append(dict(zip(fields, row)))
        my_data[table_name] = rows

with open(file_name, 'w') as output_file:
    json.dump(my_data, output_file, default=str)
output_file.close()
