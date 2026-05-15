from products import Product, ProductError


class StoreError(Exception):
    """Custom exception for store-related errors."""


class OrderError(StoreError):
    """Raised when there is an issue with processing an order."""


class Store:
    """Represents a store that manages a collection of products.

    Attributes:
        products (list[Product]): List of products in the store.
    """

    def __init__(self, products: list[Product]):
        """Initialize the store with a list of products.

        Args:
            products (list): A list of Product instances available in the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """Add a new product to the store inventory.

        Args:
            product (Product): The Product instance to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product_name: str):
        """Remove a product from the store inventory by name.

        Args:
            product_name (str): The name of the product to remove.
        """
        self.products = [p for p in self.products if p.name != product_name]

    def get_total_quantity(self) -> int:
        """Calculate the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list[Product]:
        """Get a list of all active products in the store.

        Returns:
            list: A list of active Product instances.
        """
        return [product for product in self.products if product.is_active()]

    @staticmethod
    def order(shopping_list: list[tuple[Product, int]]) -> float:
        """Calculate the total cost of an order based on a shopping list.

        Args:
            shopping_list: A list of tuples, each tuple contains a Product instance
                and the desired quantity.

        Returns:
            float: The total cost of the order.
        """
        total_cost = 0.0
        for product, quantity in shopping_list:
            try:
                total_cost += product.buy(quantity)
            except ProductError as error:
                raise OrderError(
                    f"Error purchasing '{product.get_name()}': {error}"
                ) from error

        return total_cost
