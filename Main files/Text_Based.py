#SQL and databases section
import sqlite3
from sqlite3 import Error
from Database import database
database()

#defining connection and cursor, also importing database from database file
filename="users.db"
connection=sqlite3.connect(filename)
cursor=connection.cursor()

#defining login system function
def login(loggedIn,User_loggin_ID):
#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#gives user 3 attempts
	count=3
#username input outside of loop so user doesn't have to keep inputting if password wrong
	username=input("Enter your username:	")
#loop that only occurs if user still has attempts and is not logged in
	while count > 0 and loggedIn==False:
#taking password input and running select statement in database to see if the record exists
		password=input("Enter your password:	")
		cursor.execute(f"SELECT username FROM Users_table WHERE username='{username}' AND password='{password}';")
#if no record is returned then attempts is decremented by 1, a message is displayed and user has to try again
		if not cursor.fetchone():
			print("Login failed")
			count=count-1
			print(count," attemps left")
			loggedIn=False
#else if a record is returned then message displayed, logged in is set to true and the user_ID is saved to the variable
		else:
			loggedIn=True
			print("Login successful")
			cursor.execute(f"SELECT User_ID FROM Users_table WHERE username='{username}' AND password='{password}';")
			User_loggin_ID=cursor.fetchone()[0]
#if no more attempts are allowed the message returned
		if count<1:
			print("Out of attempts")
#variables returned
	return loggedIn,User_loggin_ID

#defininf register system function
def register():
#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#Variables to check if an account has been made and if one already exists, loops until account has been made
	accountMade=False
	while accountMade==False:
#username taken as input, select statement used to check if record with the username exists
		username=input("Enter your username:")
		cursor.execute(f"SELECT username FROM Users_table WHERE username='{username}';")
#if no record is returned then username can be used
		if not cursor.fetchone():
#automatically finds the largest user ID and increments it by one for the new account being registered
			cursor.execute("SELECT User_ID FROM Users_table ORDER BY User_ID DESC")
			UserID=cursor.fetchone()[0]
			UserID=UserID+1
#takes an input for password and address, account_type is constant as all accounts are automatically registered as buyers
			password=input("Enter your password:")
			account_type=("Buyer")
			address=input("Enter your city:")
#insert statement to add record to database
			cursor.execute("""INSERT INTO Users_table VALUES (?,?,?,?,?);""",(UserID,username,password,account_type,address))
			accountMade=True
#if user doesn't exist then message displayed
		else:
			print("User already exists")
#saves changes
	connection.commit()

#Search bar function, only works theoretically and if search is identical
def Search_Bar():
#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#loops until the item is found
	search=False
	while search!=True:
#user inputs the name of the item they want to search the is checked against the database using a select statement
		Search_Value=input("Enter product in search:")
		cursor.execute(f"SELECT Product_name FROM Product_table WHERE Product_name='{Search_Value}'")
#if no record is returned then the items doesnt exist and a message is returned
		if not cursor.fetchone():
			print("Product not found")
#if product exists the information about it is fetched and returned
		else:
#titles for users reading information
			print("ID-Name-Type-Price")
			cursor.execute(f"SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_name='{Search_Value}'")
			results=cursor.fetchall()
			print(results)
			search=True

#function to delete account in account section
def Account_Deletion(User_loggin_ID):
#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#loops until account is deleted
	account_delete=False
	while account_delete==False:
#takes username and password of the account that is to be deleted and uses a select statement to verify record exists
		username=input("Enter your username:	")
		password=input("Enter your password:	")
		cursor.execute(f"SELECT username FROM Users_table WHERE username='{username}' AND password='{password}';")
#if account record doesn't exist then message displayed
		if not cursor.fetchone():
			print("Account doesn't exist")
#if account exists select user ID of the account and save it to a variable user_loggin_ID, use this to check if account type is seller or not and save to variable sellerAccount
		else:
			cursor.execute(f"SELECT User_ID FROM Users_table WHERE username='{username}' AND password='{password}';")
			User_loggin_ID=cursor.fetchone()[0]
			cursor.execute(f'SELECT Account_Type FROM Users_table WHERE User_ID={User_loggin_ID}')
			sellerAccount=cursor.fetchone()[0]
#if seller account is true then all products are deleted
			if sellerAccount=="Seller":
				cursor.execute(f'DELETE FROM Product_table WHERE User_ID={User_loggin_ID}')
#user account is deleted where userID is userLogginID
			cursor.execute(f'DELETE FROM Users_table WHERE User_ID="{User_loggin_ID}"')
			account_delete=True
#saves changes
	connection.commit()

#function for sellers to add products
def product_addition(sellerAccount,User_loggin_ID):
#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selects account type based on the user_loggin_ID
	sellerAccount=cursor.execute(f'SELECT Account_Type FROM Users_table WHERE User_ID={User_loggin_ID}')
	sellerAccount=cursor.fetchone()[0]
#seller account is set to true or false depending on return above
	if sellerAccount=="Seller":
		sellerAccount=True
	elif sellerAccount=="Buyer":
		sellerAccount=False
#now is the main loop to add a product
	if sellerAccount==True:
#auto increments product ID
		ProdID=cursor.execute("SELECT Product_ID FROM Product_table ORDER BY Product_ID DESC")
		ProdID=cursor.fetchone()[0]
		ProdID=ProdID+1
#takes input for product name
		Prod_Name=input("Enter name of product:")
#option select for product type
		Prod_Type=int(input("""Press 1: Clothing
Press 2: Media (gaming/movies)
Press 3: Computers/Technology
Press 4: Kitchen
Press 5: Furniture
Press 6: Books
"""))
		if Prod_Type==1:
			Prod_Type=("Clothing")
		elif Prod_Type==2:
			Prod_Type=("Media (gaming/movies)")
		elif Prod_Type==3:
			Prod_Type=("Computers/Technology")
		elif Prod_Type==4:
			Prod_Type=("Kitchen")
		elif Prod_Type==5:
			Prod_Type=("Furniture")
		elif Prod_Type==6:
			Prod_Type=("Books")
#takes input for product price
		Price=float(input("Enter Price:	"))
#images were implemented in the next iteration so added this to make sure the previous iteration works
		photo=("temp")
#inserts record with all information
		cursor.execute('''INSERT INTO Product_table VALUES(?,?,?,?,?,?);''',(ProdID,Prod_Name,Prod_Type,Price,photo,User_loggin_ID))
#if account is not a seller then message diaplyed	
	elif sellerAccount==False:
		print("Must have a seller account")
#saves changes
	connection.commit()

def change_Username():
	#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#loops until username is changed
	user_Change=False
	while user_Change==False:
#takes inputs for username and password and uses select statement to see if account record exists
		username=input("Enter your username:	")
		password=input("Enter your password:	")
		cursor.execute(f"SELECT username FROM Users_table WHERE username='{username}' AND password='{password}';")
#if no record is returned then message displayed		
		if not cursor.fetchone():
			print("Account doesn't exist")
		else:
#if record returned then new username is asked for and is checked to see if it is already taken	
			New_Username=input("Enter new username:	")
			cursor.execute(f"SELECT Username FROM Users_table WHERE Username='{New_Username}';")
#if username is not already taken then update is run and username changed
			if not cursor.fetchone():
				cursor.execute('UPDATE Users_table SET Username=? WHERE Username=?', (New_Username, username))
				connection.commit()
				user_Change=True
#username is taken so message displayed
			else:
				print("User already exists")
#saves changes
	connection.commit()

def change_Password():
#re-connecting the to server
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#loops until password is changed
	pass_Change=False
	while pass_Change==False:
#takes inputs for username and password and uses select statement to see if account record exists
		username=input("Enter your username:	")
		password=input("Enter your password:	")
		cursor.execute(f"SELECT username FROM Users_table WHERE username='{username}' AND password='{password}';")
#if no record is returned then message displayed		
		if not cursor.fetchone():
			print("Account doesn't exist")
		else:
#if record returned then new password is asked for and is checked to see if it is already taken	
			New_Password=input("Enter new Password:	")
			cursor.execute(f"SELECT Password FROM Users_table WHERE Password='{New_Password}';")
			if not cursor.fetchone():
				cursor.execute('UPDATE Users_table SET Password=? WHERE Password=?', (New_Password, password))
				pass_Change=True
#password is taken so message displayed
			else:
				print("Password already exists")
#saves changes
	connection.commit()

#variables used globally in the program
loggedIn=False
User_loggin_ID=0
sellerAccount=False
results=("")

#main loop text based
while True:
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#first option select
	option_select=int(input('''Press 1: Login
Press 2: Register
Press 3: Store
Press 4: View database
'''))
	if option_select==1:
		if loggedIn==True:
			print("Already logged in")
		elif loggedIn==False:
			loggedIn,User_loggin_ID=login(loggedIn,User_loggin_ID)
	elif option_select==2:
		register()
#second option select
	elif option_select==3:
		option_select_2=int(input("""Press 1: Search
Press 2: Catagories
Press 3: Account
Press 4: Wishlist
Press 5: Basket
Press 6: Add product
"""))
#search bar function
		if option_select_2==1:
			Search_Bar()
#Section for all filter selects and statements
		if option_select_2==2:
			catagory_Select=int(input("""Press 1: Home
Press 2: Clothing
Press 3: Media (gaming/movies)
Press 4: Computers/Technology
Press 5: Kitchen
Press 6: Furniture
Press 7: Books
"""))
			if catagory_Select==2:
				cursor.execute("SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_Type='Clothing'")
				results=cursor.fetchall()
				print(results)
			elif catagory_Select==3:
				cursor.execute("SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_Type='Media (gaming/movies)'")
				results=cursor.fetchall()
				print(results)
			elif catagory_Select==4:
				cursor.execute("SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_Type='Computers/Technology'")
				results=cursor.fetchall()
				print(results)
			elif catagory_Select==5:
				cursor.execute("SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_Type='Kitchen'")
				results=cursor.fetchall()
				print(results)
			elif catagory_Select==6:
				cursor.execute("SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_Type='Furniture'")
				results=cursor.fetchall()
				print(results)
			elif catagory_Select==7:
				cursor.execute("SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_Type='Books'")
				results=cursor.fetchall()
				print(results)
#Account adjustment options
		if option_select_2==3:
			Account_Select=int(input("""Press 1: Account deletion
Press 2: Change Username
Press 3: Change Password
Press 4: Upgrade to seller account
"""))
			if Account_Select==1:
				Account_Deletion(User_loggin_ID)
			elif Account_Select==2:
				change_Username()
			elif Account_Select==3:
				change_Password()
#Wishlist options
		if option_select_2==4:
			print()
			#print(Wish_List)
#Basket options
		if option_select_2==5:
			print()
			#print(Basket)
#Product addition function select
		if option_select_2==6:
			product_addition(sellerAccount,User_loggin_ID)
	elif option_select==4:

#outputs the contents of users table for test purposes
#will be removed at a later date
		cursor.execute("SELECT*FROM Users_table")
		results=cursor.fetchall()
		print(results)
		print()
		cursor.execute("SELECT Product_ID,Product_name,Product_Type,Price,User_ID FROM Product_table")
		results=cursor.fetchall()
		print(results)