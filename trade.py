class Trading():
    def __init__(self, hold, stock, last_day):
        self.hold = hold                # holding prices
        self.stock = stock              # Own stock or not
        self.last = last_day            # Save yesterdays prices
        self.action = []                # Save operation log

    def act(self, prices):
        for i in range(prices.shape[0] - 1):
            self.last = prices[i]
            if i == 0:
                self.action.append(0)
            else:
                if self.stock == 1:
                    if prices[i + 1] >= self.hold + 0:
                        self.hold = 0
                        self.action.append(-1)
                        self.stock -= 1
                    else:
                        self.action.append(0)

                elif self.stock == 0:
                    if prices[i + 1] < self.last:
                        self.hold = prices[i + 1]
                        self.action.append(1)
                        self.stock += 1
                    elif prices[i + 1] > self.last:
                        self.hold = prices[i + 1]
                        self.action.append(-1)
                        self.stock -= 1
                    else:
                        self.action.append(0)

                elif self.stock == -1:
                    self.hold = 0
                    self.action.append(1)
                    self.stock += 1
                else:
                    self.action.append(0)

        return self.action
