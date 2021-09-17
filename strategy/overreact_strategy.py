from typing import Callable

import numpy as np

from constants.constants import IndicatorType
from strategy.base import BaseStrategy


class OverReactStrategy(BaseStrategy):
    def trade_by_indicator(
            self, indicator_type: IndicatorType) -> Callable[[], np.ndarray]:
        """ Get trading strategy function."""
        if (indicator_type == IndicatorType.RSI):
            return self.trade_by_rsi
        elif (indicator_type == IndicatorType.MFI):
            return self.trade_by_mfi
        elif (indicator_type == IndicatorType.WILLR):
            return self.trade_by_willr
        else:
            raise Exception("The strategy logic is unsupported.")

    def trade_by_mfi(
        self,
        timeperiod: int = 14,
        lowerbound: float = 30,
        upperbound: float = 70,
    ) -> np.ndarray:
        """ Consider overreact duration to be trading time.
            1. buy when mfi is smaller than lower bound
            2. sell when mfi is larger than upper bound

        args:
            timeperiod (int) [unit: times of the data interval]
            lowerbound (float) the lower threshold implies oversold
            upperbound (float) the upper threshold implies overbought

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        mfi = self.indicator.mfi(timeperiod=timeperiod)
        return self._get_signals(mfi,
                                 lowerbound=lowerbound, upperbound=upperbound)

    def trade_by_rsi(
        self,
        timeperiod: int = 14,
        lowerbound: float = 30,
        upperbound: float = 70,
    ) -> np.ndarray:
        """ Consider overreact duration to be trading time.
            1. buy when rsi is smaller than lower bound
            2. sell when rsi is larger than upper bound

        args:
            timeperiod (int) [unit: times of the data interval]
            lowerbound (float) the lower threshold implies oversold
            upperbound (float) the upper threshold implies overbought

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        rsi = self.indicator.rsi(timeperiod=timeperiod)
        return self._get_signals(rsi,
                                 lowerbound=lowerbound, upperbound=upperbound)

    def trade_by_willr(
        self,
        timeperiod: int = 14,
        lowerbound: float = 30,
        upperbound: float = 70,
    ) -> np.ndarray:
        """ Consider overreact duration to be trading time.
            1. buy when willr is smaller than lower bound
            2. sell when willr is larger than upper bound

        args:
            timeperiod (int) [unit: times of the data interval]
            lowerbound (float) the lower threshold implies oversold
            upperbound (float) the upper threshold implies overbought

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        willr = self.indicator.willr(timeperiod=timeperiod)
        return self._get_signals(willr,
                                 lowerbound=lowerbound, upperbound=upperbound)

    def _get_signals(
        self,
        line: np.ndarray,
        lowerbound: float,
        upperbound: float,
    ) -> np.ndarray:
        """
        args:
            line (np.ndarray): line, e.g. 10 MA
            lowerbound (float): threshold for oversold
            upperbound (float): threshold for overbought

        returns:
            singal (np.ndarray): signal for trading points
                                (1 for buying and -1 for selling)
        """
        signal_buy = line < lowerbound
        signal_sell = line > upperbound
        return self._combine_signals(signal_buy, signal_sell)
