import os
from datetime import datetime

import pandas as pd

from api.base import BaseApi
from constants.constants import CrawlerColumns


class ApiAdapter(BaseApi):
    def __init__(self, api):
        """ Get the api."""
        self.api = api

    def fetch_candles(self, filename: str, params: dict):
        """ Fetch historical candles data.
        args:
            filename (str): csv filename to be saved
            params (dict): query paramter for requests

        returns:
            complete candles data (pd.DataFrame)
        """

        file_existed = os.path.exists(filename)
        params["isEmpty"] = not file_existed
        if file_existed:
            historical_candles = pd.read_csv(filename)
            last_updates = \
                historical_candles.iloc[-1][CrawlerColumns.DATETIME.value]

            params["start"] = datetime.strptime(
                last_updates,
                "%Y-%m-%d %H:%M:%S",
            )
            params["end"] = datetime.now()

        candles = self.api.fetch_candles(params)
        candles = pd.DataFrame(
            candles,
            columns=[column.value for column in CrawlerColumns],
        )
        candles.to_csv(
            filename,
            mode="a",
            header=(not file_existed),
            index=False,
        )

        candles = pd.read_csv(
            filename, index_col=CrawlerColumns.DATETIME.value)
        candles.index = pd.DatetimeIndex(candles.index.values)
        return candles
