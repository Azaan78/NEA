#flask and web design
from flask import Flask, render_template, request, redirect, url_for, flash
import random, string
from wtforms import StringField,FileField,SubmitField
from flask_wtf import FlaskForm

#SQL and databases section
import sqlite3
from sqlite3 import Error
from Database import database
database()

#image and file imports
import base64
import os
from werkzeug.utils import secure_filename

#defining connection, cursor and variables
filename="users.db"
connection=sqlite3.connect(filename)
cursor=connection.cursor()
loggedIn=False
user_loggin_ID=0
sellerAccount=False
item=("")
template=("ID-Name-Type-Price")
shopping_cart=[]
cartID=0

#reading images for icons in base64 and storing then under variable names
	#Profile
with open('Main files\Icon_Images\Profile.png','rb') as f:
	Photo_Data=f.read()
Profile=base64.b64encode(Photo_Data).decode('utf-8')
	#Red House
with open('Main files\Icon_Images\Red House.png','rb') as f:
	Photo_Data=f.read()
RedHouse=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue Clothes
with open('Main files\Icon_Images\Blue Clothes.png','rb') as f:
	Photo_Data=f.read()
BlueClothes=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue Controller
with open('Main files\Icon_Images\Blue Controller.png','rb') as f:
	Photo_Data=f.read()
BlueController=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue Laptop
with open('Main files\Icon_Images\Blue Laptop.png','rb') as f:
	Photo_Data=f.read()
BlueLaptop=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue Wisk
with open('Main files\Icon_Images\Blue Wisk.png','rb') as f:
	Photo_Data=f.read()
BlueWisk=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue Furniture
with open('Main files\Icon_Images\Blue Furniture.png','rb') as f:
	Photo_Data=f.read()
BlueFurniture=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue Book
with open('Main files\Icon_Images\Blue Books.png','rb') as f:
	Photo_Data=f.read()
BlueBook=base64.b64encode(Photo_Data).decode('utf-8')
	#Blue House
with open('Main files\Icon_Images\Blue House.png','rb') as f:
	Photo_Data=f.read()
BlueHouse=base64.b64encode(Photo_Data).decode('utf-8')
	#Red Clothes
with open('Main files\Icon_Images\Red Clothes.png','rb') as f:
	Photo_Data=f.read()
RedClothes=base64.b64encode(Photo_Data).decode('utf-8')
	#Red Controller
with open('Main files\Icon_Images\Red Controller.png','rb') as f:
	Photo_Data=f.read()
RedController=base64.b64encode(Photo_Data).decode('utf-8')
	#Red Laptop
with open('Main files\Icon_Images\Red Laptop.png','rb') as f:
	Photo_Data=f.read()
RedLaptop=base64.b64encode(Photo_Data).decode('utf-8')
	#Red Wisk
with open('Main files\Icon_Images\Red Wisk.png','rb') as f:
	Photo_Data=f.read()
RedWisk=base64.b64encode(Photo_Data).decode('utf-8')
	#Red Furniture
with open('Main files\Icon_Images\Red Furniture.png','rb') as f:
	Photo_Data=f.read()
RedFurniture=base64.b64encode(Photo_Data).decode('utf-8')
	#Red Books
with open('Main files\Icon_Images\Red Books.png','rb') as f:
	Photo_Data=f.read()
RedBooks=base64.b64encode(Photo_Data).decode('utf-8')
	#Banner 1
with open('Main files\Icon_Images\Banner1.png','rb') as f:
	Photo_Data=f.read()
Banner1=base64.b64encode(Photo_Data).decode('utf-8')
	#Banner 2
with open('Main files\Icon_Images\Banner2.png','rb') as f:
	Photo_Data=f.read()
Banner2=base64.b64encode(Photo_Data).decode('utf-8')
	#Banner 3
with open('Main files\Icon_Images\Banner3.jpg','rb') as f:
	Photo_Data=f.read()
Banner3=base64.b64encode(Photo_Data).decode('utf-8')
	#shopping cart blue
with open('Main files\Icon_Images\shopping cart.png','rb') as f:
	Photo_Data=f.read()
cart_icon=base64.b64encode(Photo_Data).decode('utf-8')
	#shopping cart red
with open('Main files\Icon_Images\\redcart.png','rb') as f:
	Photo_Data=f.read()
redcart=base64.b64encode(Photo_Data).decode('utf-8')

#main loop flask
#defining flask, the folder with the HTML pages 
app=Flask(__name__, template_folder="pages")
#used to flash messages
app.config['SECRET_KEY']='SecretShussshh'
#used to take images as inputs
app.config['UPLOAD_FOLDER']='static/files'

#Used to store image files
class UploadFileForm(FlaskForm):
	file=FileField("File")
	submit=SubmitField("Upload File")

#defines the home page
@app.route('/')
def home():
#Variables definitions
	global loggedIn
	global user_loggin_ID
	global sellerAccount
#SQL statements to connect and fetch highest product ID for randomiser
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
	cursor.execute("SELECT Product_ID FROM Product_table ORDER BY Product_ID DESC")
	Max=cursor.fetchone()[0]
#randomiser function for products in the range of max
	Product1=random.randrange(1,Max)
	Product2=random.randrange(1,Max)
	Product3=random.randrange(1,Max)
	Product4=random.randrange(1,Max)
#SQL to fetch images for display
	Photo1=cursor.execute(f"SELECT Photo FROM Product_table WHERE Product_ID={Product1}")
	Photo1=cursor.fetchone()[0]
	Photo2=cursor.execute(f"SELECT Photo FROM Product_table WHERE Product_ID={Product2}")
	Photo2=cursor.fetchone()[0]
	Photo3=cursor.execute(f"SELECT Photo FROM Product_table WHERE Product_ID={Product3}")
	Photo3=cursor.fetchone()[0]
	Photo4=cursor.execute(f"SELECT Photo FROM Product_table WHERE Product_ID={Product4}")
	Photo4=cursor.fetchone()[0]
#Product ID variables
	id1=Product1
	id2=Product2
	id3=Product3
	id4=Product4
#Reading/converting images
	Product1=base64.b64encode(Photo1).decode('utf-8')
	Product2=base64.b64encode(Photo2).decode('utf-8')
	Product3=base64.b64encode(Photo3).decode('utf-8')
	Product4=base64.b64encode(Photo4).decode('utf-8')
#rendering the home page, this passes all variables through to the HTML page
	return render_template('home.html',title='Welcome',loggedIn=loggedIn,ID=user_loggin_ID,
	seller=sellerAccount,RedHouse=RedHouse,BlueClothes=BlueClothes,BlueController=BlueController
	,BlueLaptop=BlueLaptop,BlueWisk=BlueWisk,BlueFurniture=BlueFurniture,BlueBook=BlueBook,Profile=Profile,
	Product1=Product1,Product2=Product2,Product3=Product3,Product4=Product4,Banner1=Banner1,Banner2=Banner2,
	Banner3=Banner3,id1=id1,id2=id2,id3=id3,id4=id4,cartID=cartID,cart_icon=cart_icon)

#flask login system
@app.route('/login', methods=['POST','GET'])
def login_flask():
#variables
	global loggedIn
	global sellerAccount
	global user_loggin_ID
#checks if user is logged in
	while loggedIn==False:
#when a post occurs
		if request.method=="POST":
#fetches information from html form
			username=request.form['username']
			password=request.form['password']
#connecting to database
			connection=sqlite3.connect(filename)
			cursor=connection.cursor()
#checking database for username and password
			cursor.execute(f"SELECT Username FROM Users_table WHERE Username='{username}' AND Password='{password}';")
#if username and password not found the login failed
			if not cursor.fetchone():
				loggedIn=False
				flash("Failed login","info")
				return redirect('/')
#if username and password  found the login successful and saves user_login_ID
			else:
				loggedIn=True
				cursor.execute(f"SELECT User_ID FROM Users_table WHERE username='{username}' AND password='{password}';")
				user_loggin_ID=cursor.fetchone()[0]
				cursor.execute(f"SELECT Account_Type FROM Users_table WHERE User_ID={user_loggin_ID}")
				sellerAccount=cursor.fetchone()[0]
				if sellerAccount=="Seller":
					sellerAccount=True
				elif sellerAccount=="Buyer":
					sellerAccount=False
#message displayed in HTML page and redirected to home page
				flash("Successful login","info")
				return redirect('/')
#before the post occurs (gets the page)
		return render_template("login.html",BlueHouse=BlueHouse)
	flash("already logged in","message")
	return redirect('/')

#flask register system
@app.route('/Register', methods=['POST','GET'])
def Register_flask():
#when a post occurs
	if request.method=="POST":
#fetches information from html form
		username=request.form['username']
		password=request.form['password']
		city=request.form['city']
#connecting to database
		connection=sqlite3.connect(filename)
		cursor=connection.cursor()
#checking data base for username
		cursor.execute(f"SELECT username FROM Users_table WHERE username='{username}';")
#if no username found then a register occurs and creates a user
		if not cursor.fetchone():
			print("register")
			cursor.execute("SELECT User_ID FROM Users_table ORDER BY User_ID DESC")
			UserID=cursor.fetchone()[0]
			UserID=UserID+1
			account_type=("Buyer")
			cursor.execute("""INSERT INTO Users_table VALUES (?,?,?,?,?);""",(UserID,username,password,account_type,city))
#saves changes and redirects to home
			connection.commit()
			return redirect('/login')
#if a record is returned then user already exists and redirected to register page
		else:
			print("user already exists")
			redirect(url_for('Register.html'))
#before the post occurs (gets the page)
	return render_template('Register.html')

@app.route('/search', methods=['POST'])
def search_flask():
#variables
	global item
	if request.method=="POST":
		search=request.form['search']
#connecting to database
		connection=sqlite3.connect(filename)
		cursor=connection.cursor()
#checks if item exists
		cursor.execute(f"SELECT Product_name FROM Product_table WHERE Product_name='{search}'")
#if doesn't exist, sent to home page
		if not cursor.fetchone():
			return redirect('/')
#if does exist, data taken through variables and page redirected
		else:
			item=search
			return redirect('/search/item')
	return redirect('/')
#redirected seach function
@app.route('/search/item', methods=['GET'])
def search():
#variables
	global template
	global item
#connecting database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selects all data to do with searched item
	cursor.execute(f"SELECT Product_ID, Product_name, Product_Type,Price FROM Product_table WHERE Product_name='{item}'")
	results=cursor.fetchone()
	results=str(results)
#selects item image and converts to base64 to be used in HTML
	cursor.execute(f"SELECT Photo FROM Product_table WHERE Product_name='{item}'")
	photoData=cursor.fetchone()[0]
	photo=base64.b64encode(photoData).decode('utf-8')
#page render
	return render_template('search.html', template=template, results=results,photo=photo)

@app.route('/Clothing')
def Clothing():
#Connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selecting information from the database
	cursor.execute("""SELECT Product_ID,Product_name,Product_Type,Price FROM Product_table
						WHERE Product_Type='Clothing' ORDER BY Product_ID DESC LIMIT 4""")
	results=cursor.fetchall()
#product one variables being sent
	Product_ID_1=results[0][0]
	Product_name_1=results[0][1]
	Product_Type_1=results[0][2]
	Price_1=results[0][3]
#product two variables being sent
	Product_ID_2=results[1][0]
	Product_name_2=results[1][1]
	Product_Type_2=results[1][2]
	Price_2=results[1][3]
#product three variables being sent
	Product_ID_3=results[2][0]
	Product_name_3=results[2][1]
	Product_Type_3=results[2][2]
	Price_3=results[2][3]
#product four variables being sent
	Product_ID_4=results[2][0]
	Product_name_4=results[2][1]
	Product_Type_4=results[2][2]
	Price_4=results[2][3]
#selecting image data from database
	cursor.execute("SELECT Photo FROM Product_table WHERE Product_Type='Clothing' ORDER BY Product_ID DESC LIMIT 4")
	Photo_Data=cursor.fetchall()
#image data being sent
	image_1=base64.b64encode(Photo_Data[0][0]).decode('utf-8')
	image_2=base64.b64encode(Photo_Data[1][0]).decode('utf-8')
	image_3=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
	image_4=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
#page render
	return render_template('Clothing.html',Product_ID_1=Product_ID_1,Product_name_1=Product_name_1,Product_Type_1=Product_Type_1,Price_1=Price_1,image_1=image_1,
	BlueHouse=BlueHouse,RedClothes=RedClothes,BlueController=BlueController,BlueLaptop=BlueLaptop,BlueWisk=BlueWisk,BlueFurniture=BlueFurniture,BlueBook=BlueBook,Profile=Profile,
	Product_ID_2=Product_ID_2,Product_name_2=Product_name_2,Product_Type_2=Product_Type_2,Price_2=Price_2,image_2=image_2,
	Product_ID_3=Product_ID_3,Product_name_3=Product_name_3,Product_Type_3=Product_Type_3,Price_3=Price_3,image_3=image_3,
	Product_ID_4=Product_ID_4,Product_name_4=Product_name_4,Product_Type_4=Product_Type_4,Price_4=Price_4,image_4=image_4,
	cart_icon=cart_icon)

@app.route('/Media')
def Media():
#Connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selecting information from the database
	cursor.execute("""SELECT Product_ID,Product_name,Product_Type,Price FROM Product_table
						WHERE Product_Type='Media (gaming/movies)' ORDER BY Product_ID DESC LIMIT 4""")
	results=cursor.fetchall()
#product one variables being sent
	Product_ID_1=results[0][0]
	Product_name_1=results[0][1]
	Product_Type_1=results[0][2]
	Price_1=results[0][3]
#product two variables being sent
	Product_ID_2=results[1][0]
	Product_name_2=results[1][1]
	Product_Type_2=results[1][2]
	Price_2=results[1][3]
#product three variables being sent
	Product_ID_3=results[2][0]
	Product_name_3=results[2][1]
	Product_Type_3=results[2][2]
	Price_3=results[2][3]
#product four variables being sent
	Product_ID_4=results[2][0]
	Product_name_4=results[2][1]
	Product_Type_4=results[2][2]
	Price_4=results[2][3]
#selecting image data from database
	cursor.execute("SELECT Photo FROM Product_table WHERE Product_Type='Media (gaming/movies)' ORDER BY Product_ID DESC LIMIT 4")
	Photo_Data=cursor.fetchall()
#image data being sent
	image_1=base64.b64encode(Photo_Data[0][0]).decode('utf-8')
	image_2=base64.b64encode(Photo_Data[1][0]).decode('utf-8')
	image_3=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
	image_4=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
#page render
	return render_template('Media.html',BlueHouse=BlueHouse,BlueClothes=BlueClothes,RedController=RedController,BlueLaptop=BlueLaptop,BlueWisk=BlueWisk,BlueFurniture=BlueFurniture,BlueBook=BlueBook,Profile=Profile,
	Product_ID_1=Product_ID_1,Product_name_1=Product_name_1,Product_Type_1=Product_Type_1,Price_1=Price_1,image_1=image_1,
	Product_ID_2=Product_ID_2,Product_name_2=Product_name_2,Product_Type_2=Product_Type_2,Price_2=Price_2,image_2=image_2,
	Product_ID_3=Product_ID_3,Product_name_3=Product_name_3,Product_Type_3=Product_Type_3,Price_3=Price_3,image_3=image_3,
	Product_ID_4=Product_ID_4,Product_name_4=Product_name_4,Product_Type_4=Product_Type_4,Price_4=Price_4,image_4=image_4,
	cart_icon=cart_icon)

@app.route('/Computers')
def Computers():
#Connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selecting information from the database
	cursor.execute("""SELECT Product_ID,Product_name,Product_Type,Price FROM Product_table
						WHERE Product_Type='Computers/Technology' ORDER BY Product_ID DESC LIMIT 4""")
	results=cursor.fetchall()
#product one variables being sent
	Product_ID_1=results[0][0]
	Product_name_1=results[0][1]
	Product_Type_1=results[0][2]
	Price_1=results[0][3]
#product two variables being sent
	Product_ID_2=results[1][0]
	Product_name_2=results[1][1]
	Product_Type_2=results[1][2]
	Price_2=results[1][3]
#product three variables being sent
	Product_ID_3=results[2][0]
	Product_name_3=results[2][1]
	Product_Type_3=results[2][2]
	Price_3=results[2][3]
#product four variables being sent
	Product_ID_4=results[2][0]
	Product_name_4=results[2][1]
	Product_Type_4=results[2][2]
	Price_4=results[2][3]
#selecting image data from database
	cursor.execute("SELECT Photo FROM Product_table WHERE Product_Type='Computers/Technology' ORDER BY Product_ID DESC LIMIT 4")
	Photo_Data=cursor.fetchall()
#image data being sent
	image_1=base64.b64encode(Photo_Data[0][0]).decode('utf-8')
	image_2=base64.b64encode(Photo_Data[1][0]).decode('utf-8')
	image_3=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
	image_4=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
#page render
	return render_template('Computers.html',BlueHouse=BlueHouse,BlueClothes=BlueClothes,BlueController=BlueController,RedLaptop=RedLaptop,BlueWisk=BlueWisk,BlueFurniture=BlueFurniture,BlueBook=BlueBook,Profile=Profile,
	Product_ID_1=Product_ID_1,Product_name_1=Product_name_1,Product_Type_1=Product_Type_1,Price_1=Price_1,image_1=image_1,
	Product_ID_2=Product_ID_2,Product_name_2=Product_name_2,Product_Type_2=Product_Type_2,Price_2=Price_2,image_2=image_2,
	Product_ID_3=Product_ID_3,Product_name_3=Product_name_3,Product_Type_3=Product_Type_3,Price_3=Price_3,image_3=image_3,
	Product_ID_4=Product_ID_4,Product_name_4=Product_name_4,Product_Type_4=Product_Type_4,Price_4=Price_4,image_4=image_4,
	cart_icon=cart_icon)

@app.route('/Kitchen')
def Kitchen():
#Connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selecting information from the database
	cursor.execute("""SELECT Product_ID,Product_name,Product_Type,Price FROM Product_table
						WHERE Product_Type='Kitchen' ORDER BY Product_ID DESC LIMIT 4""")
	results=cursor.fetchall()
#product one variables being sent
	Product_ID_1=results[0][0]
	Product_name_1=results[0][1]
	Product_Type_1=results[0][2]
	Price_1=results[0][3]
#product two variables being sent
	Product_ID_2=results[1][0]
	Product_name_2=results[1][1]
	Product_Type_2=results[1][2]
	Price_2=results[1][3]
#product three variables being sent
	Product_ID_3=results[2][0]
	Product_name_3=results[2][1]
	Product_Type_3=results[2][2]
	Price_3=results[2][3]
#product four variables being sent
	Product_ID_4=results[2][0]
	Product_name_4=results[2][1]
	Product_Type_4=results[2][2]
	Price_4=results[2][3]
#selecting image data from database
	cursor.execute("SELECT Photo FROM Product_table WHERE Product_Type='Kitchen' ORDER BY Product_ID DESC LIMIT 4")
	Photo_Data=cursor.fetchall()
#image data being sent
	image_1=base64.b64encode(Photo_Data[0][0]).decode('utf-8')
	image_2=base64.b64encode(Photo_Data[1][0]).decode('utf-8')
	image_3=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
	image_4=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
#page render
	return render_template('Kitchen.html',BlueHouse=BlueHouse,BlueClothes=BlueClothes,BlueController=BlueController,BlueLaptop=BlueLaptop,RedWisk=RedWisk,BlueFurniture=BlueFurniture,BlueBook=BlueBook,Profile=Profile,
	Product_ID_1=Product_ID_1,Product_name_1=Product_name_1,Product_Type_1=Product_Type_1,Price_1=Price_1,image_1=image_1,
	Product_ID_2=Product_ID_2,Product_name_2=Product_name_2,Product_Type_2=Product_Type_2,Price_2=Price_2,image_2=image_2,
	Product_ID_3=Product_ID_3,Product_name_3=Product_name_3,Product_Type_3=Product_Type_3,Price_3=Price_3,image_3=image_3,
	Product_ID_4=Product_ID_4,Product_name_4=Product_name_4,Product_Type_4=Product_Type_4,Price_4=Price_4,image_4=image_4,
	cart_icon=cart_icon)

@app.route('/Furniture')
def Furniture():
#Connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selecting information from the database
	cursor.execute("""SELECT Product_ID,Product_name,Product_Type,Price FROM Product_table
						WHERE Product_Type='Furniture' ORDER BY Product_ID DESC LIMIT 4""")
	results=cursor.fetchall()
#product one variables being sent
	Product_ID_1=results[0][0]
	Product_name_1=results[0][1]
	Product_Type_1=results[0][2]
	Price_1=results[0][3]
#product two variables being sent
	Product_ID_2=results[1][0]
	Product_name_2=results[1][1]
	Product_Type_2=results[1][2]
	Price_2=results[1][3]
#product three variables being sent
	Product_ID_3=results[2][0]
	Product_name_3=results[2][1]
	Product_Type_3=results[2][2]
	Price_3=results[2][3]
#product four variables being sent
	Product_ID_4=results[2][0]
	Product_name_4=results[2][1]
	Product_Type_4=results[2][2]
	Price_4=results[2][3]
#selecting image data from database
	cursor.execute("SELECT Photo FROM Product_table WHERE Product_Type='Furniture' ORDER BY Product_ID DESC LIMIT 4")
	Photo_Data=cursor.fetchall()
#image data being sent
	image_1=base64.b64encode(Photo_Data[0][0]).decode('utf-8')
	image_2=base64.b64encode(Photo_Data[1][0]).decode('utf-8')
	image_3=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
	image_4=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
#page render
	return render_template('Furniture.html',BlueHouse=BlueHouse,BlueClothes=BlueClothes,BlueController=BlueController,BlueLaptop=BlueLaptop,BlueWisk=BlueWisk,RedFurniture=RedFurniture,BlueBook=BlueBook,Profile=Profile,
	Product_ID_1=Product_ID_1,Product_name_1=Product_name_1,Product_Type_1=Product_Type_1,Price_1=Price_1,image_1=image_1,
	Product_ID_2=Product_ID_2,Product_name_2=Product_name_2,Product_Type_2=Product_Type_2,Price_2=Price_2,image_2=image_2,
	Product_ID_3=Product_ID_3,Product_name_3=Product_name_3,Product_Type_3=Product_Type_3,Price_3=Price_3,image_3=image_3,
	Product_ID_4=Product_ID_4,Product_name_4=Product_name_4,Product_Type_4=Product_Type_4,Price_4=Price_4,image_4=image_4,
	cart_icon=cart_icon)

@app.route('/Books')
def Books():
#Connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#selecting information from the database
	cursor.execute("""SELECT Product_ID,Product_name,Product_Type,Price FROM Product_table
						WHERE Product_Type='Books' ORDER BY Product_ID DESC LIMIT 4""")
	results=cursor.fetchall()
#product one variables being sent
	Product_ID_1=results[0][0]
	Product_name_1=results[0][1]
	Product_Type_1=results[0][2]
	Price_1=results[0][3]
#product two variables being sent
	Product_ID_2=results[1][0]
	Product_name_2=results[1][1]
	Product_Type_2=results[1][2]
	Price_2=results[1][3]
#product three variables being sent
	Product_ID_3=results[2][0]
	Product_name_3=results[2][1]
	Product_Type_3=results[2][2]
	Price_3=results[2][3]
#product four variables being sent
	Product_ID_4=results[2][0]
	Product_name_4=results[2][1]
	Product_Type_4=results[2][2]
	Price_4=results[2][3]
#selecting image data from database
	cursor.execute("SELECT Photo FROM Product_table WHERE Product_Type='Books' ORDER BY Product_ID DESC LIMIT 4")
	Photo_Data=cursor.fetchall()
#image data being sent
	image_1=base64.b64encode(Photo_Data[0][0]).decode('utf-8')
	image_2=base64.b64encode(Photo_Data[1][0]).decode('utf-8')
	image_3=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
	image_4=base64.b64encode(Photo_Data[2][0]).decode('utf-8')
#page render
	return render_template('Books.html',BlueHouse=BlueHouse,BlueClothes=BlueClothes,BlueController=BlueController,BlueLaptop=BlueLaptop,BlueWisk=BlueWisk,BlueFurniture=BlueFurniture,RedBooks=RedBooks,Profile=Profile,
	Product_ID_1=Product_ID_1,Product_name_1=Product_name_1,Product_Type_1=Product_Type_1,Price_1=Price_1,image_1=image_1,
	Product_ID_2=Product_ID_2,Product_name_2=Product_name_2,Product_Type_2=Product_Type_2,Price_2=Price_2,image_2=image_2,
	Product_ID_3=Product_ID_3,Product_name_3=Product_name_3,Product_Type_3=Product_Type_3,Price_3=Price_3,image_3=image_3,
	Product_ID_4=Product_ID_4,Product_name_4=Product_name_4,Product_Type_4=Product_Type_4,Price_4=Price_4,image_4=image_4,
	cart_icon=cart_icon)

@app.route('/ChangeUsername',methods=['GET','POST'])
def ChangeUsername():
#defining global variables
	global loggedIn
	global user_loggin_ID
#connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#if not logged in message returned on HTML page and redirected to home
	if loggedIn==False:
		flash("Not logged in","info")
		return redirect('/')
#if logged in username change occurs
	if loggedIn==True:
		#defines the page type
		change=("user")
#then a post occurs
		if request.method=="POST":
#fetching all data from the form
			olduser=request.form['olduser']
			newuser=request.form['newuser']
			newusercon=request.form['newusercon']
#checking if username exists already
			cursor.execute(f"SELECT Username FROM Users_table WHERE User_ID={user_loggin_ID}")
			CheckUser=cursor.fetchone()[0]
#checks if username is the same user confirm for validation, also checks if username is taken for more validation
			if olduser==CheckUser:
				if newuser==newusercon:
					cursor.execute(f"SELECT User_ID FROM Users_table WHERE Username='{newuser}'")
					if not cursor.fetchone():
						cursor.execute(f"UPDATE Users_table SET Username='{newuser}' WHERE User_ID={user_loggin_ID}")
						connection.commit()
						flash("Username has been changed","info")
						return redirect('/')
					else:
						flash("Another user already has this username","info")
						return redirect('/ChangeUsername')
				elif newuser!=newusercon:
					flash("Username dows not match confirm username")
					return redirect('/ChangeUsername')
			elif olduser!=CheckUser:
				flash("Original username does not match!","error")
				return redirect('/ChangeUsername')
		return render_template("Change.html",change=change)

@app.route("/ChangePassword",methods=['GET','POST'])
def ChangePassword():
#defining global variables
	global loggedIn
	global user_loggin_ID
#connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#if not logged in message returned on HTML page and redirected to home
	if loggedIn==False:
		flash("Not logged in","info")
		return redirect('/')
	if loggedIn==True:
		#defines the page type
		change=("pass")
#then a post occurs
		if request.method=="POST":
#fetching all data from the form
			oldpass=request.form['oldpass']
			newpass=request.form['newpass']
			newpasscon=request.form['newpasscon']
#checking if username exists already
			cursor.execute(f"SELECT Password FROM Users_table WHERE User_ID={user_loggin_ID}")
			CheckUser=cursor.fetchone()[0]
#checks if username is the same user confirm for validation, also checks if username is taken for more validation
			if oldpass==CheckUser:
				if newpass==newpasscon:
					cursor.execute(f"SELECT User_ID FROM Users_table WHERE Password='{newpass}'")
					if not cursor.fetchone():
						cursor.execute(f"UPDATE Users_table SET Password='{newpass}' WHERE User_ID={user_loggin_ID}")
						connection.commit()
						flash("Password has been changed","info")
						return redirect('/')
					else:
						flash("Another user already has this password","info")
						return redirect('/ChangePassword')
				elif newpass!=newpasscon:
					flash("Password dows not match confirm password")
					return redirect('/ChangePassword')
			elif oldpass!=CheckUser:
				flash("Original password does not match!","error")
				return redirect('/ChangePassword')
	return render_template("Change.html",change=change)

@app.route('/Logout')
def logout():
#defining global variables
	global user_loggin_ID
	global sellerAccount
	global loggedIn
#if user not logged in then redirected
	if loggedIn==False:
		flash("Not logged in","info")
		return redirect('/')
#if user logged in then they are logged out
	elif loggedIn==True:
		user_loggin_ID=0
		loggedIn=False
		sellerAccount=False
		flash("User logged out","info")
		return redirect('/')
#else there is an error
	else:
		flash("error","error")
		return redirect('/')
	
@app.route('/Delete')
def DeleteAccount():
#variables
	global loggedIn
	global user_loggin_ID
	global sellerAccount
#connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#checking if user is logged in
	if loggedIn==False:
		flash("Not logged in","error")
		return redirect('/')
#if user it logged in deletion occurs
	elif loggedIn==True:
#if account is seller type then all products deleted too
		if sellerAccount==True:
			cursor.execute(f"DELETE FROM Product_table WHERE User_ID={user_loggin_ID}")
#account deleted
		cursor.execute(f"DELETE FROM Users_table WHERE User_ID={user_loggin_ID}")
		connection.commit()
		flash('account deleted','message')
		return redirect('/login')

@app.route('/RemoveProduct',methods=['GET','POST'])
def RemoveProduct():
#setting variables
	#defines the page type
	type=("removal")
	global user_loggin_ID
	global sellerAccount
	global loggedIn
#connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#fetching all data related to user ID
	cursor.execute(f"SELECT Product_ID,Product_name,Price,User_ID FROM Product_table WHERE User_ID={user_loggin_ID}")
	results=cursor.fetchall()
	length=len(results)
	if request.method=="POST":
#fetching product ID from the form
		Product_ID_Form=request.form['Product_ID_Form']
#deletes product record
		cursor.execute(f"DELETE FROM Product_table WHERE Product_ID={Product_ID_Form}")
		connection.commit()
		return redirect('/RemoveProduct')
#render page
	return render_template('Product.html',type=type,results=results,length=length)

@app.route('/AddProduct', methods=['GET','POST'])
def AddProduct():
#declaring variables
	form=UploadFileForm()
	#defines the page type
	type=("addition")
	global user_loggin_ID
	global sellerAccount
	global loggedIn
#connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
#fetching all data related to user ID
	cursor.execute(f"SELECT Product_ID,Product_name,Price,User_ID FROM Product_table WHERE User_ID={user_loggin_ID}")
	results=cursor.fetchall()
	length=len(results)
	if request.method=="POST":
		print("post")
#fetching all data from the form
		ProductName=request.form['ProductName']
		ProductPrice=request.form['ProductPrice']
		ProductType=request.form['ProductType']
#all code to read image and take a file as an input
		if form.validate_on_submit():
			file=form.file.data
			file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
			path=os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
			with open(path,'rb') as f:
				image=f.read()
#converting image to base64
			imagetemp=base64.b64encode(image).decode('utf-8')
			imagetemp=sqlite3.Binary(imagetemp)
#auto increment product ID
			Product_ID=cursor.execute("SELECT Product_ID FROM Product_table ORDER BY Product_ID DESC")
			Product_ID=cursor.fetchone()[0]
			Product_ID=int(Product_ID)+1
			print(imagetemp)
			print(Product_ID,ProductName,ProductType,ProductPrice,user_loggin_ID)
#insert the new product record
			cursor.execute("INSERT INTO Product_table VALUES (?,?,?,?,?,?)",Product_ID,ProductName,ProductType,ProductPrice,imagetemp,user_loggin_ID)
			connection.commit()
			flash('product added to database','message')
			return redirect('/AddProduct')
		else:
			print("not validated")
#page render
	print("not post")
	return render_template('Product.html',type=type, results=results,length=length, form=form)

#defining add to cart function
@app.route('/add_to_cart',methods=['GET','POST'])
def add_to_cart():
#fetches product ID of the item then appends it to the shopping cart array
	cartID=request.form['cartID']
	shopping_cart.append(cartID)
	return redirect('/')

@app.route('/view_cart',methods=['GET','POST'])
def view_cart():
	#connecting to database
	connection=sqlite3.connect(filename)
	cursor=connection.cursor()
	#defining a new list to be used in the loop
	list=[]
	#taking length of shopping cart
	length=len(shopping_cart)
	#iterating through the indexes in the shopping cart list then fetching infor from database and appending to new list
	for x in range(0,length):
		i=shopping_cart[x]
		cursor.execute(f"SELECT Product_ID,Product_name,Price,User_ID FROM Product_table WHERE Product_ID={i}")
		temp=cursor.fetchone()
		list.append(temp)
	length=len(list)
	return render_template('Shopping_cart.html',list=list,length=length,BlueHouse=BlueHouse,BlueClothes=BlueClothes,
BlueController=BlueController,BlueLaptop=BlueLaptop,BlueWisk=BlueWisk,BlueFurniture=BlueFurniture,BlueBook=BlueBook,Profile=Profile,redcart=redcart)

if __name__=="__main__":
	app.run(host="0.0.0.0", port=80, debug=True)

#this is for debugging, when ctrl-c is pressed in console it kills website and prints database contents
cursor.execute("SELECT*FROM Users_table")
results=cursor.fetchall()
print(results)
print()
cursor.execute("SELECT Product_ID,Product_name,Product_Type,Price,User_ID FROM Product_table")
results=cursor.fetchall()
print(results)