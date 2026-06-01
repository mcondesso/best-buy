class ProductError(Exception):
    """Custom exception for product-related errors."""


class InvalidQuantityError(ProductError):
    """Raised when an invalid quantity is provided for a product."""


class NotEnoughStockError(ProductError):
    """Raised when trying to buy more than available stock."""


class Product:
    """Represents a product available in the store inventory.

    Attributes:
        name (str): Product name.
        price (float): Unit price of the product.
        quantity (int): Number of units currently in stock.
        active (bool): Whether the product is active and available for purchase.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """Create a new Product instance with validation.

        Args:
            name (str): Product name.
            price (float): Unit price. Must be non-negative.
            quantity (int): Initial stock quantity. Must be non-negative.

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_name(self) -> str:
        """Return the name of the product."""
        return self.name

    def get_quantity(self) -> int:
        """Return the current stock quantity for this product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Update the product stock quantity.

        Args:
            quantity (int): New stock quantity. Must be non-negative.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self) -> bool:
        """Return whether the product is currently active."""
        return self.active

    def activate(self):
        """Mark the product as active and available for purchase."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive and unavailable for purchase."""
        self.active = False

    def show(self):
        """Print a summary of the product details."""
        print(f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Purchase a quantity of the product and reduce stock.

        Args:
            quantity (int): Number of units to buy. Must be positive and no greater than available stock.

        Returns:
            float: Total cost of the purchase.

        Raises:
            InvalidQuantityError: If the requested quantity is not positive.
            NotEnoughStockError: If the requested quantity exceeds available stock.
        """
        if quantity <= 0:
            raise InvalidQuantityError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise NotEnoughStockError("Not enough stock available.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * quantity
