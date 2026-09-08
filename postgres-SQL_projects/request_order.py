cursor.execute("""SELECT users_data.username,
                      SUM(products_data.price) as total_expense,
                      ROUND(AVG(products_data.price)) as average_price
                      FROM users_data                      
                      INNER JOIN products_data ON users_data.id = products_data.user_id
                      WHERE products_data.price >= 300
                      GROUP BY users_data.username 
                      HAVING SUM(products_data.price) > 2000
                      ORDER BY total_expense DESC;
    """)

#1)first of all we select desirable things 
#2)Then we use Agg-functions and making them as variables 
#3)Then we Took it from main table(users_data)
#4)Then we JOIN two tables
#5)We sort raw values using WHERE 
#6)We group products by username
#7)Than we sort agg-values using HAVING
#8)in the end we ORDER them using DESC(or ASC)

#print(cursor.fetchall())
