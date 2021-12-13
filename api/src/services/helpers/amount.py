def format_amount_from_int_to_float(amount: int) -> float:
    return float(amount) / 100.0

def format_amount_from_float_to_int(amount: float) -> int:
    amount = "%.2f" % float(amount)
    return int(str(amount.replace(".", "").replace(",", "")))
