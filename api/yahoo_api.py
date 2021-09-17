from enum import Enum

import pandas as pd
import yfinance

from api.base import BaseApi
from constants.constants import CrawlerColumns


class YahooFinanceColumns(Enum):
    DATE = "Date"
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
    DIVIDENDS = "Dividends"
    STOCK_SPLITS = "Stock_splits"


class YahooFinanceApi(BaseApi):
    def fetch_candles(self, params):
        """ Fetch historical candles data from yahoo."""
        try:
            if params["isEmpty"]:
                candles = yfinance.Ticker(params["symbol"]).history(
                    period="max",
                )
            else:
                candles = yfinance.Ticker(params["symbol"]).history(
                    start=params["start"],
                    end=params["end"],
                )
            if candles.empty:
                return

            candles.reset_index(level=0, inplace=True)
            candles[CrawlerColumns.DATETIME.value] = \
                candles[YahooFinanceColumns.DATE.value].dt.strftime(
                    "%Y-%m-%d %H:%M:%S")

        except Exception as error:
            raise Exception(error)

        return candles[[column.value for column in CrawlerColumns]]
