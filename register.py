# Function to add a product to the product list
def add_product(products, name, unit_price, quantity_sold):
    product = {
        'name': name,
        'unit_price': unit_price,
        'quantity_sold': quantity_sold
    }
    products.append(product)

# Initialize an empty list to hold products
products = []

# Example usage of the function to add products
add_product(products, 'Product A', 10.00, 100)
add_product(products, 'Product B', 20.00, 150)
add_product(products, 'Product C', 15.00, 200)




