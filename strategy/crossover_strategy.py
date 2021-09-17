from typing import Callable

import numpy as np

from constants.constants import IndicatorType
from strategy.base import BaseStrategy


class CrossOverStrategy(BaseStrategy):
    def trade_by_indicator(
            self, indicator_type: IndicatorType) -> Callable[[], np.ndarray]:
        """ Get trading strategy function."""
        if (indicator_type == IndicatorType.SMA):
            return self.trade_by_sma
        elif (indicator_type == IndicatorType.EMA):
            return self.trade_by_ema
        elif (indicator_type == IndicatorType.WMA):
            return self.trade_by_wma
        elif (indicator_type == IndicatorType.MACD):
            return self.trade_by_macd
        elif (indicator_type == IndicatorType.MTM):
            return self.trade_by_mtm
        elif (indicator_type == IndicatorType.MTM_MA):
            return self.trade_by_mtm_and_mtm_ma
        elif (indicator_type == IndicatorType.ROC):
            return self.trade_by_roc
        elif (indicator_type == IndicatorType.ROC_MA):
            return self.trade_by_roc_and_roc_ma
        elif (indicator_type == IndicatorType.RSI):
            return self.trade_by_rsi
        elif (indicator_type == IndicatorType.KD):
            return self.trade_by_kd
        else:
            raise Exception("The strategy logic is unsupported.")

    def trade_by_sma(
        self,
        fastperiod: int = 6,
        slowperiod: int = 12,
    ) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when sma_fast upcross sma_slow
            2. sell when sma_fast downcross sma_slow

        args:
            fastperiod (int) [unit: times of the data interval]
            slowperiod (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        sma1 = self.indicator.sma(timeperiod=fastperiod)
        sma2 = self.indicator.sma(timeperiod=slowperiod)
        return self._get_signals(sma1, sma2)

    def trade_by_ema(
        self,
        fastperiod: int = 6,
        slowperiod: int = 12,
    ) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when ema_fast upcross ema_slow
            2. sell when ema_fast downcross ema_slow

        args:
            fastperiod (int) [unit: times of the data interval]
            slowperiod (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        ema1 = self.indicator.ema(timeperiod=fastperiod)
        ema2 = self.indicator.ema(timeperiod=slowperiod)
        return self._get_signals(ema1, ema2)

    def trade_by_wma(
        self,
        fastperiod: int = 6,
        slowperiod: int = 12,
    ) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when wma_fast upcross wma_slow
            2. sell when wma_fast downcross wma_slow

        args:
            fastperiod (int) [unit: times of the data interval]
            slowperiod (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        wma1 = self.indicator.wma(timeperiod=fastperiod)
        wma2 = self.indicator.wma(timeperiod=slowperiod)
        return self._get_signals(wma1, wma2)

    def trade_by_kd(
        self,
        k_period: int = 5,
        d_period: int = 3,
    ) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when d upcorss k
            2. sell when d upcorss k

        args:
            k_period (int) [unit: times of the data interval]
            d_period (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        k, d = self.indicator.kd(k_period=k_period, d_period=d_period)
        return self._get_signals(d, k)

    def trade_by_macd(
        self,
        fastperiod: int = 12,
        slowperiod: int = 26,
        signalperiod: int = 9,
    ) -> np.ndarray:
        macd, macd_signal, macd_hist = self.indicator.macd()
        return self._get_signals(macd, macd_signal)

    def trade_by_mtm(self, timeperiod: int = 10) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when mtm upcross centerline (zero)
            2. sell when mtm downcross centerline (zero)

        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        mtm = self.indicator.mtm(timeperiod=timeperiod)
        centerline = np.zeros_like(mtm)
        return self._get_signals(mtm, centerline)

    def trade_by_mtm_and_mtm_ma(
        self,
        mtm_period: int = 22,
        mtm_ma_period: int = 10,
    ) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when mtm upcross mtm_ma
            2. sell when mtm downcross mtm_ma

        args:
            mtm_period (int) [unit: times of the data interval]
            mtm_ma_period (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        mtm = self.indicator.mtm(timeperiod=mtm_period)
        mtm_ma = self.indicator.ema_with_data(mtm, timeperiod=mtm_ma_period)
        return self._get_signals(mtm, mtm_ma)

    def trade_by_roc(self, timeperiod: int = 10) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when roc upcross centerline (zero)
            2. sell when roc downcross centerline (zero)

        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        roc = self.indicator.roc(timeperiod=timeperiod)
        centerline = np.zeros_like(roc)
        return self._get_signals(roc, centerline)

    def trade_by_roc_and_roc_ma(
        self,
        roc_period: int = 22,
        roc_ma_period: int = 10,
    ) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when roc upcross roc_ma
            2. sell when roc downcross roc_ma

        args:
            roc_period (int) [unit: times of the data interval]
            roc_ma_period (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        roc = self.indicator.roc(timeperiod=roc_period)
        roc_ma = self.indicator.sma_with_data(roc, timeperiod=roc_ma_period)
        return self._get_trading_point(roc, roc_ma)

    def trade_by_rsi(self, timeperiod: int = 14) -> np.ndarray:
        """ Consider crossover points to be trading time.
            1. buy when rsi upcross centerline (fifty)
            2. sell when rsi downcross centerline (fifty)

        args:
            timeperiod (int) [unit: times of the data interval]

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        rsi = self.indicator.rsi(timeperiod=timeperiod)
        centerline = np.ones_like(rsi) * 50
        return self._get_signals(rsi, centerline)

    def _get_signals(
        self,
        fast: np.ndarray,
        slow: np.ndarray,
    ) -> np.ndarray:
        """ Implement signal logic.

        args:
            slow (np.ndarray): slow line, e.g. 20 MA
            fast (np.ndarray): fast line, e.g. 10 MA

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        prev_fast = np.roll(fast, shift=1)
        prev_slow = np.roll(slow, shift=1)
        signal_buy = (fast > slow) & (prev_fast < prev_slow)
        signal_sell = (fast < slow) & (prev_fast > prev_slow)
        return self._combine_signals(signal_buy, signal_sell)
