def format_amount_from_int_to_float(amount: int):
    return float(amount) / 100.0

def format_amount_from_float_to_int(amount: float):
    amount = "%.2f" % float(amount)
    return int(str(amount.replace(".", "").replace(",", "")))
