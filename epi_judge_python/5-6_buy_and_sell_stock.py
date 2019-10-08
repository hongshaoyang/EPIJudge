from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # solution - track min price so far and max profit so far
    curr_min_px, max_profit = float("Inf"), 0
    for p in prices:
        if p < curr_min_px:
            curr_min_px = p
        if p - curr_min_px > max_profit:
            max_profit = p - curr_min_px
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
