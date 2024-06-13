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

#This function retrieves all the dinosaur names alongside their unique ID index
def get_all_dinosaur_names():
    # Execute an SQL statement and save the result to a variable
    cursor.execute("SELECT DinosaurID, Name FROM DinosaursData;")
    names = cursor.fetchall()

    os.system("cls")
    print("All dinosaur names and their ID:\n")
    
    #Loop for each name retrieved
    for name in names:
        print(f"{name[0]} - {name[1]}")
        time.sleep(0.1)
    print("") #Create space for formatting

#This function retrives all the rows
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

#This function user lets the user retrieve information ofa random dinosaur (a random row)
def get_random_dinosaur_information():
    # Execute an SQL statement and save the result to a variable
    cursor.execute("SELECT * FROM DinosaursData;")
    data = cursor.fetchall()

    os.system("cls")
    print("Name\t\t\tPeriod\t\t\tYear Discov.\tDiet\t\t\tAvg. Height(m)\tAvg. Weight(kg)\n")
    
    #Generate random index value based on how many rows there are
    random_index = random.randint(1, len(data) - 1)
    #Use random index value to choose a row
    row = data[random_index]
    if len(row[1]) > 15: #Formatting fix for long names
        print(f"{row[1]}\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
    else:
        print(f"{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
    print("") #Create space for formatting

#This function is used to let the user create a custom query in a controller environment
#It works by declaring a variable named query, which by the end of the function, will contain an SQL command to be executed
#Throughout the function, the user is asked several question regarding what columns they want to retrieve, filter, and order by
#Numerous independent strings are concatenated with the query variable based on the criteria the user has inputted
#This method prevents SQL injection, and acts as a powerful tool that allows for many different SQL commands to be executed by the user
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
    os.system("cls")
    #Begin ordering phase of query creation
    ordering_phase_start_finished = False
    ordering_phase_end_finished = False
    while not ordering_phase_start_finished:
        while True:
            user_input = input("What column would you like to order the data by?\n1 - Name\n2 - Period\n3 - Year Discov.\n4 - Diet\n5 - Avg. Height\n6 - Avg.Weight\n7 - None\n8 - Cancel\n\n>")
            if user_input == "1":
                query += " ORDER BY Name"
                break
            elif user_input == "2":
                query += " ORDER BY Period"
                break
            elif user_input == "3":
                query += " ORDER BY YearDiscovered"
                break
            elif user_input == "4":
                query += " ORDER BY Diet"
                break
            elif user_input == "5":
                query += " ORDER BY AvgHeight"
                break
            elif user_input == "6":
                query += " ORDER BY AvgWeight"
                break
            elif user_input == "7":
                ordering_phase_end_finished = True
                break
            elif user_input == "8": #Operation cancelled
                os.system("cls")
                return
            else:
                invalid_option_response()
        ordering_phase_start_finished = True
    os.system("cls")
    while not ordering_phase_end_finished:
        while True:
            user_input = input("How would you like to order the chosen column?\n1 - Ascennding\n2 - Descending\n3 - Cancel\n\n>")
            if user_input == "1":
                break
            elif user_input == "2":
                query += " DESC"
                break
            elif user_input == "3":
                os.system("cls")
                return
            else:
                invalid_option_response()
        ordering_phase_end_finished = True            

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

def get_statistics_column():
    #Begin column choosing phase
    os.system("cls")
    #Declare variables for each numerical column
    selecting_year = False
    selecting_height = False
    selecting_weight = False
    while True:
        user_input = input("What numerical column would like to get statistics on?\n1 - Year Discov.\n2 - Avg. Height(m)\n3 - Avg. Weight(kg)\n4 - Cancel\n\n>")
        if user_input == "1":
            selecting_year = True
            break
        elif user_input == "2":
            selecting_height = True
            break
        elif user_input == "3":
            selecting_weight = True
            break
        elif user_input == "4": #Operation cancelled
            os.system("cls")
            return
        else:
            invalid_option_response()
    os.system("cls")
    #Begin statistic choosing phase
    while True:
        user_input = input("What statistics would you like to get?\n1 - Average\n2 - Sum\n3 - Range\n4 - All\n5 - Cancel\nFormat your response with a space between each value\n\n>")
        words = user_input.split()
        #Declare variables for each
        selecting_average = False
        selecting_sum = False
        selecting_range = False
        for i in range(len(words)):
            if words[i] == "1":
                selecting_average = True
            elif words[i] == "2":
                selecting_sum = True
            elif words[i] == "3":
                selecting_range = True
            elif words[i] == "4":
                selecting_average = True
                selecting_sum = True
                selecting_range = True
            elif words[i] == "5": #Operation cancelled
                os.system("cls")
                return
        if selecting_average or selecting_sum or selecting_range:
            break
        else:
            invalid_option_response()
    os.system("cls")
    #Print to the user the column which was chosen
    if selecting_year:
        print("Column selected: Year Discov.\n")
    elif selecting_height:
        print("Column selected: Avg. Height\n")
    else:
        print("Column selected: Avg. Weight\n")
    #Execute SQL statements based on criteria chosen by the user, save the results to a variable, and print results
    if selecting_average:
        if selecting_year:
            cursor.execute("SELECT AVG(YearDiscovered) FROM DinosaursData;")
            result = cursor.fetchall()
            print("Average: " + str(round(result[0][0], 2)))
        elif selecting_height:
            cursor.execute("SELECT AVG(AvgHeight) FROM DinosaursData;")
            result = cursor.fetchall()
            print("Average: " + str(round(result[0][0], 2)) + "m")
        else:
            cursor.execute("SELECT AVG(AvgWeight) FROM DinosaursData;")
            result = cursor.fetchall()
            print("Average: " + str(round(result[0][0], 2)) + "kg")
    if selecting_sum:
        if selecting_year:
            cursor.execute("SELECT SUM(YearDiscovered) FROM DinosaursData;")
            result = cursor.fetchall()
            print("Sum: " + str(result[0][0]))
        elif selecting_height:
            cursor.execute("SELECT SUM(AvgHeight) FROM DinosaursData;")
            result = cursor.fetchall()
            print("Sum: " + str(result[0][0]) + "m")
        else:
            cursor.execute("SELECT SUM(AvgWeight) FROM DinosaursData;")
            result = cursor.fetchall()
            print("Sum: " + str(result[0][0]) + "kg")
    if selecting_range:
        if selecting_year:
            cursor.execute("SELECT MIN(YearDiscovered) FROM DinosaursData;")
            result_min = cursor.fetchall()
            cursor.execute("SELECT MAX(YearDiscovered) FROM DinosaursData;")
            result_max = cursor.fetchall()
            print("Range: " + str(result_max[0][0] - result_min[0][0]) + " (" + str(result_max[0][0]) + " - " + str(result_min[0][0]) + ")")
        elif selecting_height:
            cursor.execute("SELECT MIN(AvgHeight) FROM DinosaursData;")
            result_min = cursor.fetchall()
            cursor.execute("SELECT MAX(AvgHeight) FROM DinosaursData;")
            result_max = cursor.fetchall()
            print("Range: " + str(result_max[0][0] - result_min[0][0]) + "m (" + str(result_max[0][0]) + "m - " + str(result_min[0][0]) + "m)")
        else:
            cursor.execute("SELECT MIN(AvgWeight) FROM DinosaursData;")
            result_min = cursor.fetchall()
            cursor.execute("SELECT MAX(AvgWeight) FROM DinosaursData;")
            result_max = cursor.fetchall()
            print("Range: " + str(result_max[0][0] - result_min[0][0]) + "kg (" + str(result_max[0][0]) + "kg - " + str(result_min[0][0]) + "kg)")
    print("") #Create space for formatting

#This function is used to let the user insert their very own custom dinosaur (row) into the the database (through a controlled environment)
#Several if statements are used to perform checks which restrict the fields of each column. This is done to allow for proper formatting whn data is retrieved
#The user is prompted for the field of each column until they are all equal to an acceptable value
#The new dinosaur is then inserted into the database
#The ID index must be a unique positive integer greater than zero. Its value does not matter otherwise
def insert_custom_dinosaur():
    os.system("cls")
    #Declare variables for the new dinosaur
    new_dinosaur_id = 0
    new_dinosaur_name = "None"
    new_dinosaur_period = "None"
    new_dinosaur_year = 0
    new_dinosaur_diet = "None"
    new_dinosaur_height = 0
    new_dinosaur_weight = 0
    while True:
        if new_dinosaur_id == 0: #Ask for ID
            try:
                new_dinosaur_id = int(input("Enter the ID of your dinosaur (Must be an integer greater than zero):\n\n>"))
                if new_dinosaur_id <= 0:
                    os.system("cls")
                    print("ID must be greater than zero\nTry again")
                    time.sleep(2)
                    os.system("cls")
                    new_dinosaur_id = 0
                else:
                    #Execute SQL query to check if ID index is free
                    cursor.execute("SELECT DinosaurID FROM DinosaursData WHERE DinosaurID = " + str(new_dinosaur_id) + ";")
                    data = cursor.fetchall()
                    if len(data) > 0: #Check if dinosaur ID exists before deletion
                        os.system("cls")
                        print("This ID is already taken\nTry again")
                        time.sleep(2)
                        new_dinosaur_id = 0
                    os.system("cls")
            except ValueError:
                invalid_number_response()
        elif new_dinosaur_name == "None": #Ask for name
            new_dinosaur_name = input("Enter the name of your dinosaur (Min char. of 3) (Max char. of 20):\n\n>").strip()
            if len(new_dinosaur_name) < 3:
                os.system("cls")
                print("Name too short\nTry again")
                time.sleep(3)
                new_dinosaur_name = "None"
            elif len(new_dinosaur_name) < 8: #Increase name length with whitespace for formatting
                new_dinosaur_name += "      "
            if len(new_dinosaur_name) > 20:
                os.system("cls")
                print("Name exceeds character limit\nTry again")
                time.sleep(3)
                new_dinosaur_name = "None"
            os.system("cls")
        elif new_dinosaur_period == "None": #Ask for period
            user_input = input("What period is your dinosaur from?\n\n1 - Triassic\n2 - Jurassic\n3 - Cretaceous\n\n>")
            if user_input == "1":
                new_dinosaur_period = "Triassic"
            elif user_input == "2":
                new_dinosaur_period = "Jurassic"
            elif user_input == "3":
                new_dinosaur_period = "Cretaceous"
            else:
                invalid_option_response()
            os.system("cls")
        elif new_dinosaur_year == 0: #Ask for year
            try:
                new_dinosaur_year = int(input("Enter the year discovered of your dinosaur (Year must be 4 digits long):\n\n>"))
                if len(str(new_dinosaur_year)) != 4:
                    os.system("cls")
                    print("Year must be 4 digits long\nTry again")
                    time.sleep(3)
                    new_dinosaur_year = 0
                os.system("cls")
            except ValueError:
                invalid_number_response()
        elif new_dinosaur_diet == "None": #Ask for diet
            user_input = input("What diet does your dinosaur have?\n\n1 - Carnivore\n2 - Herbivore\n3 - Omnivore\n4 - Piscivore\n\n>")
            if user_input == "1":
                new_dinosaur_diet = "Carnivore"
            elif user_input == "2":
                new_dinosaur_diet = "Herbivore"
            elif user_input == "3":
                new_dinosaur_diet = "Omnivore"
            elif user_input == "4":
                new_dinosaur_diet = "Piscivore"
            else:
                invalid_option_response()
            os.system("cls")
        elif new_dinosaur_height == 0: #Ask for height
            try:
                new_dinosaur_height = int(input("Enter the height(m) of your dinosaur (Max. 100):\n\n>"))
                if new_dinosaur_height <= 0 or new_dinosaur_height > 100:
                    os.system("cls")
                    print("Height must be greater than zero and no bigger than 100\nTry again")
                    time.sleep(4)
                    os.system("cls")
                    new_dinosaur_height = 0
                else:
                    os.system("cls")
            except ValueError:
                invalid_number_response()
        elif new_dinosaur_weight == 0: #Ask for weight
            try:
                new_dinosaur_weight = int(input("Enter the weight(kg) of your dinosaur (Max. 100000):\n\n>"))
                if new_dinosaur_weight <= 0 or new_dinosaur_weight > 100000:
                    os.system("cls")
                    print("Weight must be greater than zero and no bigger than 100000\nTry again")
                    time.sleep(4)
                    os.system("cls")
                    new_dinosaur_weight = 0
                else:
                    os.system("cls")
            except ValueError:
                invalid_number_response()
        else: #All fields filled
            #Prevent SQL injection by using parameterized queries
            query = "INSERT INTO DinosaursData (DinosaurID, Name, Period, YearDiscovered, Diet, AvgHeight, AvgWeight) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (new_dinosaur_id, new_dinosaur_name, new_dinosaur_period, new_dinosaur_year, new_dinosaur_diet, new_dinosaur_height, new_dinosaur_weight))
            conn.commit()
            os.system("cls")
            print("Dinosaur successfully inserted")
            time.sleep(3.5)
            os.system("cls")
            break

#This function lets the user delete a dinosaur (row) from the database
def delete_dinosaur():
    while True:
        try:
            get_all_dinosaur_names()
            #Execute SQL statement based on the ID index and save the results to a variable (no results means invalid ID)
            user_input = int(input("Input the ID number of the dinosaur you would like to delete\n\n>"))
            cursor.execute("SELECT DinosaurID FROM DinosaursData WHERE DinosaurID = " + str(user_input) + ";")
            data = cursor.fetchall()
            if len(data) > 0: #Check if dinosaur ID exists before deletion
                cursor.execute("DELETE FROM DinosaursData WHERE DinosaurID = " + str(data[0][0]))
                conn.commit()
                os.system("cls")
                print("Dinosaur successfully deleted\n\nIts ID index is now free")
                time.sleep(3.5)
                os.system("cls")
                break
            else:
                invalid_option_response()
        except ValueError:
            invalid_number_response()


#Main Loop
while True:
    print("Dinosaurs Database:")
    #Prompt the user for input
    user_input = input("\n1 - Get all dinosaur names (Incl. ID)\n2 - Get all information\n3 - Create advanced query\n4 - Get statistics of a numerical column\n5 - Get a random dinosaur's information\n6 - Insert a custom dinosaur\n7 - Delete a dinosaur\n8 - Exit\n\n>").strip()

    if user_input == "1":
        get_all_dinosaur_names()
    elif user_input == "2":
        get_all_information()
    elif user_input == "3":
        create_query()
    elif user_input == "4":
        get_statistics_column()
    elif user_input == "5":
        get_random_dinosaur_information()
    elif user_input == "6":
        insert_custom_dinosaur()
    elif user_input == "7":
        delete_dinosaur()
    elif user_input == "8":
        os.system("cls")
        print("Program has stopped")
        break
    else:
        invalid_option_response()

#End the program
conn.commit()
conn.close()
exit()