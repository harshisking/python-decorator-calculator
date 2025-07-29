import time
from datetime import datetime

is_logged_in = False

def loginReq(func):
	def wrapper(*args, **kwargs):
		if not is_logged_in:
			print("Please log in first")
			return None
		return func(*args, **kwargs)
	return wrapper

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"{func.__name__} took {end-start} seconds")
		return result
	return wrapper

def Validate(func):
	def wrapper(a,b):
		if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
			print("invalid input")
			return None
		return func(a,b)
	return wrapper

def logtofile(func):
	def wrapper(*args, **kwargs):
		with open("logs.txt", "a") as file:
			file.write(f"[{datetime.now()}] {func.__name__} was called with {args}\n")
		return func(*args, **kwargs)
	return wrapper

def login():
	global is_logged_in
	username = input("Username > ")
	password = input("Password > ")
	if password == "12345678" and username == "admin":
		is_logged_in= True
		print("logged in successfully")
	else:
		print("Wrong Password")

@timer
@Validate
@loginReq
@logtofile
def Add(a,b):
	return a+b

@timer
@Validate
@loginReq
@logtofile
def Divide(a,b):
	return a/b

@timer
@Validate
@loginReq
@logtofile
def Multiply(a,b):
	return a*b

@timer
@Validate
@loginReq
@logtofile
def Substract(a,b):
	return a-b

def menu():
	while True:
		print("\n1.Login\n2.Add\n3.Substract\n4.Multiply\n5.Divide\n6.Exit")
		choice = input("Choice: ")
		if choice == "1":
			login()
		elif choice =="2":
			x = int(input("X: "))
			y = int(input("Y: "))
			Add(x,y)
		elif choice =="3":
			x = int(input("X: "))
			y = int(input("Y: "))
			Substract(x,y)
		elif choice =="4":
			x = int(input("X: "))
			y = int(input("Y: "))
			Multiply(x,y)
		elif choice =="5":
			x = int(input("X: "))
			y = int(input("Y: "))
			Divide(x,y)
		else:
			exit()

menu()