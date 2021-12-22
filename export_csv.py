import psycopg2
import csv

#  поля заповнити власними значеннями
username = ''
password = ''
database = ''
host = ''
port = ''
file_name = 'Zaytsev_DB_{}.csv'
tables = [
    'Personage',
    'Weapon',
    'Feature',
    'Main_role'
]

connct = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with connct:
    curr_lane = connct.cursor()
    for table_name in tables:
        curr_lane.execute('SELECT * FROM ' + table_name)
        fields = [el[0] for el in curr_lane.description]

        with open(file_name.format(table_name), 'w') as output_file:
            my_writer = csv.writer(output_file)
            my_writer.writerow(fields)
            for row in curr_lane:
                my_writer.writerow([str(el).lstrip() for el in row])
        output_file.close()
