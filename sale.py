from register import products

# Function to analyze sales of each product and the overall total
def analyze_sales(products):
    total_overall = 0

    # Analyze each product
    for product in products:
        name = product['name']
        unit_price = product['unit_price']
        quantity_sold = product['quantity_sold']
        
        # Calculate the total sales for the current product
        total_product = unit_price * quantity_sold
        product['total_sales'] = total_product
        
        # Add to the overall total
        total_overall += total_product

        # Display product information
        print(f"Product: {name}")
        print(f"  Unit Price: ${unit_price:.2f}")
        print(f"  Quantity Sold: {quantity_sold}")
        print(f"  Total Sales: ${total_product:.2f}")
        print()

    # Display the overall total sales
    print(f"Overall Total Sales: ${total_overall:.2f}")


# Call the function to analyze sales
analyze_sales(products)