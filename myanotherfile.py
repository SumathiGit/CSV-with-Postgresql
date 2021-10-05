import pandas
import psycopg2
import json

df = pandas.read_csv('myfile.csv')
print(df)
result = df.to_json('mynew.json', orient='records')


myjsonlist = []
with open('mynew.json') as f:
    for line in f:
        myjsonlist = json.loads(line) #returns a json object

print(type(myjsonlist)) #list


connection = psycopg2.connect("host=localhost dbname=json_database user=postgres password=*****123")
cursor = connection.cursor()

fields = [
    'id',
    'name',
    'price'
]

# print(data)
print(myjsonlist)

for item in myjsonlist:
    my_data = [item[field] for field in fields]
    insert_query = "INSERT INTO json_data VALUES (%s, %s, %s)"
    cursor.execute(insert_query, tuple(my_data))
    connection.commit()

cursor.close()
connection.close()