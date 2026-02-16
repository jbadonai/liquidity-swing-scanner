# Configuration for Liquidity Swing Scanner

# Telegram Settings
TELEGRAM_BOT_TOKEN = "7022439090:AAGIJo3K-o85isgUL-1CkzNwwSzFYyjMD8U"
TELEGRAM_CHAT_ID = "5252531829"

# Trading Pairs to Monitor
# PAIRS =  ["ETHUSDT","BTCUSDT","ARUSDT","FILUSDT","NEARUSDT","ARBUSDT","OPUSDT","ATOMUSDT","DOTUSDT","AAVEUSDT","CRVUSDT","GMXUSDT","DYDXUSDT","LDOUSDT","LINKUSDT","PYTHUSDT","GRTUSDT","RENDERUSDT","INJUSDT","ONDOUSDT"]

PAIRS =  ["ENSOUSDT","C98USDT","AUCTIONUSDT","JTOUSDT","ASTRUSDT","ARKUSDT","BREVUSDT","INITUSDT","AXLUSDT","SAHARAUSDT","ROSEUSDT","DUSKUSDT","RESOLVUSDT","NKNUSDT","0GUSDT","AXSUSDT","FLOWUSDT","MANTAUSDT","GASUSDT","ERAUSDT","KERNELUSDT","DOLOUSDT","KITEUSDT","OPENUSDT","HOLOUSDT","ARKMUSDT","HEMIUSDT","ARPAUSDT","MOVEUSDT","JUPUSDT","CYBERUSDT","METISUSDT","1INCHUSDT","BERAUSDT","MIRAUSDT","NEWTUSDT","ONGUSDT","NILUSDT","PYTHUSDT","GIGGLEUSDT","AVNTUSDT","SAGAUSDT","ACTUSDT","SCRTUSDT","PROMUSDT","FIDAUSDT","BBUSDT","RENDERUSDT","CVCUSDT","IOUSDT","GUNUSDT","DASHUSDT","KAIAUSDT","AIXBTUSDT","MINAUSDT","ALLOUSDT","EDENUSDT","NTRNUSDT","MMTUSDT","PLUMEUSDT","HFTUSDT","2ZUSDT","POLYXUSDT","ALTUSDT","PENGUUSDT","PROVEUSDT","ETHFIUSDT","ONTUSDT","HEIUSDT","BIOUSDT","HAEDALUSDT","DEXEUSDT","CVXUSDT","COTIUSDT","CHZUSDT","EIGENUSDT","ONDOUSDT","REDUSDT","EULUSDT","BANANAUSDT","COWUSDT","HYPERUSDT","SHELLUSDT","MAVUSDT","MITOUSDT","SNXUSDT","PHBUSDT","SCRUSDT","AEVOUSDT","PENDLEUSDT","PHAUSDT","KAITOUSDT","PNUTUSDT","ENJUSDT","AGLDUSDT","ARUSDT","BANKUSDT","MUBARAKUSDT","LISTAUSDT","ORDIUSDT","NMRUSDT","LSKUSDT","SKLUSDT","SAPIENUSDT","IMXUSDT","BATUSDT","OGUSDT","RONINUSDT","EPICUSDT","ENAUSDT","ASTERUSDT","FORMUSDT","LAUSDT","ILVUSDT","OPUSDT","MAGICUSDT","PORTALUSDT","APEUSDT","APTUSDT","BLURUSDT","BARDUSDT","OMUSDT","POLUSDT","METUSDT","ENSUSDT","ACEUSDT","CGPTUSDT","API3USDT","CTSIUSDT","GMXUSDT","BIGTIMEUSDT","SANDUSDT","PEOPLEUSDT","CELOUSDT","KAVAUSDT","RAREUSDT","POWRUSDT","DYDXUSDT","EGLDUSDT","CRVUSDT","GRTUSDT","HOOKUSDT","INJUSDT","KMNOUSDT","COOKIEUSDT","BICOUSDT","MEUSDT","ALGOUSDT","LPTUSDT","ARBUSDT","ETHUSDT","AAVEUSDT","CHRUSDT","IOTAUSDT","DYMUSDT","MOVRUSDT","LUMIAUSDT","ALICEUSDT","ICPUSDT","LDOUSDT","MASKUSDT","NFPUSDT","BELUSDT","SOLUSDT","CUSDT","MANAUSDT","AUSDT","KSMUSDT","CFXUSDT","QTUMUSDT","FILUSDT","LINKUSDT","EDUUSDT","NEARUSDT","DOGEUSDT","MLNUSDT","ICXUSDT","FIOUSDT","LRCUSDT","CETUSUSDT","JSTUSDT","GMTUSDT","SIGNUSDT","HIVEUSDT","COMPUSDT","ORCAUSDT","BMTUSDT","MORPHOUSDT","MBOXUSDT","QNTUSDT","RDNTUSDT","ADAUSDT","HIGHUSDT","OGNUSDT","DOTUSDT","RLCUSDT","RPLUSDT","NEOUSDT","AVAXUSDT","ASRUSDT","ALPINEUSDT","FLUXUSDT","FFUSDT","BANDUSDT","HBARUSDT","OXTUSDT","CAKEUSDT","KNCUSDT","NXPCUSDT","PUNDIXUSDT","PARTIUSDT","AVAUSDT","DIAUSDT","PAXGUSDT","IDUSDT","BCHUSDT","BABYUSDT","SFPUSDT","GLMUSDT","ACXUSDT","LTCUSDT","ATOMUSDT","CTKUSDT","RUNEUSDT","SKYUSDT","CATIUSDT","HUMAUSDT","AWEUSDT","HOMEUSDT","LQTYUSDT","ATUSDT"]


# Binance API Settings
BINANCE_API_BASE = "https://api.binance.com/"
KLINES_LIMIT = 100  # Number of candles to fetch (should be > pivot_lookback * 2)

# Swing Detection Parameters
PIVOT_LOOKBACK = 14  # Pivot lookback period (same as Pine Script default)
SWING_AREA = "Wick Extremity"  # Options: "Wick Extremity" or "Full Range"

# DAILY TREND DETECTION (NEW FEATURE)
# Determines trend direction and identifies POI zones
ENABLE_DAILY_TREND = True  # Enable daily trend-based POI detection
TREND_LOOKBACK_DAYS = 2    # Number of previous days to analyze for trend (2-3 recommended)
                           # Looks at previous 2-3 completed days (excluding today)
                           # Uptrend: Previous lows not taken out (higher lows)
                           # Downtrend: Previous highs not taken out (lower highs)

# POI DETECTION MODE
# When ENABLE_DAILY_TREND = True:
#   - Only liquidity swings between daily open and protected level are tracked as POIs
#   - Protected level: Previous day's LOW (uptrend) or HIGH (downtrend)
#   - Uptrend: POIs are between prev day low and today's open (downside liquidity)
#   - Downtrend: POIs are between prev day high and today's open (upside liquidity)
#   - Only these POIs trigger alerts when mitigated
# When ENABLE_DAILY_TREND = False:
#   - All liquidity swings are monitored (original behavior)

# Behavior when trend is unclear (consolidation, mixed signals)
SKIP_PAIRS_WITHOUT_TREND = True  # True: Skip pairs with unclear trend (strict POI mode)
                                  # False: Fall back to standard mode for unclear pairs (mixed mode)

# FVG (FAIR VALUE GAP) DETECTION - ADVANCED CONFIRMATION
# After a liquidity sweep, scanner can detect FVG formation as confirmation
ENABLE_FVG_DETECTION = True  # True: Detect FVG after sweeps, False: Skip FVG detection
FVG_LOOKBACK_CANDLES = 20    # Number of candles to watch for FVG after sweep (default: 20)
                             # FVG Definition:
                             # - Gap between candle 1 high and candle 3 low (or vice versa)
                             # - Candle 2 in the middle must create the gap
                             # - Candle 3 must close within the range of candle 2
                             # - Candle 2 body must be at least 2x candle 3 body
                             # - Confirmed only when candle 3 closes (not while forming)

# LIQUIDITY FILTER - CRITICAL FOR IDENTIFYING LIQUIDITY ZONES
# Not all swing points are liquidity swings. A swing becomes a "liquidity zone" only when:
# - Price revisits the zone multiple times (Count filter), OR
# - Significant volume accumulates in the zone (Volume filter)
# This replicates how the Pine Script only displays/alerts swings that cross the filter threshold
FILTER_BY = "Count"  # Options: "Count" or "Volume"
FILTER_VALUE = 0     # Minimum threshold (uses GREATER THAN comparison):
                     # - Count: count MUST BE > FILTER_VALUE to qualify
                     # - Volume: volume MUST BE > FILTER_VALUE to qualify
                     # Set to 0 to track all swings (any count > 0 qualifies)
                     # Set to 1 to track swings with 2+ touches (count > 1)
                     # Set to 2 to track swings with 3+ touches (count > 2)
                     # Example: FILTER_VALUE = 1 means price must touch the zone at least 2 times total
                     # (initial swing formation + 1 revisit = count of 1, which is NOT > 1, so need 2 revisits)

# Timeframe Settings
TIMEFRAME = "15m"  # Timeframe for LIQUIDITY SWING/POI DETECTION
                  # This is used to detect pivot points and liquidity zones
                  # Examples: "1m", "5m", "15m", "30m", "1h", "4h"
                  # IMPORTANT: Daily ("1d") timeframe is used ONLY for trend detection,
                  # NOT for swing detection. Swings are always detected on this intraday timeframe.
SCAN_INTERVAL = 60  # Seconds between scans

# Performance Settings
MAX_WORKERS = 10  # Maximum concurrent API requests for parallel processing
REQUEST_TIMEOUT = 10  # Seconds for API request timeout
MAX_RETRIES = 3  # Maximum retry attempts for failed requests

# Display Settings
SHOW_SWING_HIGH = True
SHOW_SWING_LOW = True
LOG_LEVEL = "INFO"  # Options: "DEBUG", "INFO", "WARNING", "ERROR"
