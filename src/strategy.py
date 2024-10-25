def trading_strategy(predictions, threshold=0.02):
    if predictions[-1] > predictions[-2] * (1 + threshold):
        return "buy"
    elif predictions[-1] < predictions[-2] * (1 - threshold):
        return "sell"
    else:
        return "hold"
