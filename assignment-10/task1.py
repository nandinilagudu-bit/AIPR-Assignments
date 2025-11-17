def discount(price, category):
    if category == "student":
        rate = 0.9 if price > 1000 else 0.95
    else:
        rate = 0.85 if price > 2000 else 1.0
    return price * rate
print(discount(2000,"student"))


def discount(price, category):
    if category == "student":
        if price > 1000:
            return price * 0.9
        else:
            return price * 0.95
    else:
        if price > 2000:
            return price * 0.85
        else:
            return price

print(discount(2000,"student"))
