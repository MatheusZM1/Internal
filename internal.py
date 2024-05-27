#Imports go at the top
import sqlite3, os, time, random

#Essentials to connect to the database
conn = sqlite3.connect('DinosaursData')
cursor = conn.cursor()

def get_all_dinosaur_names():
    # Execute an SQL statement and save the result to a variable
    cursor.execute('SELECT Name FROM DinosaursData;')
    names = cursor.fetchall()
    
    #Loop for each name retrieved
    for name in names:
        print(f"{name[0]}")
        time.sleep(0.1)

#Main Loop
while True:
    user_input = input("\n1 - Get all dinosaur names\n2 - Exit\n\n>")

    if user_input == "1":
        get_all_dinosaur_names()
    elif user_input == "2":
        os.system("cls")
        print("Program has stopped")
        break

#End the program
conn.commit()
conn.close()