# COOPMART Inventory System
# A simple console program to manage grocery store inventory

def show_menu():
    print("\n=== COOPMART INVENTORY SYSTEM ===")
    print("1. Add item")
    print("2. Delete item")
    print("3. Check stock levels")
    print("4. View all inventory")
    print("5. Exit")

def add_item(inventory):
    item = input("Enter item name: ").strip()
    if not item:
        print("Error: Item name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid number for quantity.")
        return

    if item in inventory:
        inventory[item] += quantity
        print(f"Item '{item}' already exists. Quantity updated to {inventory[item]}.")
    else:
        inventory[item] = quantity
        print(f"Item '{item}' added successfully.")

def delete_item(inventory):
    item = input("Enter item name: ").strip()
    if not item:
        print("Error: Item name cannot be empty.")
        return

    if item not in inventory:
        print(f"Error: Item '{item}' not found in inventory.")
    else:
        del inventory[item]
        print(f"Item '{item}' removed successfully.")

def check_stock_levels(inventory):
    item = input("Enter item name: ").strip()
    if not item:
        print("Error: Item name cannot be empty.")
        return

    if item not in inventory:
        print(f"Error: Item '{item}' not found in inventory.")
    else:
        print(f"Stock level of '{item}': {inventory[item]}")

def view_all_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        print("-" * 30)
        for item, quantity in inventory.items():
            print(f"{item:<20} {quantity:>8}")
        print("-" * 30)

def main():
    inventory = {}

    while True:
        show_menu()
        try:
            choice = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Error: Please enter a valid number between 1 and 5.")
            continue

        if choice < 1 or choice > 5:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_item(inventory)
        elif choice == 2:
            delete_item(inventory)
        elif choice == 3:
            check_stock_levels(inventory)
        elif choice == 4:
            view_all_inventory(inventory)
        elif choice == 5:
            print("Thank you for using COOPMART Inventory System. Goodbye!")
            break

if __name__ == "__main__":
    main()