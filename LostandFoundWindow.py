from graphics2 import GraphWin, Point, Rectangle, Text, Entry
from LostAndFoundSystem import LostAndFoundSystem


class LostAndFoundApp:
    def __init__(self):
        self.system = LostAndFoundSystem()
        self.win = GraphWin("Lost and Found System", 400, 600)
        self.win.setBackground("lightblue")
        self.setup_ui()
        self.item_buttons = []  # Store item buttons for clickable items

    def setup_ui(self):
        # Title
        title = Text(Point(200, 30), "Lost and Found System")
        title.setSize(18)
        title.setStyle("bold")
        title.draw(self.win)

        # Buttons
        self.add_button = self.create_button(Point(50, 100), Point(150, 140), "Add Item")
        self.view_button = self.create_button(Point(250, 100), Point(350, 140), "View All Items")
        self.search_button = self.create_button(Point(50, 180), Point(150, 220), "Search")

        # Entry fields and label
        self.label = Text(Point(200, 260), "")
        self.label.draw(self.win)
        self.entry = Entry(Point(200, 300), 30)
        self.entry.draw(self.win)

        # Output area
        self.output_area = Text(Point(200, 500), "")
        self.output_area.setSize(10)
        self.output_area.draw(self.win)

    def create_button(self, p1, p2, text):
        rect = Rectangle(p1, p2)
        rect.setFill("white")
        rect.draw(self.win)
        label = Text(rect.getCenter(), text)
        label.draw(self.win)
        return rect, label  # Return both the rectangle and the label

    def create_item_button(self, item_name, index, y_position):
        """Create a clickable button for an item in the list."""
        button = self.create_button(Point(50, y_position), Point(350, y_position + 30), item_name)
        return {"button": button, "item_index": index}

    def check_button_click(self, click, button_tuple):
        rect = button_tuple[0]  # Extract the rectangle from the tuple
        p1, p2 = rect.getP1(), rect.getP2()
        return p1.getX() <= click.getX() <= p2.getX() and p1.getY() <= click.getY() <= p2.getY()

    def reset_ui(self):
        """Reset UI elements to avoid conflicts when interacting with buttons."""
        self.label.setText("")
        self.entry.setText("")
        self.output_area.setText("")
        self.clear_item_buttons()

    def clear_item_buttons(self):
        """Remove all item buttons from the window."""
        for item_button in self.item_buttons:
            item_button["button"].undraw()
        self.item_buttons = []

    def run(self):
        while True:
            click = self.win.getMouse()
            self.reset_ui()  # Reset UI on every click to prevent freezing

            if self.check_button_click(click, self.add_button):
                self.handle_add_item()
            elif self.check_button_click(click, self.view_button):
                self.handle_view_items(click)
            elif self.check_button_click(click, self.search_button):
                self.handle_search()
            else:
                # Check for item button clicks
                self.handle_item_click(click)

    def handle_add_item(self):
        self.label.setText("Enter item name and description:")
        name, description = self.get_two_inputs()
        if name and description:
            self.system.add_item(name, description)
            self.output_area.setText(f"Item '{name}' added successfully!")
        else:
            self.output_area.setText("Invalid input! Please try again.")

    def handle_view_items(self, click=None):
        self.label.setText("Inventory:")
        item_names = self.system.view_items()  # Get only the names
        print(f"Items to display: {item_names}")
        if item_names:
            self.output_area.setText("Click on an item to view details.")
            self.display_items_as_buttons(item_names)
        else:
            self.output_area.setText("No items found in inventory.")

    def display_items_as_buttons(self, items):
        """Display all items as clickable buttons."""
        y_position = 320  # Starting position for item buttons
        for index, name in enumerate(items):  # Use the list of names returned by view_items
            item_button = self.create_item_button(name, index, y_position)  # Use the name for the button
            self.item_buttons.append(item_button)
            y_position += 40  # Increment y-position for the next button

    def handle_item_click(self, click):
        """Handle clicks on individual item buttons."""
        for item_button in self.item_buttons:
            rect, label = item_button["button"]
            if self.check_button_click(click, (rect, label)):
                self.clear_item_buttons()  # Clear buttons and text
                self.display_item_details(item_button["item_index"])  # Show item details
                return

    def clear_item_buttons(self):
        """Remove all item buttons and their labels from the window."""
        for item_button in self.item_buttons:
            rect = item_button["button"][0]  # Extract the rectangle
            label = item_button["button"][1]  # Extract the label
            rect.undraw()  # Undraw the button rectangle
            label.undraw()  # Undraw the label text
        self.item_buttons = []  # Clear the list of buttons

    def display_item_details(self, index):
        """Display full details of a selected item."""
        item_details = self.system.get_item_details(index)
        if item_details:
            self.output_area.setText(f"Item Details:\n{item_details}")
        else:
            self.output_area.setText("Error: Item details not found.")
    
    def handle_search(self):
        self.label.setText("Enter item name or description:")
        query = self.get_input()
        result = self.system.search_item(query)
        if result:
            self.output_area.setText(f"Search Result:\n{result}")
        else:
            self.output_area.setText("No matching items found.")

    def get_input(self):
        self.entry.setText("")
        while True:
            key = self.win.getKey()
            if key == "Return":
                return self.entry.getText().strip()

    def get_two_inputs(self):
        self.label.setText("Enter item name and press Enter:")
        name = self.get_input()
        self.label.setText("Enter item description and press Enter:")
        description = self.get_input()
        return name, description


if __name__ == "__main__":
    app = LostAndFoundApp()
    app.run()
