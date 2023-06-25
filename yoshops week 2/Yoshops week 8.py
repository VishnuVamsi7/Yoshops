import os

def generate_bill(name, phone_no, food_item_no):
    # Calculate the bill amount based on the food item number
    if food_item_no == 1:
        item_name = "Chicken Biryani"
        item_price = 200
    elif food_item_no == 2:
        item_name = "Mutton Biryani"
        item_price = 250
    elif food_item_no == 3:
        item_name = "Veg Biryani"
        item_price = 150
    else:
        print("Invalid food item number.")
        return

    # Generate the bill
    bill = f"Name: {name}\nPhone No: {phone_no}\nFood Item: {item_name}\nPrice: {item_price} INR"

    # Create a directory for bills if it doesn't exist
    directory = "Bills"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the bill to a file inside the directory
    file_name = f"{name}_bill.txt"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(bill)

    print("Bill generated and saved successfully.")

# Example usage
name = input("Enter your name: ")
phone_no = input("Enter your phone number: ")
food_item_no = int(input("Enter the food item number (1: Chicken Biryani, 2: Mutton Biryani, 3: Veg Biryani): "))

generate_bill(name, phone_no, food_item_no)
