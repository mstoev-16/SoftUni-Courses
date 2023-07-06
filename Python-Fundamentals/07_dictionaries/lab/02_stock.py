def search_products(initial_products, searched_products):
    for i in range(0, len(initial_products), 2):
        product = initial_products[i]
        quantity = int(initial_products[i + 1])
        products[product] = quantity

    for product in searched_products:
        if product in products.keys():
            print(f"We have {products[product]} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")


products = {}
product_sequence = input().split()
searched_products = input().split()
search_products(product_sequence, searched_products)
