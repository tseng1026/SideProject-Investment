# SideProject-Investment

## About The Project

Implement investing strategy and find when to buy or sell the stock.

## Getting Started
### Prerequisites
To setup the environment, install `pipenv` by running the following script (if you use Mac). For other devices, the instruction is in the [link](https://github.com/pypa/pipenv).
```shell
  brew install pipenv
```

### Installation
To create the environment, run the following script from the root of your project’s directory (where it includes the file `pipfile.lock`.
```shell
  pipenv install
```

To activate the environment, run the following script from the root of your project’s directory (where it includes the file `pipfile.lock`.
```shell
  pipenv shell
```

## Usage
Modify `config.yaml` if you needed and quick implement by the following script.
```shell
  python backtesting --config config.yaml
```

Get the candles by other third-party by inherit `BaseApi` in the file `api/base`; `fetch_candles` returns pandas dataframe with columns described by `CrawlerColumns` in the file `constants/constants`.
```python
class BaseApi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_candles(self, payload: dict = None) -> pd.DataFrame:
        """ Fetch historical candles data."""
        pass
```

Modify new investing strategy by inherit `BaseStrategy` in the file `strategy/base`; `trade_by_indicator` returns the method that implement your strategy with numpy array as output. 
```python
class BaseStrategy(metaclass=abc.ABCMeta):
    def __init__(self, indicator) -> None:
        """ Get the indicators computation resources."""
        self.indicator = indicator

    @abc.abstractmethod
    def trade_by_indicator(self, indicator_type: IndicatorType):
        """ Get trading strategy function."""
        pass

    @abc.abstractmethod
    def _get_signals(self):
        """ Implement signal logic."""
        pass

    def _combine_signals(
        self,
        signal_buy: np.ndarray,
        signal_sell: np.ndarray,
    ) -> np.ndarray:
        """
        args:
            signal_buy (np.ndarray): signal for buying
            signal_sell (np.ndarray): signal for selling

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        return signal_buy.astype(int) - signal_sell.astype(int)
```

## Authors
Scarlett Tseng

## License
Theis is released under the under terms of the  [MIT License](https://github.com/tseng1026/SideProject-Investment/blob/master/LICENSE) .
