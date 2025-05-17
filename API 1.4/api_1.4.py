import json
# Regular User Input that will be stored as personal info
def personal_info():
    print("Please enter your personal information:")
    personal_info = {
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "address": input("Address: "),
        "phone": input("Phone number: "),
        "email": input("Email: ")
    }
    return personal_info

# Save to JSON file
def save_to_json(info, json_filename):
    with open(json_filename, 'w') as json_file:
        json.dump(info, json_file)
    print(f"\nInfo has been saved to {json_filename}")

# Read from JSON file
def read_from_json(json_filename):
    with open(json_filename, 'r') as json_file:
        info = json.load(json_file)
    return info

def main():
    # Get userinput and store in dictionary
    personal_data = personal_info()
    
    # Converts to JSON string and saves the file
    save_to_json(personal_data, "personal_info.json")
    #test
    #print("Book data loaded from file:", personal_info)

    # Reads the file back and display the data
    print("\nDisplaying the info From the JSON File:")
    info = read_from_json("personal_info.json")
    print("\nPersonal Information:")
    print("\n".join(f"{key.capitalize()}: {value}" for key, value in info.items()))


main()