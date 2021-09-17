import abc

import numpy as np


class BaseIndicator(metaclass=abc.ABCMeta):
    def __init__(self, candles):
        """ Get the historical candles data."""
        self.candles = candles

    @abc.abstractmethod
    def bbands(self, timeperiod: int = 5) \
            -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """ Return bollinger bands[upperband, middleband, lowerband]."""
        pass

    @abc.abstractmethod
    def ema(self, timeperiod: int = 30) -> np.ndarray:
        """ Compute exponential moving average."""
        pass

    @abc.abstractmethod
    def ema_with_data(self,
                      data: np.ndarray, timeperiod: int = 14) -> np.ndarray:
        """ Compute exponential moving average of data."""
        pass

    @abc.abstractmethod
    def sma(self, timeperiod: int = 30) -> np.ndarray:
        """ Compute simple moving average."""
        pass

    @abc.abstractmethod
    def sma_with_data(self,
                      data: np.ndarray, timeperiod: int = 14) -> np.ndarray:
        """ Compute simple moving average of data."""
        pass

    @abc.abstractmethod
    def wma(self, timeperiod: int = 30) -> np.ndarray:
        """ Compute weighted moving average."""
        pass

    @abc.abstractmethod
    def wma_with_data(self,
                      data: np.ndarray, timeperiod: int = 14) -> np.ndarray:
        """ Compute weighted moving average of data."""
        pass

    @abc.abstractmethod
    def dmi(self, timeperiod: int = 14) -> np.ndarray:
        """ Compute directional movement index."""
        pass

    @abc.abstractmethod
    def kd(self, k_period: int = 5, d_period: int = 3) -> np.ndarray:
        """ Compute  stochastic oscillator [k, d]."""
        pass

    @abc.abstractmethod
    def macd(self,
             fastperiod: int = 12,
             slowperiod: int = 26,
             signalperiod: int = 9,
             ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """ Compute moving average convergence/divergence
            [macd, macdsignal, macdhist]."""
        pass

    @abc.abstractmethod
    def mfi(self, timeperiod: int = 14) -> np.ndarray:
        """ Compute money flow index."""
        pass

    @abc.abstractmethod
    def mtm(self, timeperiod: int = 10) -> np.ndarray:
        """ Compute momentum."""
        pass

    @abc.abstractmethod
    def roc(self, timeperiod: int = 10) -> np.ndarray:
        """ Compute rate of change."""
        pass

    @abc.abstractmethod
    def rsi(self, timeperiod: int = 14) -> np.ndarray:
        """ Compute rsi."""
        pass

    @abc.abstractmethod
    def willr(self, timeperiod: int = 14) -> np.ndarray:
        """ Compute williams %R."""
        pass
