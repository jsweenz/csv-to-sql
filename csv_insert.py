"""
This python script takes in the path to a csv file and converts each row
of the csv file to a SQL INSERT command and writes it to a specified 
.sql file. 

Requirements:
- the .sql file must already exist at the specified directory path
- the CSV file must contain no spaces before or after the commas
- the second row of the CSV fiule must contain the <type> of the value
  such as str for string, int for integer. int is the only important 
  value currently.

to run the command:
$ python csv_insert.py <csv file path> <destination .sql file path> <sql table name>
"""
import csv
import sys
sql_file = open(sys.argv[2], "w")
table_name = sys.argv[3]
with open(sys.argv[1], "r") as table:
    reader =  csv.reader(table, delimiter=',')
    header_values = next(reader)
    types = next(reader)
    for row in reader:
        entry = row
        sql_command = "INSERT INTO \'" + table_name + "\' VALUES ("
        for x in range(len(entry)-1):
            if types[x] == 'int':
                sql_command+= entry[x] +","
            else:
                sql_command+= "\'"+ entry[x] +"\',"
        sql_command = sql_command[:-1]
        sql_command+=")"
        sql_file.write(sql_command + "\n")
sql_file.close()
