import numpy as np
import talib

from indicator.base import BaseIndicator


class Indicator(BaseIndicator):
    def __init__(self, candles):
        """ Get the historical candles data."""
        self.candles = candles

    def bbands(self,
               timeperiod: int = 5,
               matype: talib.MA_Type = talib.MA_Type.SMA,
               ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        args:
            timeperiod (int) [unit: times of the data interval]
            matype (talib.MA_Type): type of ma

        returns:
            bollinger bands[upperband, middleband, lowerband]
                    (tuple[np.ndarray, np.ndarray, np.ndarray)
        """
        return talib.BBANDS(
            self.candles.Close,
            timeperiod=timeperiod,
            nbdevup=2,
            nbdevdn=2,
            matype=talib.MA_Type.SMA,
        )

    def ema(self, timeperiod: int = 30) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            exponential moving average (np.ndarray)
        """
        return talib.EMA(
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def ema_with_data(self,
                      data: np.ndarray, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            data (np.ndarray)
            timeperiod (int) [unit: times of the data interval]

        returns:
           exponential moving average (np.ndarray)
        """
        return talib.EMA(
            data,
            timeperiod=timeperiod,
        )

    def sma(self, timeperiod: int = 30) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            simple moving average (np.ndarray)
        """
        return talib.SMA(
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def sma_with_data(self,
                      data: np.ndarray, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            data (np.ndarray)
            timeperiod (int) [unit: times of the data interval]

        returns:
            simple moving average (np.ndarray)
        """
        return talib.SMA(
            data,
            timeperiod=timeperiod,
        )

    def wma(self, timeperiod: int = 30) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            weighted moving average (np.ndarray)
        """
        return talib.WMA(
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def wma_with_data(self,
                      data: np.ndarray, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            data (np.ndarray)
            timeperiod (int) [unit: times of the data interval]

        returns:
            weighted moving average (np.ndarray)
        """
        return talib.WMA(
            data,
            timeperiod=timeperiod,
        )

    def dmi(self, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            directional movement index (np.ndarray)
        """
        return talib.DX(
            self.candles.High,
            self.candles.Low,
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def kd(self,
           k_period: int = 5, d_period: int = 3,
           matype: talib.MA_Type = talib.MA_Type.SMA,
           ) -> np.ndarray:
        """
        args:
            k_period (int) [unit: times of the data interval]
            d_period (int) [unit: times of the data interval]
            matype (talib.MA_Type): type of ma

        returns:
            stochastic oscillator[k, d] (tuple[np.ndarray, np.ndarray])
        """
        return talib.STOCHF(
            self.candles.High,
            self.candles.Low,
            self.candles.Close,
            fastk_period=k_period,
            fastd_period=d_period,
            fastd_matype=matype,
        )

    def macd(self,
             fastperiod: int = 12,
             slowperiod: int = 26,
             signalperiod: int = 9,
             ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        args:
            slowperiod (int) [unit: times of the data interval]
            fastperiod (int) [unit: times of the data interval]
            signalperiod (int) [unit: times of the data interval]

        returns:
            moving average convergence/divergence
                [macd, macdsignal, macdhist]
                    (tuple[np.ndarray, np.ndarray, np.ndarray)
        """
        return talib.MACD(
            self.candles.Close,
            fastperiod=fastperiod,
            slowperiod=slowperiod,
            signalperiod=signalperiod,
        )

    def mfi(self, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            money flow index (np.ndarray)
        """
        return talib.MFI(
            self.candles.High,
            self.candles.Low,
            self.candles.Close,
            self.candles.volume,
            timeperiod=timeperiod
        )

    def mtm(self, timeperiod: int = 10) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            momentum (np.ndarray)
        """
        return talib.MOM(
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def roc(self, timeperiod: int = 10) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            rate of change (np.ndarray)
        """
        return talib.ROC(
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def rsi(self, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            relative strength index (np.ndarray)
        """
        return talib.RSI(
            self.candles.Close,
            timeperiod=timeperiod,
        )

    def willr(self, timeperiod: int = 14) -> np.ndarray:
        """
        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            williams %R (np.ndarray)
        """
        return talib.WILLR(
            self.candles.High,
            self.candles.Low,
            self.candles.Close,
            timeperiod=timeperiod
        )
