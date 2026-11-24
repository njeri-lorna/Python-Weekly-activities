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

    # Display product information
    def displayProductDetails(self):
        print("\nProduct Name:", self.name)
        print("Product Code:", self.code)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Stock Value:", self.calculateStockValue())


# Main program
products = []

# Create three product objects
for i in range(3):
    print("\nEnter product", i + 1, "details")

    name = input("Enter product name: ")
    code = input("Enter product code: ")

    # Handle invalid price and quantity
    while True:
        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid input. Enter numbers only.")

    # Create product object
    product = Product()
    product.setProductDetails(name, code, price, quantity)

    # Add product to list
    products.append(product)


# Calculate total stock value
total_value = 0

print("\nSUPERMARKET INVENTORY")

for product in products:
    product.displayProductDetails()
    total_value += product.calculateStockValue()


# Display total value
print("\nTotal Stock Value:", total_value)


# Save inventory to file
f = open("inventory.txt", "w")

for product in products:
    print("Product Name:", product.name, file=f)
    print("Product Code:", product.code, file=f)
    print("Price:", product.price, file=f)
    print("Quantity:", product.quantity, file=f)
    print("Stock Value:", product.calculateStockValue(), file=f)
    print("----------------------", file=f)

print("Total Stock Value:", total_value, file=f)

f.close()

print("\nInventory saved successfully.")
