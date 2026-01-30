inventory = {}

def menu(inventory):
    while True:
        print("\n=== COOPMART INVENTORY SYSTEM ===")
        print("1. Add item")
        print("2. Delete item")
        print("3. Search item")
        print("4. Show inventory")
        print("5. Exit")
 
        choice_input = input("Enter choice (1-5): ")
        choice = int(choice_input)
        
        # Input validation
        if choice < 1 or choice > 5:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")
        
        elif choice == 1:
            # Add item
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
                
            # Quantity validation    
            if quantity < 0:
                print("Error: Quantity cannot be negative.")
                continue
            elif item in inventory:
                inventory[item] += quantity
                print(f"Item '{item}' already exists. Quantity updated to {inventory[item]}.")
            else:
                inventory[item] = quantity
                print(f"Item '{item}' added.")
            
        elif choice == 2:
            # Delete item
            item = input("Enter item name: ")
            if item in inventory:
                del inventory[item]
                print(f"Item '{item}' removed.")
            else:
                print(f"Error: Item '{item}' not found.")
            
        elif choice == 3:
            # Search item
            if not inventory:
                print("Inventory is empty.")
                continue
            item = input("Enter item name: ")
            if item in inventory:
                print(f"Quantity of '{item}': {inventory[item]}")
            else:
                print(f"Error: Item '{item}' not found.")
         
        elif choice == 4:
            # Show inventory 
            if not inventory:
                print("Inventory is empty.")
            else:
                print("Inventory:")
                for item, quantity in inventory.items():
                    print(f"{item} {quantity}")
            
        elif choice == 5:
            # Exit 
            print("Goodbye!")
            break 

menu(inventory) 