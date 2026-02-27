# Configuration for Liquidity Swing Scanner

# Telegram Settings
TELEGRAM_BOT_TOKEN = "7022439090:AAGIJo3K-o85isgUL-1CkzNwwSzFYyjMD8U"
TELEGRAM_CHAT_ID = "5252531829"

# Trading Pairs to Monitor
PAIRS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "BNBUSDT", "BTCUSDC", "ETHUSDC", "ADAUSDT", "LINKUSDT"]
# PAIRS = ["ENSOUSDT", "AGLDUSDT", "ALLOUSDT", "KITEUSDT", "AWEUSDT", "ORCAUSDT", "BIOUSDT", "SNXUSDT", "LAUSDT", "RPLUSDT", "DEXEUSDT", "SAPIENUSDT", "DUSKUSDT", "INJUSDT", "FIDAUSDT", "BELUSDT", "JTOUSDT", "EULUSDT", "MORPHOUSDT", "OPUSDT", "DOLOUSDT", "PROMUSDT", "KERNELUSDT", "COTIUSDT", "COWUSDT", "AXLUSDT", "PORTALUSDT", "DOTUSDT", "APTUSDT", "HOLOUSDT", "METUSDT", "0GUSDT", "IOUSDT", "BERAUSDT", "CHRUSDT", "HUMAUSDT", "CYBERUSDT", "INITUSDT", "CTKUSDT", "PUNDIXUSDT", "ETHFIUSDT", "ARUSDT", "PARTIUSDT", "BREVUSDT", "AXSUSDT", "EDENUSDT", "GIGGLEUSDT", "NILUSDT", "KMNOUSDT", "KSMUSDT", "ARPAUSDT", "MITOUSDT", "OGNUSDT", "MUBARAKUSDT", "ARBUSDT", "BBUSDT", "EIGENUSDT", "NEARUSDT", "FILUSDT", "ROSEUSDT", "CTSIUSDT", "PENGUUSDT", "ENAUSDT", "BANKUSDT", "RONINUSDT", "DYDXUSDT", "FLOWUSDT", "RENDERUSDT", "ICPUSDT", "CETUSUSDT", "SIGNUSDT", "ETCUSDT", "ORDIUSDT", "BIGTIMEUSDT", "IMXUSDT", "GUNUSDT", "C98USDT", "DASHUSDT", "ENSUSDT", "ARKMUSDT", "CVXUSDT", "AIXBTUSDT", "EDUUSDT", "2ZUSDT", "METISUSDT", "JUPUSDT", "APEUSDT", "MAVUSDT", "ADAUSDT", "LPTUSDT", "MIRAUSDT", "BICOUSDT", "GLMUSDT", "CRVUSDT", "LRCUSDT", "HFTUSDT", "ACEUSDT", "SANDUSDT", "BANDUSDT", "ONTUSDT", "SKLUSDT", "NTRNUSDT", "GMXUSDT", "MANTAUSDT", "PENDLEUSDT", "POLUSDT", "AAVEUSDT", "BCHUSDT", "CHZUSDT", "LDOUSDT", "AVNTUSDT", "ONDOUSDT", "CUSDT", "FLUXUSDT", "SAGAUSDT", "PHAUSDT", "PNUTUSDT", "HIGHUSDT", "AEVOUSDT", "KAITOUSDT", "GRTUSDT", "HAEDALUSDT", "DIAUSDT", "NXPCUSDT", "MANAUSDT", "ACXUSDT", "SHELLUSDT", "AVAUSDT", "COOKIEUSDT", "AVAXUSDT", "MMTUSDT", "KAVAUSDT", "ENJUSDT", "ALTUSDT", "PEOPLEUSDT", "DOGEUSDT", "HEMIUSDT", "CAKEUSDT", "SOLUSDT", "CFXUSDT", "BANANAUSDT", "REDUSDT", "LINKUSDT", "ILVUSDT", "EPICUSDT", "SAHARAUSDT", "PLUMEUSDT", "HEIUSDT", "ATOMUSDT", "SCRUSDT", "LUMIAUSDT", "PYTHUSDT", "AUSDT", "SFPUSDT", "MASKUSDT", "MINAUSDT", "LISTAUSDT", "GMTUSDT", "HIVEUSDT", "RAREUSDT", "LSKUSDT", "MOVRUSDT", "HOOKUSDT", "PROVEUSDT", "MOVEUSDT", "COMPUSDT", "QTUMUSDT", "MEUSDT", "DYMUSDT", "BLURUSDT", "ACTUSDT", "MAGICUSDT", "EGLDUSDT", "IDUSDT", "ASTRUSDT", "NEWTUSDT", "ICXUSDT", "CELOUSDT", "FORMUSDT", "LTCUSDT", "RDNTUSDT", "OPENUSDT", "NFPUSDT", "BABYUSDT", "CGPTUSDT", "ALICEUSDT", "HOMEUSDT", "SCRTUSDT", "BATUSDT", "1INCHUSDT", "MLNUSDT", "POLYXUSDT", "ALGOUSDT", "ETHUSDT", "FIOUSDT", "BNTUSDT", "BMTUSDT", "IOTAUSDT", "GASUSDT", "RUNEUSDT", "HBARUSDT", "MBOXUSDT", "SEIUSDT", "KAIAUSDT", "KNCUSDT", "POWRUSDT", "ASTERUSDT", "API3USDT", "ERAUSDT", "LQTYUSDT", "CATIUSDT", "NEOUSDT", "HYPERUSDT", "RLCUSDT", "QNTUSDT", "OGUSDT", "MTLUSDT", "OXTUSDT", "ALPINEUSDT", "AUCTIONUSDT", "JSTUSDT", "ONGUSDT", "FFUSDT", "ASRUSDT"]

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

# CRT (CHANGE OF RETAIL TENDENCY) DETECTION - ICT CONCEPT
# Monitors 4-hour candles for liquidity sweep and close back in range
ENABLE_CRT_DETECTION = True  # True: Monitor for CRT patterns on 4H, False: Skip CRT
CRT_TIMEFRAME = "4h"         # Timeframe for CRT detection (recommended: 4h)
                             # CRT Pattern:
                             # - Candle 1 (previous): Establishes high/low range
                             # - Candle 2 (current): Sweeps high OR low of candle 1
                             # - Candle 2 MUST close back within candle 1 range
                             # - Bullish CRT: Sweeps low, closes back in range
                             # - Bearish CRT: Sweeps high, closes back in range
                             # - Signal sent only when candle 2 closes (confirmed)

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
