def predict_yield(acres):
    yield_per_acre = 2.5
    return round(acres * yield_per_acre, 2)

def estimate_bags(yield_ton):
    bags_per_ton = 20
    return int(yield_ton * bags_per_ton)

def recommend_vehicle(yield_ton):
    if yield_ton <= 5:
        return "Mini Truck"
    elif yield_ton <= 10:
        return "Medium Truck"
    else:
        return "Large Truck"