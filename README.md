# **CryptoTrader using Reinforcement learning (RL)**

## Motivation
Based on this [article](https://levelup.gitconnected.com/a-complex-reinforcement-learning-crypto-trading-environment-in-python-134f3faf0d7a), I decided to give it a try and produce my own and try to extract some insights from the cryptocurrency market.

## Initial thoughts and assumptions
- A simple scheme of two steps could be feasible:
1) LightGBM for trend identification and prediction 
2) RL for rewards and decision making .

- The basic variables (open, close, high, low, marketcap, volume) should be enough for a first try. Only variable added is "Performance". Feature engineering can be used for further development and accuracy improvement.

- As explained on this [article](https://towardsdatascience.com/using-reinforcement-learning-to-trade-bitcoin-for-massive-profit-b69d0e8f583b), the time series data is usually not stationary. Therefore, before using LightGBM, the data needs to be differentiated and take the logarithm.

- For the prediction, LightGBM will be fed with data from the 40 days before (following the value provided on [article](https://levelup.gitconnected.com/a-complex-reinforcement-learning-crypto-trading-environment-in-python-134f3faf0d7a)). However, a sensitivity analysis will be carried out with different values.


## Structure
- **prelim_data_works**: Data prelim analysis,visualization and wrangling
Loading crypto historic data (downloaded from [Kaggle and coinmarketcap](https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory)) in a Jupyter notebook, creating some graphs using Plotly and wrangling the data to prepare for machine learning.

- **my_env**


- **my_testing**


_Conclusions_

- After applying the [Augmented Dickey-Fuller test](https://machinelearningmastery.com/time-series-data-stationary-python/), some variables of the coins were stationary. However, it was decided to apply the differentiate and take logarithm to all variables ('High', 'Low', 'Open', 'Close','Volume' and 'Marketcap') except for 'Performance' variable.