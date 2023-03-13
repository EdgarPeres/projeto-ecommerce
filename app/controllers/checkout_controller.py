from models import Cart, Payment

class CheckoutController:
    def __init__(self):
        self.cart = Cart()

    def validate_cart(self):
        # Check if the cart is not empty
        if len(self.cart.items) == 0:
            return False, "The cart is empty"

        # Check if all items are available
        for item in self.cart.items:
            if not item.is_available():
                return False, f"The item '{item.name}' is not available"

        return True, ""

    def process_payment(self, payment_method):
        # Validate the cart
        is_valid, error_message = self.validate_cart()
        if not is_valid:
            return False, error_message

        # Create the Payment object
        payment = Payment(self.cart.total_price(), payment_method)

        # Process the payment
        if not payment.process():
            return False, "Payment failed"

        # Clear the cart
        self.cart.clear()

        return True, "Payment successful"