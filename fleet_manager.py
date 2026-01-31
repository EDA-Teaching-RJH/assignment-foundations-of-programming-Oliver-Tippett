def init_database():
    names = ["Spock","Data","Jean-Luc Picard","James T.Kirk","Tuvok"]
    ranks = ["First Officer","Operations Officer","Captain","Captain","Security"]
    division = ["Science","Operations","Command","Command","Operations"]
    ids = ["100","101","102","103","104"]

    return names, ranks, division, ids

def display_menu():
    user = input("Enter your full name: ")
    print("Current student logged in is",user)
    print("1. Add Crew Member")
    print("2. Remove Crew Member")
    print("3. Update Rank")
    print("4. Display Crew Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")

    choice = input("Select Option (1-9)")
    return choice