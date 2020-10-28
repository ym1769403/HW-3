#Yasir Mushtaque
#1769403

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
            self.item_price * self.item_quantity))

    def print_item_description(self):
        string = self.item_name + ':' + self.item_description;


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for object in self.cart_items:
            if (object.item_name == item_name):
                self.cart_items.remove(object)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        object_found = False
        for object in range(0, len(self.cart_items)):
            if self.cart_items[object].item_name == ItemToPurchase.item_name:
                object_found = True
                self.cart_items[object].item_quantity = ItemToPurchase.item_quantity
                break

        if not object_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for object in self.cart_items:
            num_items = num_items + object.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for object in self.cart_items:
            total_cost = total_cost + (object.item_price * object.item_quantity)
        return total_cost

    def print_total(self):
        if (len(self.cart_items) != 0):
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: " + str(self.get_num_items_in_cart()) + "\n")
            for object in self.cart_items:
                object.print_item_cost()
            print("\nTotal: $" + str(self.get_cost_of_cart()))
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Number of Items: 0")
            print("\nSHOPPING CART IS EMPTY\n")
            print('Total: $0')

    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("\nItem Descriptions")
        for object in self.cart_items:
            object.print_item_description()


def print_menu(self):
    menu = '\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items\' descriptions\no - Output shopping cart\nq - Quit\n'
    option = ''
    while (option != 'q'):
        print(menu)
        option = input('Choose an option:\n')
        while option != 'a' and option != 'o' and option != 'i' and option != 'r' and option != 'c' and option != 'q':
            option = input('Choose an option:\n')

        if option == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            self.add_item(item)

        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            self.remove_item(item_name)

        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name, 0, item_quantity, None)
            self.modify_item(item)

        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()

        elif option == 'o':
            print("OUTPUT SHOPPING CART")
            self.print_total()


if __name__ == '__main__':
    customer_name = input()
    c_date = input()
    sCart = ShoppingCart(customer_name, c_date)

    print("Enter customer's name:")
    print("Enter today's date:")
    print("\nCustomer name: " + sCart.customer_name)
    print("Today's date: " + sCart.current_date)

    print_menu(sCart)