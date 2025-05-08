def conference_signup(*people, **contact_details):
    print("\n---- Conference Registration Summary Thing----")

    if not people:
        print("\nNo participants are registered yet")
    else:
        #Whenevr people are called a number corresponding 
        #to their spot in the tuple will be displayed 
        print("\nPeople")
        for i, name in enumerate(people, 1):
            print(f"{i}. {name}")
    if not contact_details:
        print("\nNo contact details provided.")
    else:
        print("\nContact Details:")
        for contact_type, detail in contact_details.items():
            print(f"{contact_type}: {detail}")

if __name__ == "__main__":
    conference_signup(
        "Alice Smith", 
        "Bob Johnson", 
        "Charlie Brown",
        email="random@example.com",
        phone="111-222-4567"
    )
    #Tests with no contact details
    conference_signup("Dana White", "Eve Black")
    #Tests with no users im so tired 
    conference_signup(email="random@conference.com")
    