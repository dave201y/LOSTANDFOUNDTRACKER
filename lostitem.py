from datetime import datetime

class LostItem:
    def __init__(self, item_name, description, date_reported):
        """
        Create a class for a lost item. 
        
        param:
        item_name(str): name of item.
        description(str): description of the item lost
        date_reported(datetime): date and time the item was reported      
        """
        self.name = item_name
        self.description = description
        self.date_reported = date_reported
     
    @classmethod
    def create_from_string(cls, data):
        """
        Creates a LostItem object from a string.
        
        param:
        data: String representation of a LostItem
        
        return:
        LostItem object
        """
        parts = data.split('|')
        return cls(
            item_name=parts[0],
            description=parts[1],
            date_reported=datetime.strptime(parts[2], "%Y-%m-%d %H:%M:%S")
        )
    
    def __str__(self):
        """
        String representation of the LostItem, formatted for storage.
        """
        return f"{self.name}|{self.description}|{self.date_reported}"
