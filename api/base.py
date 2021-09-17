import abc

import pandas as pd


class BaseApi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_candles(self, payload: dict = None) -> pd.DataFrame:
        """ Fetch historical candles data."""
        pass
