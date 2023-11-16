class Shopping_basket: 
    def __init__(self):
        self.items = []
    #Item {
    #"name": "value"
    #"price": number
    #}

    def add_items(self, item): 
        self.items.append(item)


    def delete_item(self, item_name): 
        for item in self.items: 
            if item.name == item_name: 
                self.items.remove(item)

    
    def sort_by_price(self, boolean):
        self.items = sorted(self.items, key=lambda item_list: item_list.price, reverse=boolean)

    