from enum import Enum

import pandas as pd
import requests

from api.base import BaseApi
from constants.constants import CrawlerColumns


class BinanceColumns(Enum):
    OPEN_TIME = "open_time"
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
    CLOSE_TIME = "Close Time"
    QUOTE_ASSET_VOLUME = "Quote Asset Volume"
    NUMBER_OF_TRADES = "Number of Trades"
    TAKER_BUY_BASE_ASSET_VOLUME = "Taker Buy Base Asset Volume"
    TAKER_BUY_QUOTE_ASSET_VOLUME = "Taker Buy Quote Asset Volume"
    IGNORE = "Ignore"


class BinanceApi(BaseApi):
    def fetch_candles(self, params=None):
        """ Fetch historical candles data from binance.
            interval should be:
                1m, 3m, 5m, 15m, 30m,
                1h, 2h, 4h, 6h, 8h, 12h,
                1d, 3d, 1w, 1M
        """
        try:
            payload = {
                "symbol": params["symbol"],
                "interval": params["interval"],
            }
            if params["isEmpty"]:
                payload["limit"] = 1000
            else:
                payload["startTime"] = int(params["start"].timestamp())
                payload["endTime"] = int(params["end"].timestamp())

            response = requests.get(
                "https://api.binance.com/api/v3/klines",
                params=payload,
            )
            response.raise_for_status()
            candles = response.json()
            if candles is None:
                return

            candles = pd.DataFrame(
                candles,
                columns=[column.value for column in BinanceColumns],
            )
            candles[CrawlerColumns.DATETIME.value] = pd.to_datetime(
                candles[BinanceColumns.CLOSE_TIME.value] // 1000,
                unit="s",
            )

        except requests.exceptions.RequestException as error:
            raise Exception(error.response.text)

        return candles[[column.value for column in CrawlerColumns]]
