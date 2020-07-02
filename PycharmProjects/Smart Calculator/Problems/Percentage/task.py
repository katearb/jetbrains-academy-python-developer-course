def get_percentage(number, round_digits=None):
    percentage = number * 100
    if round_digits is None:
        return str(int(percentage)) + '%'
    else:
        return str(round(percentage, round_digits)) + '%'
