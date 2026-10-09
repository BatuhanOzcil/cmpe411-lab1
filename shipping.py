"""Shipping fee calculator used in Lab 1.

Business rules (the specification you test against):
  1. Weight must be greater than 0 kg and at most 30 kg.
     Any other weight raises ValueError.
  2. Base fee:
       - up to and including 2 kg          -> 30 TL
       - more than 2 kg, up to 10 kg       -> 50 TL
       - more than 10 kg, up to 30 kg      -> 90 TL
  3. Members get 50% off the base fee.
  4. The result is rounded to 2 decimals.
"""


def shipping_fee(weight_kg: float, is_member: bool = False) -> float:
    if weight_kg <= 0 or weight_kg > 30:
        raise ValueError("weight must be in (0, 30] kg")

    if weight_kg < 2:
        fee = 30
    elif weight_kg <= 10:
        fee = 50
    else:
        fee = 90

    if is_member:
        fee = fee * 0.5

    return round(fee, 2)
