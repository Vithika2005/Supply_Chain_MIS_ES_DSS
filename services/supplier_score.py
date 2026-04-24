def calculate_supplier_score(supplier):
    score = (
        supplier.quality_score +
        supplier.cost_score +
        supplier.reliability_score
    ) / 3

    return round(score, 2)
