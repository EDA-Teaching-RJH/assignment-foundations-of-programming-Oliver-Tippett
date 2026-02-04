def init_database():
    names = ["Spock","Data","Jean-Luc Picard","James T.Kirk","Tuvok"]
    ranks = ["Commander","Lt Commander","Captain","Captain","Lt Commander"]
    divisions = ["Sciences","Operations","Command","Command","Operations"]
    ids = [100, 101, 102, 103, 104]

    return names, ranks, divisions, ids

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

    choice = input("Select Option (1-9): ")
    return choice

def add_member(names, ranks, divisions, ids):
    name = input("Enter your name: ")
    rank = input("Enter your rank: ")
    division = input("Enter your division: ")
    crew_id = input("Enter your Id: ")
    
    if crew_id in ids:
        print("This Id already in use")
        return
    valid_ranks = ["Captain","Commander","Lieutenant","Lt Commander","Ensign"]

    if rank not in valid_ranks:
        print("This rank is not a valid TNG rank")
        return
    
    names.append(name)
    ranks.append(rank)
    divisions.append(division)
    ids.append(crew_id)

    print("Crew member added")

def remove_member(names, ranks, divisions, ids):
    crew_id = int(input("Enter Crew Id to remove: ")) 
    if crew_id not in ids:
        print("This Id is not in the database")
        return
    
    index = ids.index(crew_id)

    names.pop(index)
    ranks.pop(index)
    divisions.pop(index)
    ids.pop(index)

    print("Crew member removed")

def update_rank(names, ranks, ids):
    crew_id = int(input("Enter Id to update members rank: "))
    if crew_id not in ids:
        print("This id is not in the database")
        return
    
    index = ids.index(crew_id)
    new_rank = input("Enter a rank: ")
    ranks[index] = new_rank 
    print(f" {names[index]} has been updated to {new_rank}")

def display_roster(names, ranks, divisions, ids):
    print("Names               |Ranks               |Divisions           |Ids")
    print("--------------------------------------------------------------------")
    for i in range(len(names)):
        print(f"{names[i]:<20}|{ranks[i]:<20}|{divisions[i]:<20}|{ids[i]:<6}")

def search_crew(names, ranks, divisions, ids):
    term = input("Enter a name to search: ")
    for i in range(len(names)):
        if term in names[i]:
            print(f"{names[i]}, {ranks[i]}, {divisions[i]}, {ids[i]}")
            break
        elif term not in names:
            print("Not found")
            break
    

def main():
    names, ranks, divisions, ids = init_database()
    while True:
        choice = display_menu()

        if choice == "1":
            add_member(names, ranks, divisions, ids)
        elif choice == "2": 
            remove_member(names, ranks, divisions, ids)
        elif choice == "3":
            update_rank(names, ranks,ids)
        elif choice == "4":
            display_roster(names, ranks, divisions, ids)
        elif choice == "5":
            search_crew(names, ranks, divisions, ids)
main()