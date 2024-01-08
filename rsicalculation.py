import numpy as np

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum()/period
    down = -seed[seed < 0].sum()/period
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:period] = 100. - 100./(1. + rs)

    for i in range(period, len(prices)):
        delta = deltas[i - 1]  # cause the diff is 1 shorter

        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(period - 1) + upval)/period
        down = (down*(period - 1) + downval)/period

        rs = up/down
        rsi[i] = 100. - 100./(1. + rs)

    return rsi
need to be integrated into a larger system that handles data fetching, order execution, and other aspects of the trading strategy. 
