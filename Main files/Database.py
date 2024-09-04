#defining the function for the database
def database():
	#SQL and databases section
	import sqlite3
	from sqlite3 import Error

	#defining connection and cursor
	filename="users.db"
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()

	#Converting images to Blob from JPEG and storing under a variable name
	with open('Main files\Images\Lamp.jpg','rb') as f:
		Lamp=f.read()

	with open('Main files\Images\Chair.jpg','rb') as f:
		Chair=f.read()
		
	with open('Main files\Images\Sofa.jpg','rb') as f:
		Sofa=f.read()

	with open('Main files\Images\Harry_potter.jpg','rb') as f:
		Harry_potter=f.read()

	with open('Main files\Images\Great_gatsby.jpg','rb') as f:
		Great_gatsby=f.read()

	with open('Main files\Images\Empireland.jpg','rb') as f:
		Empireland=f.read()

	with open('Main files\Images\Blue_jeans.jpg','rb') as f:
		Blue_jeans=f.read()

	with open('Main files\Images\Blue_jeans.jpg','rb') as f:
		Blue_jeans=f.read()

	with open('Main files\Images\White_tee.jpg','rb') as f:
		White_tee=f.read()

	with open('Main files\Images\Brown_hoodie.jpg','rb') as f:
		Brown_hoodie=f.read()

	with open('Main files\Images\Interstella.jpg','rb') as f:
		Interstella=f.read()

	with open('Main files\Images\Minecraft.jpg','rb') as f:
		Minecraft=f.read()

	with open('Main files\Images\Damn.jpg','rb') as f:
		Damn=f.read()

	with open('Main files\Images\Kitchen_knife.jpg','rb') as f:
		Kitchen_knife=f.read()

	with open('Main files\Images\Garlic_press.jpg','rb') as f:
		Garlic_press=f.read()

	with open('Main files\Images\Tin_opener.jpg','rb') as f:
		Tin_opener=f.read()
		
	with open('Main files\Images\Laptop.jpg','rb') as f:
		Laptop=f.read()

	with open('Main files\Images\Iphone.jpg','rb') as f:
		Iphone=f.read()

	with open('Main files\Images\Wireless_ear_buds.jpg','rb') as f:
		Wireless_ear_buds=f.read()

	#defining and creating tables
	#creating user table
	Users_table=('''CREATE TABLE IF NOT EXISTS
		Users_table(User_ID INTEGER PRIMARY KEY,
		Username TEXT,
		Password TEXT,
		Account_Type TEXT,
		Address TEXT)''')
	cursor.execute(Users_table)

	#creating product table
	Product_table=('''CREATE TABLE IF NOT EXISTS
		Product_table(Product_ID INTEGER PRIMARY KEY,
		Product_name TEXT,
		Product_Type TEXT,
		Price FLOAT,
		Photo BLOB,
		User_ID INTEGER,
		FOREIGN KEY(User_ID) REFERENCES Users_table(User_ID))''')
	cursor.execute(Product_table)

	#creating wishlist table (will be removed or worked upon later)
	Wishlist_table=('''CREATE TABLE IF NOT EXISTS
		Wishlist_table(User_ID INTEGER PRIMARY KEY,
		Product_ID_1 INTEGER,
		Product_ID_2 INTEGER,
		Product_ID_3 INTEGER,
		Product_ID_4 INTEGER,
		Product_ID_5 INTEGER,
		Product_ID_6 INTEGER,
		Product_ID_7 INTEGER,
		Product_ID_8 INTEGER,
		Product_ID_9 INTEGER,
		Product_ID_10 INTEGER,
		FOREIGN KEY(User_ID) REFERENCES Users_table(User_ID))''')
	cursor.execute(Wishlist_table)

	#testing database functions
	#test data for users table
	cursor.execute("""INSERT OR IGNORE INTO Users_table VALUES(?,?,?,?,?)""",
		(1,'Azaan','CHILDISH.lbc','Seller','Newcastle'))
	cursor.execute("""INSERT OR IGNORE INTO Users_table VALUES(?,?,?,?,?)""",
		(2,'John','pAssWOrD','Buyer','Manchester'))
	cursor.execute("""INSERT OR IGNORE INTO Users_table VALUES(?,?,?,?,?)""",
		(3,'Tommy','Wednesday1963','Buyer','London'))
	cursor.execute("""INSERT OR IGNORE INTO Users_table VALUES(?,?,?,?,?)""",
		(4,'Kivaan','amazonSucks','Seller','Newcastle'))
	cursor.execute("""INSERT OR IGNORE INTO Users_table VALUES(?,?,?,?,?)""",
		(5,'Sarah','Sarah453','Seller','birmingham'))

	#test data for product table
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(1,'lamp','Furniture',24.99,sqlite3.Binary(Lamp),4))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(2,'chair','Furniture',19.99,sqlite3.Binary(Chair),1))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(3,'sofa','Furniture',949.99,sqlite3.Binary(Sofa),4))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table VALUES (?,?,?,?,?,?)""",
		(4,'Harry Potter','Books',31.99,sqlite3.Binary(Harry_potter),1))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(5,'The Great Gatsby','Books',11.99,sqlite3.Binary(Great_gatsby),5))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(6,'Empireland','Books',7.99,sqlite3.Binary(Empireland),4))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(7,'Dark Blue Jeans','Clothing',19.99,sqlite3.Binary(Blue_jeans),5))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(8,'Basic White Tee','Clothing',7.49,sqlite3.Binary(White_tee),1))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(9,'Basic Brown Hoodie','Clothing',34.99,sqlite3.Binary(Brown_hoodie),5))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(10,'Interstella','Media (gaming/movies)',11.99,sqlite3.Binary(Interstella),4))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(11,'MineCraft','Media (gaming/movies)',9.99,sqlite3.Binary(Minecraft),4))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(12,'DAMN','Media (gaming/movies)',14.99,sqlite3.Binary(Damn),1))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(13,'Kitchen Knife','Kitchen',9.99,sqlite3.Binary(Kitchen_knife),5))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(14,'Garlic press','Kitchen',11.99,sqlite3.Binary(Garlic_press),1))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(15,'Tin opener','Kitchen',4.99,sqlite3.Binary(Tin_opener),5))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(16,'Laptop','Computers/Technology',549.99,sqlite3.Binary(Laptop),1))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(17,'I phone','Computers/Technology',1299.99,sqlite3.Binary(Iphone),5))
	connection.commit()
	cursor.execute("""INSERT OR IGNORE INTO Product_table
	(Product_ID,Product_name,Product_Type,Price,Photo,User_ID) VALUES(?,?,?,?,?,?)""",
		(18,'Wireless ear buds','Computers/Technology',199.99,sqlite3.Binary(Wireless_ear_buds),4))
	connection.commit()

#------test data for wishlist table (will be removed or worked upon later)------
	#cursor.execute("""INSERT OR IGNORE INTO Wishlist_table(User_ID,Product_ID_1,Product_ID_2,Product_ID_3,Product_ID_4,
	#Product_ID_5,Product_ID_6,Product_ID_7,Product_ID_8,Product_ID_9,Product_ID_10)VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
	#		(1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1),
	#		(2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1),
	#		(3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1),
	#		(4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1),
	#		(5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1))
#-------------------------------------------------------------------------------

	connection.commit()
	connection.close()