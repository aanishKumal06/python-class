def order_food(item, quantity=1, spicy=False):
    return f"Order: {quantity} x {item} (Spicy: {spicy})"


# Using all default values
print(order_food("Momo"))

# Overriding one default value
print(order_food("Chowmein", 2))

# Overriding all default values
print(order_food("Thukpa", 3, True))

# Note: Parameters with default values must come after
# parameters without defaults in the function definition
