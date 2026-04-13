# Python CRUD Capstone - Gym Membership System

members = []
plans = []
payments = []

# CREATE FUNCTIONS
def create_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone Number: ")

    member = {
        "member_id": member_id,
        "name": name,
        "age": age,
        "phone": phone
    }

    members.append(member)
    print("Member added successfully!\n")


def create_plan():
    plan_id = input("Enter Plan ID: ")
    plan_name = input("Enter Plan Name: ")
    duration = input("Enter Duration (Months): ")
    price = input("Enter Price: ")

    plan = {
        "plan_id": plan_id,
        "plan_name": plan_name,
        "duration": duration,
        "price": price
    }

    plans.append(plan)
    print("Membership plan added successfully!\n")


def create_payment():
    payment_id = input("Enter Payment ID: ")
    member_id = input("Enter Member ID: ")
    amount = input("Enter Payment Amount: ")
    payment_method = input("Enter Payment Method: ")

    payment = {
        "payment_id": payment_id,
        "member_id": member_id,
        "amount": amount,
        "payment_method": payment_method
    }

    payments.append(payment)
    print("Payment added successfully!\n")


# READ FUNCTIONS
def read_members():
    if len(members) == 0:
        print("No members found.\n")
    else:
        print("\n=== Member List ===")
        for member in members:
            print(f"ID: {member['member_id']}")
            print(f"Name: {member['name']}")
            print(f"Age: {member['age']}")
            print(f"Phone: {member['phone']}")
            print("----------------------")


def read_plans():
    if len(plans) == 0:
        print("No membership plans found.\n")
    else:
        print("\n=== Membership Plan List ===")
        for plan in plans:
            print(f"Plan ID: {plan['plan_id']}")
            print(f"Plan Name: {plan['plan_name']}")
            print(f"Duration: {plan['duration']} months")
            print(f"Price: {plan['price']}")
            print("----------------------")


def read_payments():
    if len(payments) == 0:
        print("No payment records found.\n")
    else:
        print("\n=== Payment List ===")
        for payment in payments:
            print(f"Payment ID: {payment['payment_id']}")
            print(f"Member ID: {payment['member_id']}")
            print(f"Amount: {payment['amount']}")
            print(f"Method: {payment['payment_method']}")
            print("----------------------")

# UPDATE FUNCTIONS
def update_member():
    member_id = input("Enter Member ID to Update: ")

    for member in members:
        if member['member_id'] == member_id:
            member['name'] = input("Enter New Name: ")
            member['age'] = input("Enter New Age: ")
            member['phone'] = input("Enter New Phone Number: ")
            print("Member updated successfully!\n")
            return

    print("Member not found.\n")


def update_plan():
    plan_id = input("Enter Plan ID to Update: ")

    for plan in plans:
        if plan['plan_id'] == plan_id:
            plan['plan_name'] = input("Enter New Plan Name: ")
            plan['duration'] = input("Enter New Duration: ")
            plan['price'] = input("Enter New Price: ")
            print("Membership plan updated successfully!\n")
            return

    print("Plan not found.\n")


def update_payment():
    payment_id = input("Enter Payment ID to Update: ")

    for payment in payments:
        if payment['payment_id'] == payment_id:
            payment['amount'] = input("Enter New Amount: ")
            payment['payment_method'] = input("Enter New Payment Method: ")
            print("Payment updated successfully!\n")
            return

    print("Payment not found.\n")

# DELETE FUNCTIONS
def delete_member():
    member_id = input("Enter Member ID to Delete: ")

    for member in members:
        if member['member_id'] == member_id:
            members.remove(member)
            print("Member deleted successfully!\n")
            return

    print("Member not found.\n")


def delete_plan():
    plan_id = input("Enter Plan ID to Delete: ")

    for plan in plans:
        if plan['plan_id'] == plan_id:
            plans.remove(plan)
            print("Plan deleted successfully!\n")
            return

    print("Plan not found.\n")


def delete_payment():
    payment_id = input("Enter Payment ID to Delete: ")

    for payment in payments:
        if payment['payment_id'] == payment_id:
            payments.remove(payment)
            print("Payment deleted successfully!\n")
            return

    print("Payment not found.\n")

# SEARCH FUNCTION (EXTRA POINT)
def search_member():
    keyword = input("Enter Member Name to Search: ").lower()

    found = False

    for member in members:
        if keyword in member['name'].lower():
            print("\nMember Found:")
            print(f"ID: {member['member_id']}")
            print(f"Name: {member['name']}")
            print(f"Age: {member['age']}")
            print(f"Phone: {member['phone']}")
            found = True

    if not found:
        print("Member not found.\n")

# New Member (CREATE MENU)
def create_menu():
    while True:
        print("\n=== CREATE MENU ===")
        print("1. Add Member")
        print("2. Add Membership Plan")
        print("3. Add Payment")
        print("4. Back to Main Menu")

        choice = input("Choose Menu: ")

        if choice == '1':
            create_member()
        elif choice == '2':
            create_plan()
        elif choice == '3':
            create_payment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Member Information (READ MENU)
def read_menu():
    while True:
        print("\n=== READ MENU ===")
        print("1. View Members")
        print("2. View Membership Plans")
        print("3. View Payments")
        print("4. Search Member")
        print("5. Back to Main Menu")

        choice = input("Choose Menu: ")

        if choice == '1':
            read_members()
        elif choice == '2':
            read_plans()
        elif choice == '3':
            read_payments()
        elif choice == '4':
            search_member()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Update Member Information (UPDATE MENU)
def update_menu():
    while True:
        print("\n=== UPDATE MENU ===")
        print("1. Update Member")
        print("2. Update Membership Plan")
        print("3. Update Payment")
        print("4. Back to Main Menu")

        choice = input("Choose Menu: ")

        if choice == '1':
            update_member()
        elif choice == '2':
            update_plan()
        elif choice == '3':
            update_payment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Delete Member Information (DELETE MENU)
def delete_menu():
    while True:
        print("\n=== DELETE MENU ===")
        print("1. Delete Member")
        print("2. Delete Membership Plan")
        print("3. Delete Payment")
        print("4. Back to Main Menu")

        choice = input("Choose Menu: ")

        if choice == '1':
            delete_member()
        elif choice == '2':
            delete_plan()
        elif choice == '3':
            delete_payment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# MAIN MENU
def main_menu():
    while True:
        print("\n=== GYM MEMBERSHIP SYSTEM ===")
        print("1. New Member")
        print("2. Member Information")
        print("3. Update Member")
        print("4. Delete Member")
        print("5. Exit")

        choice = input("Choose Menu: ")

        if choice == '1':
            create_menu()
        elif choice == '2':
            read_menu()
        elif choice == '3':
            update_menu()
        elif choice == '4':
            delete_menu()
        elif choice == '5':
            print("Thank you for using Gym Membership System!")
            break
        else:
            print("Invalid choice. Please try again.")
#RUN
main_menu()
