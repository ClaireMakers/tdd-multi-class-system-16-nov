from lib.item import Item 

def test_get_item_name():
    item = Item("item", 6)
    assert item.get_name() == "item"

def test_get_item_price():
    item = Item("item", 6)
    assert item.get_price() == 6