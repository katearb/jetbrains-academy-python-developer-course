def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        difference = x % 10
        if difference < 5:
            add_number = 5 - difference
            return x + add_number
        else:
            add_number = 10 - difference
            return x + add_number
