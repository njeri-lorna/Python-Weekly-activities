
# Create Product class
class Product:

    # Set product details
    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    # Calculate stock value
    def calculateStockValue(self):
        return self.price * self.quantity

    # Display product details
    def displayProductDetails(self):
        print("\nProduct Name:", self.name)
        print("Product Code:", self.code)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Stock Value:", self.calculateStockValue())


# Main program
product1 = Product()

# Set product information
product1.setProductDetails(
    "Laptop",
    "P001",
    50000,
    10
)

# Display product details
product1.displayProductDetails()
