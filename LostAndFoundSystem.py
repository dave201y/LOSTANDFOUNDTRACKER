import os
from lostitem import LostItem
from datetime import datetime

class LostAndFoundSystem:
    #Constructor
    def __init__(self):
        self.items = []
        self.file_path = "lost_and_found_data.txt"
        self.load_items()
    #add new lost items
    def add_item(self, name, description):
        date_reported = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_item = LostItem(name, description, date_reported)
        self.items.append(new_item)
        self.save_items()
    #view lost inventory
    def view_items(self):
        if not self.items:
            return "No items found in inventory."
        else:
            # Return only item names
            return [item.name for item in self.items]
    
    def get_item_details(self, index):
        """Retrieve full details of an item by index."""
        if 0 <= index < len(self.items):
            item = self.items[index]
            return f"Name: {item.name}\nDescription: {item.description}\nDate Reported: {item.date_reported}"
        return "Item not found."

    def search_item(self, query):
        query = query.lower()# to make it case insenstive 
        for item in self.items:
            if query == item.name.lower() or query in item.description.lower():
                return (f"Name: {item.name}, Description: {item.description}, Date Reported: {item.date_reported}")
        return "Item not found."

    def save_items(self):
        with open(self.file_path, "w") as file:
            for item in self.items:
                file.write(str(item) + "\n")

    def load_items(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    self.items.append(LostItem.create_from_string(line.strip()))
                    
if __name__=='__main__':
    system = LostAndFoundSystem()
    system.add_item("Wallet", "Black leather wallet")
    system.add_item("Phone", "Black iPhone with a cracked screen")

    print("\nAll Items:")
    print(system.view_items())

    print("\nSearch for 'wallet':")
    print(system.search_item("wallet"))

    print("\nSearch for 'Black':")
    print(system.search_item("Black"))

