from products import Product
from store import Store


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


def get_user_choice() -> int:
    """Prompt the user to select a menu option and return their choice."""
    print_menu()
    choice = None
    try:
        choice = int(input("Please choose a number: "))
    except ValueError:
        print("Error with your choice! Try again!")
    if choice < 1 or choice > 4:
        choice = None
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


def start(store: Store):
    """Start the main loop of the store application, allowing the user to interact with the menu."""
    while True:
        choice = get_user_choice()
        if choice is None:
            continue
        elif choice == 4:
            break
        elif choice == 1:
            list_all_products(store)
        elif choice == 2:
            print(f"Total of {store.get_total_quantity()} items in store")
        elif choice == 3:
            print("Ordering is not implemented yet.")


def main():
    best_buy = setup_initial_store()

    start(best_buy)


if __name__ == "__main__":
    main()
