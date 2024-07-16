question1 = input("Do you want to register as a user or an admin , or exit?? (user / admin / exit ) : ").lower()

while question1 not in ['user', 'admin' , 'exit']:
    print("Error! You must enter 'user' , 'admin', or 'exit'.")
    question1 = input("Do you want to register as a user or an admin , or exit?? (user / admin / exit ) : ").lower()

if (question1 == "user"):



    question2 = input("Do you want to sign_up or login ?? ( sign_up / login ) : ").lower()
    while question2 not in ['sign_up', 'login']:
        print("Error! You must enter 'sign_up' or 'login'.")
        question2 = input("Do you want to sign_up or login ?? ( sign_up / login ) : ").lower()

    if (question2 == 'sign_up'):

        with open("List_of_user_information.txt", "a") as f:
            name1 = input("Enter Your first name: ")
            name2 = input("Enter your second name: ")
            name3 = input("Enter Your third name: ")
            name4 = input("Enter Your fourth name: ")

            while not (name1 and name2 and name3 and name4):
                print("Error! You must enter something for all names.")
                name1 = input("Enter Your first name: ")
                name2 = input("Enter your second name: ")
                name3 = input("Enter Your third name: ")
                name4 = input("Enter Your fourth name: ")

            full_name = f"{name1} {name2} {name3} {name4}"
            print("You entered:", name1, name2, name3, name4)


        while True:
            question3 = input("Do you have your own user_id? (yes / no): ").lower()

            if question3== "yes":
                user_id = input("Enter your ID: ")

                if user_id.isdigit():
                    user_id = int(user_id)
                    print("Your ID is:", user_id)
                    break
                else:
                    print("Error! Please enter a valid integer for user_id.")

            elif question3 == "no":
                print("Please contact your administrator or responsible party to obtain your ID.")
                user_id = input("Enter your ID: ")

                if user_id.isdigit():
                    user_id = int(user_id)
                    break
                else:
                    print("Error! Please enter a valid integer for user_id.")

            else:
                print("Error! Please choose yes or no.")

        while True:
            phone_number = input("Enter your phone number (11 digits): ")

            if phone_number.isdigit() and len(phone_number) == 11:         #len() means the length of the variable
                print("You entered a valid phone number:", phone_number)
                break
            else:
                print("Error! Please enter a valid 11-digit integer for phone number.")

        while True:
            national_id = input("Please enter your 14-digit National ID (write it from left to right) : ")

            if national_id.isdigit() and len(national_id) == 14:
                print("Your National ID is:", national_id)
                break

            else:
                print("Error! Please enter a valid 14-digit integer for National ID.")

        while True:
            email = input("Enter your email: ").lower()

            if email and email.endswith(("@gmail.com", "@yahoo.com", "@outlook.com")):


                # Open user data file outside the loop
                with open("list_of_user_information.txt", "r") as user_data:
                    user_data = user_data.read()

                if f"Email: {email}" in user_data:
                    print("Error! This email is already in use. Please use a different email.")
                else:
                    print("You entered a valid email:", email)
                    break  # Break only after both checks are valid

            else:
                print("Error! Please enter a valid email ending with @gmail.com, @yahoo.com, or @outlook.com.")

        while True:
            password = input("Enter your password at least 8 characters long: ")

            # Check if the password is at least 8 characters long
            if len(password) < 8:
                print("Error! Password must be at least 8 characters long. Please try again.")
                continue

            # Check if the password contains a mixture of letters and numbers
            if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
                print("Error! Password must contain a mixture of letters and numbers. Please try again.")
                continue

            confirm_password = input("Confirm your password: ")

            # Check if the confirmed password is not empty
            if not confirm_password:
                print("Error! Please confirm your password.")
                continue

            if password == confirm_password:
                print("Password confirmed!")
                break
            else:
                print("Passwords do not match. Please try again.")

        with open("List_of_user_information.txt", "a") as f:
            f.write(f"Full Name: {full_name}\n")
            f.write(f"User ID: {user_id}\n")
            f.write(f"Phone Number: {phone_number}\n")
            f.write(f"National ID: {national_id}\n")
            f.write(f"Email: {email}\n")
            f.write("_" * 100 + "\n")  # Separator for multiple entries
            f.close()
        with open("List_of_user_emails_and_passwords.txt", "a") as f:
            f.write(f"Email: {email}\n")
            f.write(f"Password: {password}\n")
            f.write("_" * 100 + "\n")  # Separator for multiple entries
            f.close()
        with open("List_of_user_reservation_date.txt", "w") as f:
            f.write(f"Full Name: {full_name}\n")
            f.write(f"User ID: {user_id}\n")
            f.write("_" * 100 + "\n")  # Separator for multiple entries
            f.close()
        print("\n")
        print("welcome" + " " + name1)
        print("\n")
        while True:
            print("\nVaccination Scheduling System Menu:\n")
            print("1. View Vaccination Center list")
            print("2. Reserve Vaccination")
            print("3. View Your Reservation Date")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            print("\n")

            def View_Vaccination_Center_list():
                print("  <<list of Vaccination Centers>>  ")
                print("\n")
                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    Vaccination_Center_data = file.readlines()
                    for line in Vaccination_Center_data:
                        if "Name of the vaccination center" in line or "Vaccination Center id" in line or "Vaccination Center address" in line or "List of vaccines available at the center" in line  or "_" in line:
                            print(line.strip())
                print("\n")
                print("Choose from the following list if you want to do something else\n")


            def Reserve_Vaccination():
                user_id = input("Enter your ID: ")
                while not user_id.isdigit():
                    print("Error! Please enter a valid integer for the user ID.")
                    user_id = input("Enter your ID: ")
                # Convert the ID to an integer
                user_id = int(user_id)

                # Check if the user ID exists in the file
                with open("List_of_user_information.txt", "r") as file:
                    file_content = file.read()

                    if f"User ID: {user_id}" not in file_content:
                        print("Error! User ID does not exist. Reservation cannot be made.")
                        return

                vaccination_center_id = input("Enter the ID of the vaccination center: ")
                while not vaccination_center_id.isdigit():
                    print("Error! Please enter a valid integer for the center ID.")
                    vaccination_center_id = input("Enter the vaccination center ID: ")
                # Convert the ID to an integer
                vaccination_center_id = int(vaccination_center_id)

                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    file_content = file.read()

                    if f"Vaccination Center id: {vaccination_center_id}" not in file_content:
                        print("Error! Vaccination Center ID does not exist. Reservation cannot be made.")
                        return

                vaccine_name = input("Enter the name of the vaccine you want: ")
                while not vaccine_name.isalpha():
                    print("Error! Please enter valid characters for the vaccine name.")
                    vaccine_name = input("Enter the name of the vaccine you want: ")

                # Create a list with user information
                reservation_info = [f"User ID: {user_id}", f"Vaccination Center ID: {vaccination_center_id}",
                                    f"Vaccine Name: {vaccine_name}"]

                with open("List_of_user_information.txt", "r") as file:
                    file_content = file.read()

                    # Check if the search name is in the file content
                    if f"User ID: {user_id}" in file_content:
                        # Extract relevant information based on the search name
                        start_index = file_content.find(f"User ID: {user_id}")
                        end_index = file_content.find("_" * 100, start_index)
                        user_info = file_content[start_index:end_index].strip()

                        # Append the reservation information to the user information
                        user_info += "\nReserve Vaccination: " +"["+ ', '.join(reservation_info)+"]"+"\n"
                        with open("List_of_user_information.txt", "w") as f:
                            f.write(file_content.replace(file_content[start_index:end_index], user_info))

                print(reservation_info)
                print("Reservation successful.")



            def View_Your_Reservation_Date():
                full_name = input(str("Enter your name to View Your Reservation Date: "))
                while not full_name:
                    print("Error! Please enter valid characters for your name.")
                    full_name = input(str("Enter your name to View Your Reservation Date: "))

                user_id = input("Enter your id to View Your Reservation Date: ")

                # Read the entire file content into a string
                with open("List_of_user_reservation_date.txt", "r") as file:
                    user_data = file.read()

                    # Check if the search name is in the file content
                    if f"User ID: {user_id}" in user_data:
                        # Extract relevant information based on the search name
                        start_index = user_data.find(f"User ID: {user_id}")
                        end_index = user_data.find("_" * 100 , start_index)
                        relevant_info = user_data[start_index:end_index].strip()

                        # Print the relevant information
                        print("    <<View Your Reservation Date>>    \n")
                        print("\n")
                        print("Full Name:", full_name)
                        print(relevant_info)
                        print("\n")
                        print("Choose from the following list if you want to do something else\n")
                    else:
                        print(f"No User ID with the id {user_id} found!!\n")
                        print("\nChoose from the following list if you want to do something else\n")





            if choice == "1":
                View_Vaccination_Center_list()

            elif choice == "2":
                Reserve_Vaccination()

            elif choice == "3":
                View_Your_Reservation_Date()

            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


    elif question2 == 'login':

        while True:

            email = input("Enter your email: ").lower()
            if not email:
                print("Error! email cannot be empty. Please try again.")
                continue

            password = input("Enter your password: ")
            if not password:
                print("Error! password cannot be empty. Please try again.")
                continue

            # Check if the user exists in the user information file

            with open("list_of_user_emails_and_passwords.txt", "r") as user_data:

                user_data = user_data.read()

            if f"Email: {email}" in user_data and f"Password: {password}" in user_data:

                print("Login successful!")

                break  # Exit the loop if login is successful

            else:

                print("Login failed. Invalid email or password. Please try again.")

        while True:
            print("\nVaccination Scheduling System Menu:\n")
            print("1. View Vaccination Center list")
            print("2. Reserve Vaccination")
            print("3. View Your Reservation Date")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            print("\n")


            def View_Vaccination_Center_list():
                print("  <<list of Vaccination Centers>>  ")
                print("\n")
                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    Vaccination_Center_data = file.readlines()
                    for line in Vaccination_Center_data:
                        if "Name of the vaccination center" in line or "Vaccination Center id" in line or "Vaccination Center address" in line or "List of vaccines available at the center" in line or "_" in line:
                            print(line.strip())
                print("\n")
                print("Choose from the following list if you want to do something else\n")


            def Reserve_Vaccination():
                user_id = input("Enter your ID: ")
                while not user_id.isdigit():
                    print("Error! Please enter a valid integer for the user ID.")
                    user_id = input("Enter your ID: ")
                # Convert the ID to an integer
                user_id = int(user_id)

                # Check if the user ID exists in the file
                with open("List_of_user_information.txt", "r") as file:
                    file_content = file.read()

                    if f"User ID: {user_id}" not in file_content:
                        print("Error! User ID does not exist. Reservation cannot be made.")
                        return

                vaccination_center_id = input("Enter the ID of the vaccination center: ")
                while not vaccination_center_id.isdigit():
                    print("Error! Please enter a valid integer for the center ID.")
                    vaccination_center_id = input("Enter the vaccination center ID: ")
                # Convert the ID to an integer
                vaccination_center_id = int(vaccination_center_id)

                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    file_content = file.read()

                    if f"Vaccination Center id: {vaccination_center_id}" not in file_content:
                        print("Error! Vaccination Center ID does not exist. Reservation cannot be made.")
                        return

                vaccine_name = input("Enter the name of the vaccine you want: ")
                while not vaccine_name.isalpha():
                    print("Error! Please enter valid characters for the vaccine name.")
                    vaccine_name = input("Enter the name of the vaccine you want: ")

                # Create a list with user information
                reservation_info = [f"User ID: {user_id}", f"Vaccination Center ID: {vaccination_center_id}",
                                    f"Vaccine Name: {vaccine_name}"]

                with open("List_of_user_information.txt", "r") as file:
                    file_content = file.read()

                    # Check if the search name is in the file content
                    if f"User ID: {user_id}" in file_content:
                        # Extract relevant information based on the search name
                        start_index = file_content.find(f"User ID: {user_id}")
                        end_index = file_content.find("_" * 100, start_index)
                        user_info = file_content[start_index:end_index].strip()

                        # Append the reservation information to the user information
                        user_info += "\nReserve Vaccination: " + "[" + ', '.join(reservation_info) + "]" + "\n"
                        with open("List_of_user_information.txt", "w") as f:
                            f.write(file_content.replace(file_content[start_index:end_index], user_info))

                print(reservation_info)
                print("Reservation successful.")


            def View_Your_Reservation_Date():
                full_name = input(str("Enter your name to View Your Reservation Date: "))
                while not full_name:
                    print("Error! Please enter valid characters for your name.")
                    full_name = input(str("Enter your name to View Your Reservation Date: "))

                user_id = input("Enter your id to View Your Reservation Date: ")

                # Read the entire file content into a string
                with open("List_of_user_reservation_date.txt", "r") as file:
                    user_data = file.read()

                    # Check if the search name is in the file content
                    if f"User ID: {user_id}" in user_data:
                        # Extract relevant information based on the search name
                        start_index = user_data.find(f"User ID: {user_id}")
                        end_index = user_data.find("_" * 100, start_index)
                        relevant_info = user_data[start_index:end_index].strip()

                        # Print the relevant information
                        print("    <<View Your Reservation Date>>    \n")
                        print("\n")
                        print("Full Name:", full_name)
                        print(relevant_info)
                        print("\n")
                        print("Choose from the following list if you want to do something else\n")
                    else:
                        print(f"No User ID with the id {user_id} found!!\n")
                        print("\nChoose from the following list if you want to do something else\n")


            if choice == "1":
                View_Vaccination_Center_list()

            elif choice == "2":
                Reserve_Vaccination()

            elif choice == "3":
                View_Your_Reservation_Date()

            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    else :
        print("error!! please choose whether you want to sign_up  or login\n")
        print("**Make sure you write the letters in  small letters**\n")



#---------------------------------------------------------------------------------------


elif (question1=="admin"):
    question2 = input("Do you want to sign_up or login ?? ( sign_up / login ) : ").lower()
    while question2 not in ['sign_up', 'login']:
        print("Error! You must enter 'sign_up' or 'login'.")
        question2 = input("Do you want to sign_up or login ?? ( sign_up / login ) : ").lower()
    if (question2 == 'sign_up'):

        with open("List_of_admin_information.txt", "a") as f:
            name1 = input("Enter Your first name: ")
            name2 = input("Enter your second name: ")
            name3 = input("Enter Your third name: ")
            name4 = input("Enter Your fourth name: ")

            while not (name1 and name2 and name3 and name4):
                print("Error! You must enter something for all names.")
                name1 = input("Enter Your first name: ")
                name2 = input("Enter your second name: ")
                name3 = input("Enter Your third name: ")
                name4 = input("Enter Your fourth name: ")

            full_name = f"{name1} {name2} {name3} {name4}"
            print("You entered:", name1, name2, name3, name4)
        while True:
            question3 = input("Do you have your own user_id? (yes / no): ").lower()

            if question3== "yes":
                user_id = input("Enter your ID: ")

                if user_id.isdigit():
                    user_id = int(user_id)
                    print("Your ID is:", user_id)
                    break
                else:
                    print("Error! Please enter a valid integer for user_id.")

            elif question3 == "no":
                print("Please contact your administrator or responsible party to obtain your ID.")
                user_id = input("Enter your ID: ")

                if user_id.isdigit():
                    user_id = int(user_id)
                    break
                else:
                    print("Error! Please enter a valid integer for user_id.")

            else:
                print("Error! Please choose yes or no.")

        while True:
            email = input("Enter your email: ").lower()

            if email and email.endswith(("@gmail.com", "@yahoo.com", "@outlook.com")):

                # Open user data file outside the loop
                with open("list_of_admin_information.txt", "r") as admin_data:
                    admin_data = admin_data.read()

                if f"Email: {email}" in admin_data:
                    print("Error! This email is already in use. Please use a different email.")
                else:
                    print("You entered a valid email:", email)
                    break  # Break only after both checks are valid

            else:
                print("Error! Please enter a valid email ending with @gmail.com, @yahoo.com, or @outlook.com.")

        while True:
            password = input("Enter your password: ")

            # Check if the password is at least 8 characters long
            if len(password) < 8:
                print("Error! Password must be at least 8 characters long. Please try again.")
                continue

            # Check if the password contains a mixture of letters and numbers
            if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
                print("Error! Password must contain a mixture of letters and numbers. Please try again.")
                continue

            confirm_password = input("Confirm your password: ")

            # Check if the confirmed password is not empty
            if not confirm_password:
                print("Error! Please confirm your password.")
                continue

            if password == confirm_password:
                print("Password confirmed!")
                break
            else:
                print("Passwords do not match. Please try again.")

        with open("List_of_admin_information.txt", "a") as f:
            f.write(f"Full Name: {full_name}\n")
            f.write(f"User ID: {user_id}\n")
            f.write(f"Email: {email}\n")
            f.write("_" * 100 + "\n")  # Separator for multiple entries
            f.close()
        with open("List_of_admin_emails_and_passwords.txt", "a") as f:
            f.write(f"Email: {email}\n")
            f.write(f"Password: {password}\n")
            f.write("_" * 100 + "\n")  # Separator for multiple entries
            f.close()
        print("\n")
        print("welcome"+" "+name1)
        print("\n")
        while True:
            print("Vaccination Scheduling System Menu:\n")
            print("1. Add Vaccination Center")
            print("2. Remove Vaccination Center")
            print("3. Search Vaccination Center")
            print("4. List Registered Users")
            print("5. Add Reservation Date")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")
            print("\n")


            def Addition_process():
                with open("List_of_Vaccination_Center_information.txt", "a") as f:
                    Name_of_the_vaccination_center = input("Enter the name of the vaccination center: ")
                    while not Name_of_the_vaccination_center:
                        print("Error! You must enter something for the name of the vaccination center.")
                        Name_of_the_vaccination_center = input("Enter the name of the vaccination center: ")

                    Vaccination_Center_id = input("Enter the vaccination center ID: ")
                    while not Vaccination_Center_id.isdigit():
                        print("Error! Please enter a valid integer for vaccination center ID.")
                        Vaccination_Center_id = input("Enter the vaccination center ID: ")

                    Vaccination_Center_address = input("Enter the address of the vaccination center: ")
                    while not Vaccination_Center_address:
                        print("Error! You must enter the address of the vaccination center.")
                        Vaccination_Center_address = input("Enter the address of the vaccination center: ")

                    List_of_vaccines_available_at_the_center = input("Enter the list of vaccines available at the center like that -> [  A  ,   B   ,  C   ]: ")
                    while not List_of_vaccines_available_at_the_center:
                        print("Error! You must enter the list of vaccines available at the center.")
                        List_of_vaccines_available_at_the_center = input("Enter the list of vaccines available at the center like that -> [  A  ,   B   ,  C   ]: ")

                    f.write(f"Name of the vaccination center: {Name_of_the_vaccination_center}\n")
                    f.write(f"Vaccination Center id: {Vaccination_Center_id}\n")
                    f.write(f"Vaccination Center address: {Vaccination_Center_address}\n")
                    f.write(f"List of vaccines available at the center: {List_of_vaccines_available_at_the_center}\n")
                    f.write("_" * 100 + "\n")  # Separator for multiple entries
                    f.close()
                    print("Data added successfully\n")

                    print("Choose from the following list if you want to do something else\n")


            def removal_process():
                # Get the vaccination center ID from the user
                vaccination_center_id = input("Enter the vaccination center ID: ")

                # Validate the input to ensure it's a valid integer
                while not vaccination_center_id.isdigit():
                    print("Error! Please enter a valid integer for the center ID.")
                    vaccination_center_id = input("Enter the vaccination center ID: ")

                # Convert the ID to an integer
                vaccination_center_id = int(vaccination_center_id)

                # Read the existing data from the file
                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    vaccination_center_data = file.readlines()

                # Find the index of the line to be removed
                index_to_remove = -1
                for i, line in enumerate(vaccination_center_data):
                    if str(vaccination_center_id) in line:
                        index_to_remove = i
                        break

                # Check if the ID was found
                if index_to_remove != -1:
                    # Calculate start and end indices for lines to be removed
                    start_index = max(0, index_to_remove - 1)
                    end_index = min(index_to_remove + 4, len(vaccination_center_data))

                    # Remove the lines from the list
                    del vaccination_center_data[start_index:end_index]

                    # Write the modified data back to the file
                    with open("List_of_Vaccination_Center_information.txt", "w") as file:
                        file.writelines(vaccination_center_data)

                    print(f"Lines around ID {vaccination_center_id} removed successfully.")
                    print("\n")
                    print("Choose from the following list if you want to do something else\n")
                else:
                    print(f"Vaccination center with ID {vaccination_center_id} not found.")
                    print("\n")
                    print("Choose from the following list if you want to do something else\n")


            def search_process():
                search_name = input("Enter the name of the vaccination center to search: ")
                while not search_name.isalpha():
                    print("Error! Please enter valid characters for the vaccination center name.")
                    vaccine_name = input("Enter the name of the vaccine you want: ")

                # Read the entire file content into a string
                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    file_content = file.read()

                    # Check if the search name is in the file content
                    if f"Name of the vaccination center: {search_name}" in file_content:
                        # Extract relevant information based on the search name
                        start_index = file_content.find(f"Name of the vaccination center: {search_name}")
                        end_index = file_content.find("_" * 100, start_index)
                        relevant_info = file_content[start_index:end_index].strip()

                        # Print the relevant information
                        print("Vaccination Center Information:\n")
                        print(relevant_info)
                        print("\n")
                        print("Choose from the following list if you want to do something else\n")
                    else:
                        print(f"No vaccination center with the name {search_name} found!!\n")
                        print("\nChoose from the following list if you want to do something else\n")


            def list_registered_users():
                print("  <<list of user information>>  ")
                print("\n")
                with open("list_of_user_information.txt", "r") as file:
                    user_data = file.readlines()
                    for line in user_data:
                        if "User ID" in line or "Full Name" in line or "Phone Number" in line or "National ID" in line or "Email" in line or "Reserve_Vaccination" in line or "_" in line:
                            print(line.strip())
                print("\n")
                print("Choose from the following list if you want to do something else\n")


            def add_reservation_date():
                user_id = input("Enter the user ID for who you want to add a reservation date: ")

                while not user_id.isdigit():
                    print("Error! Please enter a valid integer for the user ID.")
                    user_id = input("Enter the user ID for whom you want to add a reservation date: ")

                user_id = int(user_id)
                with open("List_of_user_reservation_date.txt", "r") as file:
                    file_content = file.read()

                    if f"User ID: {user_id}" not in file_content:
                        print("Error! User ID does not exist. Add reservation date cannot be made.")
                        return

                while True:
                    day_of_reservation = input("Enter the day of reservation: ")
                    month_of_reservation = input("Enter the month of reservation: ")
                    year_of_reservation = input("Enter the year of reservation: ")

                    while not (day_of_reservation.isdigit() and month_of_reservation.isdigit() and year_of_reservation.isdigit()):
                        print("Error!! Please enter valid integers for all reservation fields.")
                        day_of_reservation = input("Enter the day of reservation: ")
                        month_of_reservation = input("Enter the month of reservation: ")
                        year_of_reservation = input("Enter the year of reservation: ")

                    # Additional validation for date values
                    day_of_reservation = int(day_of_reservation)
                    month_of_reservation = int(month_of_reservation)
                    year_of_reservation = int(year_of_reservation)

                    if 1 <= month_of_reservation <= 12 and 1 <= day_of_reservation <= 31:
                        break
                    else:
                        print("Error!! Please enter valid values for day, month, and year.")

                with open("List_of_user_reservation_date.txt", "r") as f:
                    lines = f.readlines()
                    found = False

                with open("List_of_user_reservation_date.txt", "w") as f:
                    for line in lines:
                        if f"User ID: {user_id}" in line:
                            found = True
                            f.write(line)
                            f.write(f"Your Reservation Date: ({day_of_reservation}-{month_of_reservation}-{year_of_reservation})\n")
                        else:
                            f.write(line)

                    if found:
                        print(f"Reservation Date ({day_of_reservation}-{month_of_reservation}-{year_of_reservation}) added for User ID {user_id}.")
                        print("\nChoose from the following list if you want to do something else\n")
                    else:
                        print(f"No User data found with ID {user_id}.")
                        print("\nChoose from the following list if you want to do something else\n")


            if choice == "1":
                Addition_process()
            elif choice == "2":
                removal_process()
            elif choice == "3":
                search_process()
            elif choice == "4":
                list_registered_users()
            elif choice == "5":
                add_reservation_date()
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    elif question2 == 'login':

        while True:

            email = input("Enter your email: ").lower()
            if not email:
                print("Error! email cannot be empty. Please try again.")
                continue

            password = input("Enter your password: ")
            if not password:
                print("Error! password cannot be empty. Please try again.")
                continue

            # Check if the user exists in the user information file

            with open("list_of_admin_emails_and_passwords.txt", "r") as admin_data:

                admin_data = admin_data.read()

            if f"Email: {email}" in admin_data and f"Password: {password}" in admin_data:

                print("Login successful!")
                print("\n")

                break  # Exit the loop if login is successful

            else:

                print("Login failed. Invalid email or password. Please try again.")

        while True:
            print("Vaccination Scheduling System Menu:\n")
            print("1. Add Vaccination Center")
            print("2. Remove Vaccination Center")
            print("3. Search Vaccination Center")
            print("4. List Registered Users")
            print("5. Add Reservation Date")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")
            print("\n")


            def Addition_process():
                with open("List_of_Vaccination_Center_information.txt", "a") as f:
                    Name_of_the_vaccination_center = input("Enter the name of the vaccination center: ")
                    while not Name_of_the_vaccination_center:
                        print("Error! You must enter something for the name of the vaccination center.")
                        Name_of_the_vaccination_center = input("Enter the name of the vaccination center: ")

                    Vaccination_Center_id = input("Enter the vaccination center ID: ")
                    while not Vaccination_Center_id.isdigit():
                        print("Error! Please enter a valid integer for vaccination center ID.")
                        Vaccination_Center_id = input("Enter the vaccination center ID: ")

                    Vaccination_Center_address = input("Enter the address of the vaccination center: ")
                    while not Vaccination_Center_address:
                        print("Error! You must enter the address of the vaccination center.")
                        Vaccination_Center_address = input("Enter the address of the vaccination center: ")

                    List_of_vaccines_available_at_the_center = input(
                        "Enter the list of vaccines available at the center like that -> [  A  ,   B   ,  C   ]: ")
                    while not List_of_vaccines_available_at_the_center:
                        print("Error! You must enter the list of vaccines available at the center.")
                        List_of_vaccines_available_at_the_center = input(
                            "Enter the list of vaccines available at the center like that -> [  A  ,   B   ,  C   ]: ")

                    f.write(f"Name of the vaccination center: {Name_of_the_vaccination_center}\n")
                    f.write(f"Vaccination Center id: {Vaccination_Center_id}\n")
                    f.write(f"Vaccination Center address: {Vaccination_Center_address}\n")
                    f.write(f"List of vaccines available at the center: {List_of_vaccines_available_at_the_center}\n")
                    f.write("_" * 100 + "\n")  # Separator for multiple entries
                    f.close()
                    print("Data added successfully\n")

                    print("Choose from the following list if you want to do something else\n")


            def removal_process():
                # Get the vaccination center ID from the user
                vaccination_center_id = input("Enter the vaccination center ID: ")

                # Validate the input to ensure it's a valid integer
                while not vaccination_center_id.isdigit():
                    print("Error! Please enter a valid integer for the center ID.")
                    vaccination_center_id = input("Enter the vaccination center ID: ")

                # Convert the ID to an integer
                vaccination_center_id = int(vaccination_center_id)

                # Read the existing data from the file
                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    vaccination_center_data = file.readlines()

                # Find the index of the line to be removed
                index_to_remove = -1
                for i, line in enumerate(vaccination_center_data):
                    if str(vaccination_center_id) in line:
                        index_to_remove = i
                        break

                # Check if the ID was found
                if index_to_remove != -1:
                    # Calculate start and end indices for lines to be removed
                    start_index = max(0, index_to_remove - 1)
                    end_index = min(index_to_remove + 4, len(vaccination_center_data))

                    # Remove the lines from the list
                    del vaccination_center_data[start_index:end_index]

                    # Write the modified data back to the file
                    with open("List_of_Vaccination_Center_information.txt", "w") as file:
                        file.writelines(vaccination_center_data)

                    print(f"Lines around ID {vaccination_center_id} removed successfully.")
                    print("\n")
                    print("Choose from the following list if you want to do something else\n")
                else:
                    print(f"Vaccination center with ID {vaccination_center_id} not found.")
                    print("\n")
                    print("Choose from the following list if you want to do something else\n")


            def search_process():
                search_name = input("Enter the name of the vaccination center to search: ")
                while not search_name.isalpha():
                    print("Error! Please enter valid characters for the vaccination center name.")
                    vaccine_name = input("Enter the name of the vaccine you want: ")

                # Read the entire file content into a string
                with open("List_of_Vaccination_Center_information.txt", "r") as file:
                    file_content = file.read()

                    # Check if the search name is in the file content
                    if f"Name of the vaccination center: {search_name}" in file_content:
                        # Extract relevant information based on the search name
                        start_index = file_content.find(f"Name of the vaccination center: {search_name}")
                        end_index = file_content.find("_" * 100, start_index)
                        relevant_info = file_content[start_index:end_index].strip()

                        # Print the relevant information
                        print("Vaccination Center Information:\n")
                        print(relevant_info)
                        print("\n")
                        print("Choose from the following list if you want to do something else\n")
                    else:
                        print(f"No vaccination center with the name {search_name} found!!\n")
                        print("\nChoose from the following list if you want to do something else\n")


            def list_registered_users():
                print("  <<list of user information>>  ")
                print("\n")
                with open("list_of_user_information.txt", "r") as file:
                    user_data = file.readlines()
                    for line in user_data:
                        if "User ID" in line or "Full Name" in line or "Phone Number" in line or "National ID" in line or "Email" in line or "Reserve Vaccination" in line or "_" in line:
                            print(line.strip())
                print("\n")
                print("Choose from the following list if you want to do something else\n")


            def add_reservation_date():
                user_id = input("Enter the user ID for who you want to add a reservation date: ")

                while not user_id.isdigit():
                    print("Error! Please enter a valid integer for the user ID.")
                    user_id = input("Enter the user ID for whom you want to add a reservation date: ")

                user_id = int(user_id)
                with open("List_of_user_reservation_date.txt", "r") as file:
                    file_content = file.read()

                    if f"User ID: {user_id}" not in file_content:
                        print("Error! User ID does not exist. Add reservation date cannot be made.")
                        return

                while True:
                    day_of_reservation = input("Enter the day of reservation: ")
                    month_of_reservation = input("Enter the month of reservation: ")
                    year_of_reservation = input("Enter the year of reservation: ")

                    while not (
                            day_of_reservation.isdigit() and month_of_reservation.isdigit() and year_of_reservation.isdigit()):
                        print("Error!! Please enter valid integers for all reservation fields.")
                        day_of_reservation = input("Enter the day of reservation: ")
                        month_of_reservation = input("Enter the month of reservation: ")
                        year_of_reservation = input("Enter the year of reservation: ")

                    # Additional validation for date values
                    day_of_reservation = int(day_of_reservation)
                    month_of_reservation = int(month_of_reservation)
                    year_of_reservation = int(year_of_reservation)

                    if 1 <= month_of_reservation <= 12 and 1 <= day_of_reservation <= 31:
                        break
                    else:
                        print("Error!! Please enter valid values for day, month, and year.")

                with open("List_of_user_reservation_date.txt", "r") as f:
                    lines = f.readlines()
                    found = False

                with open("List_of_user_reservation_date.txt", "w") as f:
                    for line in lines:
                        if f"User ID: {user_id}" in line:
                            found = True
                            f.write(line)
                            f.write(
                                f"Your Reservation Date: ({day_of_reservation}-{month_of_reservation}-{year_of_reservation})\n")
                        else:
                            f.write(line)

                    if found:
                        print(
                            f"Reservation Date ({day_of_reservation}-{month_of_reservation}-{year_of_reservation}) added for User ID {user_id}.")
                        print("\nChoose from the following list if you want to do something else\n")
                    else:
                        print(f"No User data found with ID {user_id}.")
                        print("\nChoose from the following list if you want to do something else\n")


            if choice == "1":
                Addition_process()
            elif choice == "2":
                removal_process()
            elif choice == "3":
                search_process()
            elif choice == "4":
                list_registered_users()
            elif choice == "5":
                add_reservation_date()
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")




    else:
        print("error!! please choose whether you want to sign_up  or login\n")


elif (question1 == "exit"):
    print("Exiting.... the program. Goodbye!")
    # Exit the outer loop to end the program

else:
    print("error!! please choose whether you want to register as a user , an admin or exit\n")

