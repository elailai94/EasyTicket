import sqlite3

connection = sqlite3.connect('easy_ticket.db')
cursor = connection.cursor()
print("Opened database successfully")

input_file = open('links.txt', 'r')
num_of_lines = int(input_file.readline().strip())

i = 0
while i < num_of_lines:
    connection_info = input_file.readline().strip().split(';')
    station_a = connection_info[0].strip()
    cursor.execute('SELECT * FROM station WHERE name = ?', (station_a,))
    station_a_row = cursor.fetchone()
    station_a_id = station_a_row[0]
    station_b = connection_info[1].strip()
    print(station_b);
    cursor.execute('SELECT * FROM station WHERE name = ?', (station_b,))
    station_b_row = cursor.fetchone()
    station_b_id = station_b_row[0]
    connection_distance = float(connection_info[2].strip())
    print(station_a_id, station_b_id, connection_distance)
    cursor.execute('INSERT INTO connection(station_a, station_b, distance) VALUES(?,?,?)', (station_a_id, station_b_id, connection_distance))
    connection.commit()
    i += 1

connection.close()
