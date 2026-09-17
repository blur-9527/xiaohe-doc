def calculate_total(products):
    total = 0
    for product in products:
        total += product[1]
    return "{:.1f}".format(total)
products = eval(input())
result = calculate_total(products)
print(result)

