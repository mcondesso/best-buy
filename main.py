from products import Product
from store import Store, StoreError


def setup_initial_store() -> Store:
    """Set up the initial store with a predefined list of products.

    Returns:
        Store: An instance of the Store class initialized with a list of products.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    return Store(product_list)


def print_menu():
    """Print the main menu options for the store application."""
    print()
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def get_user_choice() -> int | None:
    """Prompt the user to select a menu option and return their choice."""
    print_menu()
    choice = None
    try:
        choice = int(input("Please choose a number: "))
        if choice < 1 or choice > 4:
            choice = None
    except ValueError:
        print("Error with your choice! Try again!")
    return choice


def list_all_products(store: Store):
    """Print a list of all active products in the store.

    Args:
        store (Store): The Store instance from which to retrieve and display products.
    """
    print("------")
    for i, product in enumerate(store.get_all_products()):
        print(f"{i + 1}. ", end="")
        product.show()
    print("------")


def get_product_number(num_products: int) -> int | None:
    """Prompt the user to select a product number from the list.

    Args:
        num_products (int): The total number of products available.

    Returns:
        int | None: The selected product number (1-based), or None if user cancels.
    """
    while True:
        choice = input("Which product # do you want? ")
        if not choice:
            return None
        try:
            choice = int(choice)
            if 1 <= choice <= num_products:
                return choice
            raise ValueError()
        except ValueError:
            print("Invalid choice. Please enter the number of the product you want.")


def get_product_quantity(max_quantity: int) -> int | None:
    """Prompt the user to enter the quantity for a product.

    Args:
        max_quantity (int): The maximum available quantity for the product.

    Returns:
        int | None: The selected quantity, or None if user cancels.
    """
    while True:
        choice = input(f"What amount do you want? We have {max_quantity} available: ")
        if not choice:
            return None
        try:
            choice = int(choice)
            if 0 < choice <= max_quantity:
                return choice
            raise ValueError()
        except ValueError:
            print(
                f"Invalid quantity. Please pick between 1 and {max_quantity} (available amount)."
            )


def make_order(store: Store):
    """Prompt the user to create an order by selecting products and quantities.

    Args:
        store (Store): The Store instance from which to retrieve products for the order.
    """
    list_all_products(store)
    print("When you want to finish order, enter empty text.")
    total_order = []
    products = store.get_all_products()
    while True:
        product_number = get_product_number(len(products))
        if product_number is None:
            break
        selected_product = products[product_number - 1]
        product_quantity = get_product_quantity(selected_product.get_quantity())
        if product_quantity is None:
            break
        total_order.append((selected_product, product_quantity))
        print("Product added to list!")

    print("********")
    try:
        total_cost = store.order(total_order)
        print(f"Order made! Total payment: ${total_cost:.2f}")
    except StoreError as error:
        print(error)


def start(store: Store):
    """Start the main loop of the store application, allowing the user to interact with the menu."""
    while True:
        choice = get_user_choice()
        if choice is None:
            continue
        if choice == 4:
            break
        if choice == 1:
            list_all_products(store)
        elif choice == 2:
            print(f"Total of {store.get_total_quantity()} items in store")
        elif choice == 3:
            make_order(store)


def main():
    """Main entry point for the Best Buy store application.

    Sets up the initial store and starts the interactive menu loop.
    """
    best_buy = setup_initial_store()

    start(best_buy)


if __name__ == "__main__":
    main()
