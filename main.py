import argparse
import json
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description='Calculate maximum profit from an json file')
    parser.add_argument('input_json', help='Input path for json file')
    args = parser.parse_args()
    
    json_data = None
    with open(args.input_json, 'r') as json_file:
        json_data = json.loads(json_file.read())
    json_data["data"] = json_data["data"][::-1]

    points = []
    for index in json_data["data"]:
        points.append((index["open"], index["quote_date"], True))
        points.append((index["low"], index["quote_date"], False))
        points.append((index["high"], index["quote_date"], False))
        points.append((index["close"], index["quote_date"], False))

    max_profit = 0
    min_val_ix = 0
    min_val = float("inf")
    possible_profits = []
    for i, (value, quote_date, same_day_casual_ordered) in enumerate(points):
        if value < min_val:
            # We need to check if it is not casual ordered
            # that the high value next to this low value
            # is not greater before replacing our min value
            # Basically a one step lookahead
            if not same_day_casual_ordered and len(points) > (i + 1):
                lookahead_ix = i + 1
                profit = points[lookahead_ix][0] - min_val
                if profit > max_profit:
                    max_profit = profit
                    possible_profits.append((min_val_ix, lookahead_ix, max_profit))
            min_val = value
            min_val_ix = i
        elif max_profit < value - min_val:
            # Special case where best profit is found in the
            # same day with high and low, we can not 
            # guarantee ordering and can not include it
            if not same_day_casual_ordered and i == min_val_ix + 1:
                continue
            max_profit = value - min_val
            possible_profits.append((min_val_ix, i, max_profit))
    
    if max_profit == 0:
        print("No suitable date to buy and sell found...")
        return
    
    # The best one
    buy_ix, sell_ix, profit = possible_profits[-1];
    print("buy_ix = %d sell_ix = %d" % (buy_ix, sell_ix))
    print("buy_date = %s sell_date = %s" % (points[buy_ix][1], points[sell_ix][1]))
    print("profit = %f" % (profit))

if __name__== "__main__":
    main()