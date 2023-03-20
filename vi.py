enter_order = int(input("Insert the order base cost in AUD:\t"))
enter_order_type = int(input("enter order type 1 for dine in, 2 for pick up, 3 for deivery:\t"))

order_charges = {
        1: ["dine in", 8],
        2: ["pick up", 0],
        3: ["delivery", 10]
    }

print(enter_order + (enter_order * (order_charges[enter_order_type][1]*0.01)))
