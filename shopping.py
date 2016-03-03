class Cart:

    def __init__(self):
        self._contents = dict()
        


def get_order():

    print("[command] [item] (command is 'a'dd, 'd'elete, 'p'rint cart, 'q'uit) ")
    line = input()

    command = line[:1]
    item = line[2:]

    return command, item


def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1


def delete_from_cart(item, cart):
    if item in cart and int(cart[item]) > 1:
        cart[item] -= 1
    else:
        del cart[item]


def process_order(order, cart):
    command, item = order

    if command == "a":
        add_to_cart(item, cart)
    elif command == "d" and item in cart:
        delete_from_cart(item, cart)
    elif command == "p":
        print(cart)
    elif command == "q":
        return False

    return True

cart = Cart()

