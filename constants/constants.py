from constants.enum_extension import ExtendedEnum


class Config(str, ExtendedEnum):
    API = "api"
    SYMBOL = "symbol"
    INTERVAL = "interval"
    STRATEGY = "strategy"
    INDICATOR = "indicator"
    CASH = "cash"
    COMMISSION = "commission"


class ApiType(ExtendedEnum):
    BINANCE_API = "BinanceApi"
    YAHOO_API = "YahooFinanceApi"


class StrategyType(ExtendedEnum):
    CROSSOVER_STRATEGY = "CrossOverStrategy"
    OVERREACT_STRATEGY = "OverReactStrategy"


class IndicatorType(ExtendedEnum):
    SMA = "SMA"
    EMA = "EMA"
    WMA = "WMA"
    KD = "KD"
    MACD = "MACD"
    MFI = "MFI"
    MTM = "MTM"
    MTM_MA = "MTM_MA"
    ROC = "ROC"
    ROC_MA = "ROC_MA"
    RSI = "RSI"
    WILLR = "WILLR"


class CrawlerColumns(ExtendedEnum):
    DATETIME = "DateTime"  # millisecond
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
