#Tyler Coffie
#11/18/2024

def dime(money_left):
    items = 0
    money_left = round(money_left, 2)  # Round to handle potential precision issues

    while money_left >= 0.10:  # Continue until less than a dime remains
        items += 1
        money_left = round(money_left - 0.10, 2)  # Subtract and round to avoid floating-point errors

    return money_left, items

def nickel(money_left):
    items = 0
    money_left = round(money_left, 2)  # Round to handle potential precision issues

    while money_left >= 0.05:  # Continue until less than a nickel remains
        items += 1
        money_left = round(money_left - 0.05, 2)  # Subtract and round to avoid floating-point errors

    return money_left, items


def penny(money_left):
    items = 0
    money_left = round(money_left, 2)  # Round to handle potential precision issues

    while money_left >= 0.01:  # Continue until less than a penny remains
        items += 1
        money_left = round(money_left - 0.01, 2)  # Subtract and round to avoid floating-point errors

    return money_left, items

def main(money):
    money_left = round(money, 2)
    total_items = 0  # Track total items

    while money_left > 0:
        money_left, items = dime(money_left)
        total_items += items  # Accumulate items from the dime function

        money_left, items = nickel(money_left)
        total_items += items  # Accumulate items from the nickel function


        money_left, items = penny(money_left)
        total_items += items  # Accumulate items from the penny function
    return total_items








