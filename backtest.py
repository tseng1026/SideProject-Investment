import argparse
import importlib

import yaml
from backtesting import Backtest, Strategy

from api import ApiAdapter, BinanceApi, YahooFinanceApi
from constants import ApiType, Config, IndicatorType, StrategyType
from indicator import Indicator
from strategy import CrossOverStrategy, OverReactStrategy


def main(opt):
    module = importlib.import_module(__name__)

    assert opt[Config.API] in ApiType.list(), \
        "The api is unsupported."
    payload = {
        Config.SYMBOL: opt.get(Config.SYMBOL, ""),
        Config.INTERVAL: opt.get(Config.INTERVAL, ""),
    }
    api = getattr(module, opt[Config.API.value])()
    api_adapter = ApiAdapter(api)
    candles = api_adapter.fetch_candles(f'{opt[Config.SYMBOL]}.csv', payload)

    assert opt[Config.STRATEGY] in StrategyType.list(), \
        "The strategy type is unsupported."
    indicator = Indicator(candles)
    strategy = getattr(module, opt[Config.STRATEGY])(indicator)

    assert opt[Config.INDICATOR] in IndicatorType.list(), \
        "The indicator type is unsupported."
    signal = strategy.trade_by_indicator(
        IndicatorType(opt[Config.INDICATOR]))()

    backtest = Backtest(candles, BacktestStrategy,
                        cash=opt.get(Config.CASH, None),
                        commission=opt.get(Config.COMMISSION, None),
                        )
    result = backtest.run(**{"signal": signal})
    backtest.plot()


class BacktestStrategy(Strategy):
    def __init__(self, broker, data, params) -> None:
        """ Setup signal from argument params."""
        self.signal = None
        super().__init__(broker, data, params)

    def init(self):
        """ Add signal as indicators."""
        self.signal = self.I(lambda x: self.signal, "signal")
        super().init()

    def next(self) -> None:
        """ Make strategy decisions."""
        super().next()
        current_signal = self.signal[-1]

        if current_signal > 0:
            self.buy()
        if current_signal < 0:
            self.sell()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    main(config)
