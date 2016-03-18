



class CoinFlipsDiv2:
    def countCoins(self, state):
        s = state[0] + state + state[-1]
        return sum(
            map(
                lambda i: 1 if s[i] != s[i - 1] or s[i] != s[i + 1] else 0,
                range(1, len(s) - 1)
            )
        )


print(CoinFlipsDiv2().countCoins("HT"))

print(list(range(1, 10)))