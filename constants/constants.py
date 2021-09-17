from enum import Enum


class DataSource(Enum):
    BINANCE = "binance"


class CrawlerColumns(Enum):
    DATETIME = "DateTime"  # millisecond
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"


class IndicatorType(Enum):
    SMA = "sma"
    EMA = "ema"
    WMA = "wma"
    KD = "kd"
    MACD = "macd"
    MFI = "mfi"
    MTM = "mtm"
    MTM_MA = "mtm_ma"
    ROC = "roc"
    ROC_MA = "roc_ma"
    RSI = "rsi"
    WILLR = "willr"
