import psycopg2
import csv
import json

CSV_PATH = '/home/sumathi/json/myfile.csv'
JSON_PATH = '/home/sumathi/json/myfile.json'

#Reading the csv file
csv_file = csv.DictReader(open(CSV_PATH, 'r'))

# Created a list and adds the rows to the list
json_list = []
for row in csv_file:
    json_list.append(row)

# Writes the json output to the file
with open (JSON_PATH, 'w')as file:
    file.write(json.dumps(json_list))

connection = psycopg2.connect("host=localhost dbname=json_database user=postgres password=*****123")
cursor = connection.cursor()

fields = [
    'id',
    'name',
    'price'
]

# print(data)
print(json_list)

for item in json_list:
    my_data = [item[field] for field in fields]
    insert_query = "INSERT INTO json_table VALUES (%s, %s, %s)"
    cursor.execute(insert_query, tuple(my_data))
    connection.commit()

cursor.close()
connection.close()