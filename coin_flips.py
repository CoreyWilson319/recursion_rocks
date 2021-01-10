# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
coin = ["H", "T"]
opposite_coin = ["H", "T"]


def coin_flips(n):
    if n > 0:
        results = []
        for r in coin:
            for o in opposite_coin:
                results.append(r+o)

        coin_flips(n - 1)

        return results


print(coin_flips(2))
# => ["HH", "HT", "TH", "TT"]
