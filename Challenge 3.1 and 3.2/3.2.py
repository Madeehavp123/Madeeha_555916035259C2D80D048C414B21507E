def find_product_indices(product_list, target_product):
    indices = []

    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)

    return indices

products = input("Enter a list of products separated by spaces: ").split()
target_product = input("Enter the product you want to find: ")

result = find_product_indices(products, target_product)

if result:
    print(f"The product '{target_product}' was found at indices: {', '.join(map(str, result))}")
else:
    print(f"The product '{target_product}' was not found in the list.")
