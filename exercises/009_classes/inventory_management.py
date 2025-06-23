"""Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price,
and methods like add_item, update_item, and check_item_details."""


class Inventory:
    def __init__(self):
        # Store items as {item_id: {item_name, stock_count, price}}
        self.inventory = {}

    def add_item(self):
        item_id = input("Enter item ID: ")
        if item_id in self.inventory:
            print("Item ID already exists. Use update to modify.")
            return
        item_name = input("Enter item name: ")
        try:
            stock_count = int(input("Enter stock count: "))
            price = float(input("Enter price: "))
        except ValueError:
            print("Invalid input for stock or price. Item not added.")
            return
        self.inventory[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }
        print(f"Item '{item_name}' added successfully.")

    def check_item_details(self):
        if not self.inventory:
            print("No items in inventory.")
            return
        print("\nInventory Items:")
        for item_id, info in self.inventory.items():
            print(f"ID: {item_id}")
            print(f"Name: {info['item_name']}")
            print(f"Stock: {info['stock_count']}")
            print(f"Price: Rs.{info['price']:.2f}")
            print("-" * 30)

    def update_item(self):
        if not self.inventory:
            print("No items to update.")
            return

        item_id = input("Enter item ID to update: ")

        if item_id not in self.inventory:
            print("Item ID not found.")
            return

        item_details = self.inventory[item_id]
        new_name = input(f"Enter new name (leave blank to keep '{item_details['item_name']}'): ").strip()
        if new_name:
            item_details['item_name'] = new_name
        try:
            stock_input = input(f"Enter stock count (leave blank to keep {item_details['stock_count']}): ").strip()
            if stock_input:
                stock_count = int(stock_input)
                if stock_count < 0:
                    print("Stock cannot be negative. Update skipped.")
                else:
                    item_details['stock_count'] = stock_count
            price_input = input(f"Enter price (leave blank to keep {item_details['price']}): ").strip()
            if price_input:
                price = float(price_input)
                if price < 0:
                    print("Price cannot be negative. Update skipped.")
                else:
                    item_details['price'] = price
        except ValueError:
            print("Invalid input. Update aborted.")
            return
        print("Item updated successfully.")

    def delete_item(self):
        if not self.inventory:
            print("No items to delete.")
            return
        item_id = input("Enter item ID to delete: ")
        if item_id in self.inventory:
            removed = self.inventory.pop(item_id)
            print(f"Removed item '{removed['item_name']}' from inventory.")
        else:
            print("Item ID not found.")

    def menu(self):
        print("\n====== INVENTORY MENU ======")
        print("1. Display Items")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.check_item_details()
            elif choice == '2':
                self.add_item()
            elif choice == '3':
                self.update_item()
            elif choice == '4':
                self.delete_item()
            elif choice == '5':
                print("Exiting Inventory System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")


inventory = Inventory()
inventory.run()
