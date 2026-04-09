import sqlite3 , re
conn = sqlite3.connect('layout.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS planes')
cursor.execute("""CREATE TABLE IF NOT EXISTS planes(
    plane_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    max_range REAL
)""")
cursor.execute('DROP TABLE IF EXISTS flights')
cursor.execute("""CREATE TABLE IF NOT EXISTS flights(
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    destination TEXT, 
    distance REAL,
    assigned_flight_id INTEGER,
    FOREIGN KEY (assigned_flight_id) REFERENCES planes (plane_id)
)""")
planes_data = [('Boeing 747', 13000), ('Cessna 172', 1200), ('Airbus A320', 6000),('Airbus A220',6200)]
cursor.executemany('INSERT INTO planes (model,max_range) VALUES (?,?)',planes_data)
flights_data = [('Moscow', 1100, 2),('Paris', 2500, 3),('New York', 7500, 1),
    ('Tokyo', 9000, 4),('London', 2500, 3),('Anapa', 1500, 2),('Madrid', 3500, 1), ('Dubai', 4000, 3)]
cursor.executemany('INSERT INTO flights (destination,distance,assigned_flight_id) VALUES (?,?,?)',flights_data)
cursor.execute("""SELECT planes.model , planes.max_range , flights.destination , flights.distance , 
               CASE 
               WHEN planes.max_range > flights.distance THEN 'ALLOWED'
               ELSE '!ENDANGERED!'
               END AS status FROM flights
               JOIN planes ON flights.assigned_flight_id = planes.plane_id""")
for row in cursor.fetchall():
    print(f'plane model: {row[0]} / max range: {row[1]} / destination: {row[2]} / flight distance: {row[3]} / status: {row[4]}')
cursor.execute("""SELECT planes.model, COUNT(flights.destination) FROM flights 
               JOIN planes ON flights.assigned_flight_id = planes.plane_id
               GROUP BY planes.model 
               ORDER BY COUNT(flights.destination) DESC""")
for counter in cursor.fetchall():
    print(counter)
def regexp(expr,db_text):
    reg = re.compile(expr)
    return reg.search(db_text) is not None
conn.create_function('REGEXP',2,regexp)
cursor.execute('DELETE FROM flights WHERE destination REGEXP "^[AM]" ')
conn.commit()
conn.close()
