## Shopping cart problem: 

**We are going to create a shopping basket that lets people add items in.**

### User stories: 

- I want to be able to create shopping items. My items should have a name and a price. 

- I want to be able to get the price or name of the items I create.

- I want to be able to create a shopping basket and add items to it. I also want to be able to delete items from my shopping basket. 

- I also want to be able to sort my items by price, from the highest price to the lowest and vice-versa. 


- What's a class? 
- A class is a blueprint that lets you create multiple similarly structured objects, which are instances. Classes have methods and variables. 


### Design the class system:
What classes?

- Need a way to store the items. list? [] __init__ method? 
- ShoppingBasket class - Item class 

## Testing the Class system: 
Integration test:
- Making sure that everything works together
- Testing that elements of the code that relies on each other work well together

Unit test: 
- A single unit of code on its own (method).

### Create Examples as Integration Tests:
-> Whole system and how it'll be used


"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]


"""
When I create an item
I want to be able to add it to teh shopping basket
And check it's in the basket
"""
item = Item("box", 5)
basket = ShoppingBasket()
basket.add_items(item)
basket.items => [item]


"""
When I create an item
I want to be able to add it to the shopping basket
And then delete it if it was a mistake 
I want to be able to give my delete method the name of the item, and it will find and delete it
"""
item = Item("box", 5)
item2 = Item("cookies", 6)
basket = ShoppingBasket()
basket.add_items(item)
basket.add_items(item2)
basket.delete_item("box") -> in my implementation, I will need to think about how to identify which item to delete


"""
I want to be able to sort the items in my basket by price
I want to to sort them by highest or lowest price
"""
item = Item("box", 5)
item2 = Item("cookies", 6)
basket = ShoppingBasket()
basket.add_items(item)
basket.add_items(item2)
basket.sort_by_item(true) -> the order will be lowest to highest
basket.sort_by_item(false) -> the order will be highest to lowest

basket.item -> [{"name": box, "price": 5}, {}]


### Create Examples as Unit Tests: 
-> Looking at a closer level how each method will be implemented