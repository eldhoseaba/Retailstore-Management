import mysql.connector
try:
	mydb=mysql.connector.connect(host='localhost',user='root',password='root@123',port=3306)
	cursor=mydb.cursor()
	'''cursor.execute("CREATE DATABASE Productsbook")'''
	mydb=mysql.connector.connect(host='localhost',user='root',password='root@123',port=3306,database='Productsbook')
	cursor.mydbcursor()
	cursor.execute("CREATE TABLE prdct(Name varchar(25),Category varchar(50),Price bigint(10),image varchar(100))")
except:
	mydb=mysql.connector.connect(host='localhost',user='root',password='root@123',port=3306,database='Productsbook')
	cursor=mydb.cursor()