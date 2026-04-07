import sqlite3 , re
conn = sqlite3.connect('aviation.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS planes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    max_speed INT,
    fuel_consumption REAL,
    category TEXT
    )
""")
cursor.execute('DELETE from planes')
def regexp(expr,db_text):
    reg = re.compile(expr)
    return reg.search(db_text) is not None
conn.create_function('REGEXP',2,regexp)
planes_config_list = [['Boeing 747',950,12000,'Commercial'],['Boeing 737',880,3000,'Commercial'],
                      ['Cessna 560',796,3050,'Private'],['Cessna 172',233,37,'Private'],
                      ['Airbus A320',870,2700,'Commercial'],['AH-124',865,15750,'Cargo']]
for config in planes_config_list:
    cursor.execute('INSERT INTO planes (model,max_speed,fuel_consumption,category) VALUES (?,?,?,?)'
                   ,(config[0],config[1],config[2],config[3]))
not_boeing_models = cursor.execute('SELECT model FROM planes WHERE model NOT REGEXP "^Boeing" ')
for not_boeing in not_boeing_models:
    print(not_boeing[0])
specific_categories = conn.execute('SELECT category,AVG(fuel_consumption),COUNT(model) FROM planes GROUP BY category HAVING AVG(fuel_consumption) > 500')
for kind in specific_categories:
    print(kind)
cursor.execute('DELETE FROM planes WHERE max_speed < 250')
cursor.execute('UPDATE planes SET model = ? WHERE model = "Cessna 560" ',('Cessna_V2',))
cursor.execute('SELECT * FROM planes ORDER BY fuel_consumption DESC')
for plane in cursor.fetchall():
    print(plane)
conn.commit()
conn.close()
