import sqlite3
conn = sqlite3.connect('test.db')
print("Opend database successfully!")

conn.execute("CREATE TABLE CONTACT (NAME TEXT,PHONE_NUMBER INT PRIMARY KEY,ADDRESS CHAR(50))")
print("Table created successfully")
conn.close()
