import psycopg2

try:
    conn =psycopg2.connect(host="localhost",
    database="json_database",
    user="postgres",
    password="***123")

    print("Success")

except:
    print("I am unable to connect to the database") 

cur = conn.cursor()
try:
    cur.execute("CREATE TABLE IF NOT EXISTS json_data (id serial PRIMARY KEY, name varchar, price integer);")
except:
    print("cannot create database")

conn.commit()
cur.close()
conn.close()
