import abc

import numpy as np

from constants.constants import IndicatorType


class BaseStrategy(metaclass=abc.ABCMeta):
    def __init__(self, indicator) -> None:
        """ Get the indicators computation resources."""
        self.indicator = indicator

    @abc.abstractmethod
    def trade_by_indicator(self, 
        indicator_type: IndicatorType) -> Callable[[], np.ndarray]:
        """ Get trading strategy function."""
        pass

    @abc.abstractmethod
    def _get_signals(self) -> np.ndarray:
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
