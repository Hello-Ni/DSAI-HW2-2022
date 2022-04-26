# DSAI-HW2-2022-AutoTrading

# Data
* NASDAQ:IBM stock prices data
* csv data includes (open、high、low、close)
# Method
## Data preprocessing
we choose stock close price  to predict next day stock open price
## Model
Stock prices is time series, we choose LSTM from tensflow to predict next day stock proce
## predict result
![](./result.png)
# Trader Strategy
* if the prediction of open price is more than last day open price-->
# Execution
python 3.7.0
```
python app.py
```