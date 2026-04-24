def reorder_recommendation(current_stock, forecast, safety_stock=30):
    reorder_qty = forecast - current_stock + safety_stock

    if reorder_qty < 0:
        reorder_qty = 0

    return reorder_qty
