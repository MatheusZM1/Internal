#Imports go at the top
import sqlite3, os, time, random

#Essentials to connect to the database
conn = sqlite3.connect('DinosaursData')
cursor = conn.cursor()

def invalid_option_response():
    os.system("cls")
    print("Invalid option")
    time.sleep(2)
    os.system("cls")

def get_all_dinosaur_names():
    # Execute an SQL statement and save the result to a variable
    cursor.execute('SELECT Name FROM DinosaursData;')
    names = cursor.fetchall()

    os.system("cls")
    print("All dinosaur names:\n")
    
    #Loop for each name retrieved
    for name in names:
        print(f"{name[0]}")
        time.sleep(0.1)

def get_all_information():
    # Execute an SQL statement and save the result to a variable
    cursor.execute('SELECT * FROM DinosaursData;')
    data = cursor.fetchall()

    os.system("cls")
    print("Name\t\t\tPeriod\t\t\tYear Discov.\tDiet\t\tAverage Height\t\tAverage Weight")
    
    #Loop for each row retrieved
    for row in data:
        if len(row[1]) > 15: #Formatting fix for long names
            print(f"{row[1]}\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        else:
            print(f"{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        time.sleep(0.1)

#Main Loop
while True:
    print("\nDinosaurs Database:")
    user_input = input("\n1 - Get all dinosaur names\n2 - Get all information\n3 - Exit\n\n>")

    if user_input == "1":
        get_all_dinosaur_names()
    elif user_input == "2":
        get_all_information()
    elif user_input == "3":
        os.system("cls")
        print("Program has stopped")
        break
    else:
        invalid_option_response()

#End the program
conn.commit()
conn.close()