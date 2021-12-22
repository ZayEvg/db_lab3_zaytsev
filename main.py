import psycopg2
import matplotlib.pyplot as plt

#  поля заповнити власними значеннями
username = ''
password = ''
database = ''
host = ''
port = '5432'

query1 = '''
CREATE VIEW SupportFeatures AS
SELECT pers_feature, COUNT(*) AS feature_count
FROM Personage
WHERE pers_main_role = 'Support'
GROUP BY pers_main_role, pers_feature
ORDER BY pers_main_role
'''

query2 = '''
CREATE VIEW PersFeaturesCount AS
SELECT pers_feature, COUNT(*) AS feature_count
FROM Personage
GROUP BY pers_feature
ORDER BY pers_feature
'''

query3 = '''
CREATE VIEW PersWeaponCount AS
SELECT pers_weapon, COUNT(*) AS weapon_count
FROM Personage
GROUP BY pers_weapon
ORDER BY pers_weapon
'''

connct = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with connct:
    curr_lane = connct.cursor()

    curr_lane.execute('DROP VIEW IF EXISTS SupportFeatures')
    curr_lane.execute(query1)
    curr_lane.execute('SELECT * FROM SupportFeatures')
    x_lst = []
    y_lst = []
    for row in curr_lane:
        x_lst.append(row[0].replace(' ', ''))
        y_lst.append(row[1])
    plt.title("Стихии героев поддержки")
    plt.bar(x_lst, y_lst, color='limegreen')
    plt.show()

    curr_lane.execute('DROP VIEW IF EXISTS PersFeaturesCount')
    curr_lane.execute(query2)
    curr_lane.execute('SELECT * FROM PersFeaturesCount')
    x_lst = []
    y_lst = []
    for row in curr_lane:
        x_lst.append(row[0].replace(' ', ''))
        y_lst.append(row[1])
    plt.title("Герои разных стихий")
    plt.pie(y_lst, labels=x_lst,
            colors=['blueviolet', 'gold', 'royalblue', 'orangered'])
    plt.show()

    curr_lane.execute('DROP VIEW IF EXISTS PersWeaponCount')
    curr_lane.execute(query3)
    curr_lane.execute('SELECT * FROM PersWeaponCount')
    x_lst = []
    y_lst = []
    for row in curr_lane:
        x_lst.append(row[0].replace(' ', ''))
        y_lst.append(row[1])
    plt.title("Герои с разным оружием")
    plt.bar(x_lst, y_lst, color='lightsteelblue')
    plt.show()
