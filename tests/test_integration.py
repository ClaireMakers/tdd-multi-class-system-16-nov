from lib.shopping_basket import Shopping_basket
from lib.item import Item


"""
When I create an item
I want to be able to add it to teh shopping basket
And check it's in the basket
"""
def test_can_add_item_to_basket(): 
    item = Item("box", 5)
    basket = Shopping_basket()
    basket.add_items(item)
    assert basket.items == [item]


"""
When I create an item
I want to be able to add it to the shopping basket
And then delete it if it was a mistake 
I want to be able to give my delete method the name of the item, and it will find and delete it
"""
def test_can_delete_item_based_on_item_name(): 
    item = Item("box", 5)
    item2 = Item("cookies", 6)
    basket = Shopping_basket()
    basket.add_items(item)
    basket.add_items(item2)
    assert basket.items == [item, item2]
    basket.delete_item("box") 
    assert basket.items == [item2]


"""
I want to be able to sort the items in my basket by price
I want to to sort them by highest or lowest price
"""
def test_can_sort_items_highest_to_lowest():
    item = Item("box", 5)
    item2 = Item("cookies", 6)
    item3 = Item("bread", 10)
    item4 = Item("muffins", 1)
    basket = Shopping_basket()
    basket.add_items(item)
    basket.add_items(item2)
    basket.add_items(item3)
    basket.add_items(item4)
    basket.sort_by_price(True) 
    assert basket.items == [item3, item2, item, item4]

def test_can_sort_items_lowest_to_highest():
    item = Item("box", 5)
    item2 = Item("cookies", 6)
    item3 = Item("bread", 10)
    item4 = Item("muffins", 1)
    basket = Shopping_basket()
    basket.add_items(item)
    basket.add_items(item2)
    basket.add_items(item3)
    basket.add_items(item4)
    basket.sort_by_price(False) 
    assert basket.items == [item4, item, item2, item3]

