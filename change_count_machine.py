#Tyler Coffie
#11/18/2024

def denominations_calc(money_left,dom):
    items = 0
    money_left = round(money_left, 2)  # Round initial value to handle potential precision issues

    while money_left >= dom:
        items += 1
        money_left = round(money_left - dom, 2)  # Subtract and round to avoid errors

    return money_left, items

def main(money):
    denom_list = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    money_left = round(money,2)
    total_items = 0
    loop_val = 0
    while (money_left > 0) and loop_val < len(denom_list):
        [money_left, items] = denominations_calc(money_left,denom_list[loop_val])
        total_items += items
        loop_val += 1
    return total_items



