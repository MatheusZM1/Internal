#Imports go at the top
import sqlite3, os, time, random

#Essentials to connect to the database
conn = sqlite3.connect("DinosaursData")
cursor = conn.cursor()
os.system("cls")

def invalid_option_response():
    os.system("cls")
    print("Invalid option")
    time.sleep(2)
    os.system("cls")

def get_all_dinosaur_names():
    # Execute an SQL statement and save the result to a variable
    cursor.execute("SELECT Name FROM DinosaursData;")
    names = cursor.fetchall()

    os.system("cls")
    print("All dinosaur names:\n")
    
    #Loop for each name retrieved
    for name in names:
        print(f"{name[0]}")
        time.sleep(0.1)

def get_all_information():
    # Execute an SQL statement and save the result to a variable
    cursor.execute("SELECT * FROM DinosaursData;")
    data = cursor.fetchall()

    os.system("cls")
    print("Name\t\t\tPeriod\t\t\tYear Discov.\tDiet\t\t\tAvg. Height(m)\tAvg. Weight(kg)")
    
    #Loop for each row retrieved
    for row in data:
        if len(row[1]) > 15: #Formatting fix for long names
            print(f"{row[1]}\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        else:
            print(f"{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        time.sleep(0.1)

def create_query():
    #Begin advanced query creation
    os.system("cls")
    query = ""
    while query == "": #Loop until a valid column(s) is chosen by the user or this operation is cancelled
        #Prompt the user for input
        print("What columns do you want to retrieve?\n1 - Name\n2 - Period\n3 - Year Discov.\n4 - Diet\n5 - Avg. Height\n6 - Avg.Weight\n7 - All\n8 - Cancel")
        user_input = input("Format your response with a space between each value\n\n>").strip()
        words = user_input.split()
        #Declare variables for each column
        selecting_name = False
        selecting_period = False
        selecting_year = False
        selecting_diet = False
        selecting_height = False
        selecting_weight = False
        #Loop for each value inputted by the user to decide which columns were chosen
        for i in range(len(words)):
            if words[i] == "1":
                selecting_name = True
            elif words[i] == "2":
                selecting_period = True
            elif words[i] == "3":
                selecting_year = True
            elif words[i] == "4":
                selecting_diet = True
            elif words[i] == "5":
                selecting_height = True
            elif words[i] == "6":
                selecting_weight = True
            elif words[i] == "7":
                selecting_name = True
                selecting_period = True
                selecting_year = True
                selecting_diet = True
                selecting_height = True
                selecting_weight = True
                break
            elif words[i] == "8": #Operation cancelled
                os.system("cls")
                return
        #Create SELECT segment of query given columns chosen
        if selecting_name or selecting_period or selecting_year or selecting_diet or selecting_height or selecting_weight:
            one_column_selected = False
            if selecting_name:
                if not one_column_selected:
                    query = "SELECT Name"
                    one_column_selected = True
                else:
                    query += ", Name"
            if selecting_period:
                if not one_column_selected:
                    query = "SELECT Period"
                    one_column_selected = True
                else:
                    query += ", Period"
            if selecting_year:
                if not one_column_selected:
                    query = "SELECT YearDiscovered"
                    one_column_selected = True
                else:
                    query += ", YearDiscovered"
            if selecting_diet:
                if not one_column_selected:
                    query = "SELECT Diet"
                    one_column_selected = True
                else:
                    query += ", Diet"
            if selecting_height:
                if not one_column_selected:
                    query = "SELECT AvgHeight"
                    one_column_selected = True
                else:
                    query += ", AvgHeight"
            if selecting_weight:
                if not one_column_selected:
                    query = "SELECT AvgWeight"
                    one_column_selected = True
                else:
                    query += ", AvgWeight"
            query += " FROM DinosaursData;"
        else:
            invalid_option_response()
    os.system("cls")

    # Execute an SQL statement and save the result to a variable
    cursor.execute(query)
    data = cursor.fetchall()

    if len(data) > 0:
        column_titles = ""
        column_amount = 0

        if selecting_name:
            column_titles += "Name\t\t\t"
            column_amount += 1
        if selecting_period:
            column_titles += "Period\t\t\t"
            column_amount += 1
        if selecting_year:
            column_titles += "Year Discov.\t"
            column_amount += 1
        if selecting_diet:
            column_titles += "Diet\t\t\t"
            column_amount += 1
        if selecting_height:
            column_titles += "Avg. Height(m)\t"
            column_amount += 1
        if selecting_weight:
            column_titles += "Avg. Weight(kg)"
            column_amount += 1

        print(column_titles)

        row_to_print = ""
        for i in range(column_amount):
            row_to_print += "{row[" + str(i) + "]}\t\t"
        
        #Loop for each row retrieved
        for row in data:
            if len(row[0]) > 15 and selecting_name: #Formatting fix for long names
                formatted_string = eval(f"f'{row_to_print}'")
                formatted_string = formatted_string.replace("\t", "", 1) #Remove first spacing when names are long
                print(formatted_string)
            else:
                formatted_string = eval(f"f'{row_to_print}'")
                print(formatted_string)
            time.sleep(0.1)
    else:
        print("No results found for this query.")
    print("\nYour query was: " + query)


#Main Loop
while True:
    print("\nDinosaurs Database:")
    user_input = input("\n1 - Get all dinosaur names\n2 - Get all information\n3 - Create advanced query\n4 - Exit\n\n>")

    if user_input == "1":
        get_all_dinosaur_names()
    elif user_input == "2":
        get_all_information()
    elif user_input == "3":
        create_query()
    elif user_input == "4":
        os.system("cls")
        print("Program has stopped")
        break
    else:
        invalid_option_response()

#End the program
conn.commit()
conn.close()
exit()