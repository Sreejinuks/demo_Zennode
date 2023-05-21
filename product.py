
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}


discount_rules = {
    "flat_10_discount": {"threshold": 200, "discount_amount": 10},
    "bulk_5_discount": {"threshold": 10, "discount_percent": 0.05},
    "bulk_10_discount": {"threshold": 20, "discount_percent": 0.1},
    "tiered_50_discount": {"total_threshold": 30, "quantity_threshold": 15, "discount_percent": 0.5}
}


subtotal = 0
quantities = {}
gift_wraps = {}
total_quantity = 0
discount_name = ""
discount_amount = 0
shipping_fee = 0
gift_wrap_fee = 0


for product_name in catalog:
    quantity = int(input(f"Enter the quantity of {product_name}: "))
    is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ")
    quantities[product_name] = quantity
    gift_wraps[product_name] = is_gift_wrapped.lower() == "yes"
    subtotal += catalog[product_name] * quantity
    total_quantity += quantity


for rule, parameters in discount_rules.items():
    if rule == "flat_10_discount" and subtotal > parameters["threshold"]:
        discount_name = rule
        discount_amount = parameters["discount_amount"]
    elif rule == "bulk_5_discount":
        for product_name, quantity in quantities.items():
            if quantity > parameters["threshold"]:
                discount_name = rule
                discount_amount = catalog[product_name] * quantity * parameters["discount_percent"]
                break
    elif rule == "bulk_10_discount" and total_quantity > parameters["threshold"]:
        discount_name = rule
        discount_amount = subtotal * parameters["discount_percent"]
    elif rule == "tiered_50_discount" and total_quantity > parameters["total_threshold"]:
        for product_name, quantity in quantities.items():
            if quantity > parameters["quantity_threshold"]:
                discount_name = rule
                discount_amount = (quantity - parameters["quantity_threshold"]) * catalog[product_name] * parameters["discount_percent"]
                break


for product_name, quantity in quantities.items():
    if gift_wraps[product_name]:
        gift_wrap_fee += quantity


shipping_fee = (total_quantity - 1) // 10 + 1


total = subtotal - discount_amount + gift_wrap_fee + shipping_fee


for product_name, quantity in quantities.items():
    product_total = catalog[product_name] * quantity
    print(f"{product_name}: {quantity} - ${product_total}")

print("Subtotal:", subtotal)
print("Discount applied:", discount_name)
print("Discount amount:", discount_amount)
print("Shipping fee:", shipping_fee)
print("Gift wrap fee:", gift_wrap_fee)
print("Total:",total)