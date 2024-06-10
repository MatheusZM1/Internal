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

def invalid_number_response():
    os.system("cls")
    print("Invalid number")
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
    print("") #Create space for formatting

def get_all_information():
    # Execute an SQL statement and save the result to a variable
    cursor.execute("SELECT * FROM DinosaursData;")
    data = cursor.fetchall()

    os.system("cls")
    print("Name\t\t\tPeriod\t\t\tYear Discov.\tDiet\t\t\tAvg. Height(m)\tAvg. Weight(kg)\n")
    
    #Loop for each row retrieved
    for row in data:
        if len(row[1]) > 15: #Formatting fix for long names
            print(f"{row[1]}\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        else:
            print(f"{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        time.sleep(0.1)
    print("") #Create space for formatting

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
                query = "SELECT Name"
                one_column_selected = True
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
            query += " FROM DinosaursData"
        else:
            invalid_option_response()
    os.system("cls")
    #Begin filtering phase of query creation
    filtering_phase_finished = False
    while not filtering_phase_finished:
        print("What columns do you want to filter?\n1 - Name\n2 - Period\n3 - Year Discov.\n4 - Diet\n5 - Avg. Height\n6 - Avg.Weight\n7 - All\n8 - None\n9 - Cancel")
        user_input = input("Format your response with a space between each value\n\n>").strip()
        words = user_input.split()
        #Declare variables for each column
        filtering_name = False
        filtering_period = False
        filtering_year = False
        filtering_diet = False
        filtering_height = False
        filtering_weight = False
        #Loop for each value inputted by the user to decide which columns were chosen to be filtered by
        for i in range(len(words)):
            if words[i] == "1":
                filtering_name = True
            elif words[i] == "2":
                filtering_period = True
            elif words[i] == "3":
                filtering_year = True
            elif words[i] == "4":
                filtering_diet = True
            elif words[i] == "5":
                filtering_height = True
            elif words[i] == "6":
                filtering_weight = True
            elif words[i] == "7":
                filtering_name = True
                filtering_period = True
                filtering_year = True
                filtering_diet = True
                filtering_height = True
                filtering_weight = True
                break
            elif words[i] == "8": #Filter by nothing (override)
                filtering_phase_finished = True
                break
            elif words[i] == "9": #Operation cancelled
                os.system("cls")
                return
        if filtering_name or filtering_period or filtering_year or filtering_diet or filtering_height or filtering_weight:
            one_filter_selected = False
            if filtering_name: #Name column is being filtered
                os.system("cls")
                while True: #Loop until the column is properly filtered
                    user_input = input("How would you like to filter names?\n1 - Starts with _\n2 - Contains _\n3 - Ends with _\n4 - Cancel\n\n>").strip()
                    os.system("cls")
                    if user_input == "1":
                        user_input = input("What sequence of characters should names start with?\n\n>").lower().strip()
                        query += " WHERE Name LIKE '" + user_input + "%'"
                        break
                    elif user_input == "2":
                        user_input = input("What sequence of characters should names contain?\n\n>").lower().strip()
                        query += " WHERE Name LIKE '%" + user_input + "%'"
                        break
                    elif user_input == "3":
                        user_input = input("What sequence of characters should names end with?\n\n>").lower().strip()
                        query += " WHERE Name LIKE '%" + user_input + "'"
                        break
                    elif user_input == "4":
                        return
                    else:
                        invalid_option_response()
                one_filter_selected = True
            if filtering_period: #Period column is being filtered
                os.system("cls")
                while True: #Loop until the column is properly filtered
                    user_input = input("What periods would you like to include?\n1 - Triassic only\n2 - Jurassic only\n3 - Cretaceous only\n4 - Triassic & Jurassic\n5 - Triassic & Cretaceous\n6 - Jurassic & Cretaceous\n7 - Cancel\n\n>").strip()
                    if user_input == "1":
                        if not one_filter_selected:
                            query += " WHERE Period = 'Triassic'"
                        else:
                            query += " AND Period = 'Triassic'"
                        break
                    elif user_input == "2":
                        if not one_filter_selected:
                            query += " WHERE Period = 'Jurassic'"
                        else:
                            query += " AND Period = 'Jurassic'"
                        break
                    elif user_input == "3":
                        if not one_filter_selected:
                            query += " WHERE Period = 'Cretaceous'"
                        else:
                            query += " AND Period = 'Cretaceous'"
                        break
                    elif user_input == "4":
                        if not one_filter_selected:
                            query += " WHERE Period != 'Cretaceous'"
                        else:
                            query += " AND Period != 'Cretaceous'"
                        break
                    elif user_input == "5":
                        if not one_filter_selected:
                            query += " WHERE Period != 'Jurassic'"
                        else:
                            query += " AND Period != 'Jurassic'"
                        break
                    elif user_input == "6":
                        if not one_filter_selected:
                            query += " WHERE Period != 'Triassic'"
                        else:
                            query += " AND Period != 'Triassic'"
                        break
                    else:
                        invalid_option_response()
                one_filter_selected = True
            if filtering_year: #Year column is being filtered
                os.system("cls")
                user_input = ""
                while True: #Loop until the column is properly filtered
                    if user_input == "": #Ask for input only if an option has not been selected already
                        user_input = input("How would you like to filter years discovered?\n1 - Before _ year\n2 - After _ year\n3 - In range of years _ to _\n4 - Equal to _ year\n5 - Cancel\n\n>").strip()
                    os.system("cls")
                    if user_input == "1":
                        try: 
                            year_value = int(input("Before what year should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE YearDiscovered < " + str(year_value)
                            else:
                                query += " AND YearDiscovered < " + str(year_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "2":
                        try: 
                            year_value = int(input("After what year should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE YearDiscovered > " + str(year_value)
                            else:
                                query += " AND YearDiscovered > " + str(year_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "3":
                        year_value_low = 0
                        while year_value_low == 0: #Loop until the min year value is valid (equal to 0 until then)
                            try: 
                                year_value_low = int(input("After what year should the results be?\n\n>").strip())
                                if not one_filter_selected:
                                    query += " WHERE YearDiscovered > " + str(year_value_low)
                                else:
                                    query += " AND YearDiscovered > " + str(year_value_low)
                                break
                            except ValueError:
                                invalid_number_response()
                        os.system("cls")
                        year_value_high = 0
                        while year_value_high == 0: #Loop until the max year value is greater than the lowest (equal to 0 until then)
                            try: 
                                year_value_high = int(input("And before what year should the results be?\n\n>").strip())
                                if year_value_high <= year_value_low + 1:
                                    os.system("cls")
                                    print("The maximum year value needs to be greater than the lowest year value\nYour lowest year value is 1 year after " + str(year_value_low) + "\nTry again")
                                    time.sleep(7)
                                    os.system("cls")
                                    year_value_high = 0
                                else:
                                    query += " AND YearDiscovered < " + str(year_value_high)
                                    break
                            except ValueError:
                                invalid_number_response()
                        break
                    elif user_input == "4":
                        try: 
                            year_value = int(input("What year should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE YearDiscovered = " + str(year_value)
                            else:
                                query += " AND YearDiscovered = " + str(year_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "5":
                        return
                    else:
                        invalid_option_response()
                one_filter_selected = True
            if filtering_diet: #Diet column is being filtered
                os.system("cls")
                while True: #Loop until the column is properly filtered
                    print("What diets would you like to include?\n1 - Carnivore\n2 - Herbivore\n3 - Omnivore\n4 - Piscivore\n5 - Cancel")
                    user_input = input("Format your response with a space between each value\n\n>").strip()
                    words = user_input.split()
                    #Declare variables for each column
                    selecting_carnivore = False
                    selecting_herbivore = False
                    selecting_omnivore = False
                    selecting_piscivore = False
                    #Loop for each value inputted by the user to decide which diets were chosen
                    for i in range(len(words)):
                        if words[i] == "1":
                            selecting_carnivore = True
                        elif words[i] == "2":
                            selecting_herbivore = True
                        elif words[i] == "3":
                            selecting_omnivore = True
                        elif words[i] == "4":
                            selecting_piscivore = True
                        elif words[i] == "5": #Operation cancelled
                            os.system("cls")
                            return
                    if selecting_carnivore or selecting_herbivore or selecting_omnivore or selecting_piscivore:
                        one_diet_filtered = False
                        if selecting_carnivore:
                            if not one_filter_selected:
                                query += " WHERE (Diet = 'Carnivore'"
                            else:
                                query += " AND (Diet = 'Carnivore'"
                            one_filter_selected = True
                            one_diet_filtered = True
                        if selecting_herbivore:
                            if not one_filter_selected:
                                query += " WHERE (Diet = 'Herbivore'"
                            else:
                                if not one_diet_filtered:
                                    query += " AND (Diet = 'Herbivore'"
                                else:
                                    query += " OR Diet = 'Herbivore'"
                            one_filter_selected = True
                            one_diet_filtered = True
                        if selecting_omnivore:
                            if not one_filter_selected:
                                query += " WHERE (Diet = 'Omnivore'"
                            else:
                                if not one_diet_filtered:
                                    query += " AND (Diet = 'Omnivore'"
                                else:
                                    query += " OR Diet = 'Omnivore'"
                            one_filter_selected = True
                            one_diet_filtered = True
                        if selecting_piscivore:
                            if not one_filter_selected:
                                query += " WHERE (Diet = 'Piscivore'"
                            else:
                                if not one_diet_filtered:
                                    query += " AND (Diet = 'Omnivore'"
                                else:
                                    query += " OR Diet = 'Omnivore'"
                            one_filter_selected = True
                            one_diet_filtered = True
                        query += ")"
                        break
                    elif not (selecting_carnivore and selecting_herbivore and selecting_omnivore and selecting_piscivore):
                        invalid_option_response()
                one_filter_selected = True
            if filtering_height: #Height column is being filtered
                os.system("cls")
                user_input = ""
                while True: #Loop until the column is properly filtered
                    if user_input == "": #Ask for input only if an option has not been selected already
                        user_input = input("How would you like to filter average height?\n1 - Shorter than _ metres\n2 - Taller than _ metres\n3 - In range of metres _ to _\n4 - Equal to _ metres\n5 - Cancel\n\n>").strip()
                    os.system("cls")
                    if user_input == "1":
                        try: 
                            height_value = float(input("Shorter than how many metres should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE AvgHeight < " + str(height_value)
                            else:
                                query += " AND AvgHeight < " + str(height_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "2":
                        try: 
                            height_value = float(input("Taller than how many metres should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE AvgHeight > " + str(height_value)
                            else:
                                query += " AND AvgHeight > " + str(height_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "3":
                        height_value_low = 0
                        while height_value_low == 0: #Loop until the min height value is valid (equal to 0 until then)
                            try: 
                                height_value_low = float(input("Taller than how many metres should the results be?\n\n>").strip())
                                if not one_filter_selected:
                                    query += " WHERE AvgHeight > " + str(height_value_low)
                                else:
                                    query += " AND AvgHeight > " + str(height_value_low)
                                break
                            except ValueError:
                                invalid_number_response()
                        os.system("cls")
                        height_value_high = 0
                        while height_value_high == 0: #Loop until the max height value is greater than the lowest (equal to 0 until then)
                            try: 
                                height_value_high = float(input("And shorter than how many metres should the results be?\n\n>").strip())
                                if height_value_high <= height_value_low:
                                    os.system("cls")
                                    print("The maximum height value needs to be greater than the lowest height value\nYour lowest height value is greater than " + str(height_value_low) + "\nTry again")
                                    time.sleep(7)
                                    os.system("cls")
                                    height_value_high = 0
                                else:
                                    query += " AND AvgHeight < " + str(height_value_high)
                                    break
                            except ValueError:
                                invalid_number_response()
                        break
                    elif user_input == "4":
                        try: 
                            height_value = float(input("What height should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE AvgHeight = " + str(height_value)
                            else:
                                query += " AND AvgHeight = " + str(height_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "5":
                        return
                    else:
                        invalid_option_response()
                one_filter_selected = True
            if filtering_weight: #Weight column is being filtered
                os.system("cls")
                user_input = ""
                while True: #Loop until the column is properly filtered
                    if user_input == "": #Ask for input only if an option has not been selected already
                        user_input = input("How would you like to filter average weight?\n1 - Lighter than _ kilograms\n2 - Heavier than _ kilograms\n3 - In range of kilograms _ to _\n4 - Equal to _ kilograms\n5 - Cancel\n\n>").strip()
                    os.system("cls")
                    if user_input == "1":
                        try: 
                            weight_value = float(input("Lighter than how many kilograms should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE AvgWeight < " + str(weight_value)
                            else:
                                query += " AND AvgWeight < " + str(weight_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "2":
                        try: 
                            weight_value = float(input("Heavier than how many kilograms should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE AvgWeight > " + str(weight_value)
                            else:
                                query += " AND AvgWeight > " + str(weight_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "3":
                        weight_value_low = 0
                        while weight_value_low == 0: #Loop until the min height value is valid (equal to 0 until then)
                            try: 
                                weight_value_low = float(input("Heavier than how many kilograms should the results be?\n\n>").strip())
                                if not one_filter_selected:
                                    query += " WHERE AvgWeight > " + str(weight_value_low)
                                else:
                                    query += " AND AvgWeight > " + str(weight_value_low)
                                break
                            except ValueError:
                                invalid_number_response()
                        os.system("cls")
                        weight_value_high = 0
                        while weight_value_high == 0: #Loop until the max height value is greater than the lowest (equal to 0 until then)
                            try: 
                                weight_value_high = float(input("And lighter than how many kilograms should the results be?\n\n>").strip())
                                if weight_value_high <= weight_value_low:
                                    os.system("cls")
                                    print("The maximum weight value needs to be greater than the lowest weight value\nYour lowest weight value is greater than " + str(weight_value_low) + "\nTry again")
                                    time.sleep(7)
                                    os.system("cls")
                                    weight_value_high = 0
                                else:
                                    query += " AND AvgWeight < " + str(weight_value_high)
                                    break
                            except ValueError:
                                invalid_number_response()
                        break
                    elif user_input == "4":
                        try: 
                            weight_value = float(input("What weight should the results be?\n\n>").strip())
                            if not one_filter_selected:
                                query += " WHERE AvgWeight = " + str(weight_value)
                            else:
                                query += " AND AvgWeight = " + str(weight_value)
                            break
                        except ValueError:
                            invalid_number_response()
                    elif user_input == "5":
                        return
                    else:
                        invalid_option_response()
                one_filter_selected = True
            filtering_phase_finished = True
        else:
            if not filtering_phase_finished: #Invalid option message unless the filtering phase was skipped
                invalid_option_response()

    # Execute an SQL statement and save the result to a variable
    os.system("cls")
    query += ";"
    cursor.execute(query)
    data = cursor.fetchall()

    if len(data) > 0: #Query results contain data
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

        print(column_titles + "\n")

        row_to_print = ""
        for i in range(column_amount):
            row_to_print += "{row[" + str(i) + "]}\t\t"
        
        #Loop for each row retrieved
        for row in data:
            if selecting_name: #Formatting fix for long names
                if len(row[0]) > 15:
                    formatted_string = eval(f"f'{row_to_print}'")
                    formatted_string = formatted_string.replace("\t", "", 1) #Remove first spacing when names are long
                    print(formatted_string)
                else:
                    formatted_string = eval(f"f'{row_to_print}'")
                    print(formatted_string)
            else:
                formatted_string = eval(f"f'{row_to_print}'")
                print(formatted_string)
            time.sleep(0.1)
    else: #Query results contain no data
        print("No results found for this query.")
    #Inform user of their query
    print("\nYour query was: " + query + "\n")


#Main Loop
while True:
    print("Dinosaurs Database:")
    #Prompt the user for input
    user_input = input("\n1 - Get all dinosaur names\n2 - Get all information\n3 - Create advanced query\n4 - Exit\n\n>").strip()

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