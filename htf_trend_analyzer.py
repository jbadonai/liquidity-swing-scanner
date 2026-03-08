"""
Higher Timeframe (HTF) Trend Analyzer
Determines market bias on higher timeframes for CRT alignment
"""
from typing import Optional, List
from models import MarketData
import config


class HTFTrendAnalyzer:
    """Analyzes higher timeframe trend for CRT alignment"""
    
    def __init__(self):
        self.htf_timeframe = config.CRT_HTF_TIMEFRAME
        self.lookback = config.CRT_HTF_LOOKBACK
    
    def get_trend_bias(self, candles: List[MarketData]) -> Optional[str]:
        """
        Determine higher timeframe trend bias
        
        Uses multiple methods to determine trend:
        1. Higher highs and higher lows (uptrend)
        2. Lower highs and lower lows (downtrend)
        3. Price position relative to moving average
        4. Recent swing structure
        
        Args:
            candles: List of HTF candles (daily or weekly)
            
        Returns:
            "bullish", "bearish", or None if neutral/unclear
        """
        if not candles or len(candles) < 10:
            return None
        
        # Use recent candles for trend analysis
        recent_candles = candles[-self.lookback:] if len(candles) >= self.lookback else candles
        
        # Method 1: Swing structure analysis
        swing_bias = self._analyze_swing_structure(recent_candles)
        
        # Method 2: Moving average trend
        ma_bias = self._analyze_moving_average(recent_candles)
        
        # Method 3: Momentum (recent candles vs older candles)
        momentum_bias = self._analyze_momentum(recent_candles)
        
        # Combine signals - need at least 2 out of 3 to confirm
        bullish_votes = sum([
            swing_bias == "bullish",
            ma_bias == "bullish",
            momentum_bias == "bullish"
        ])
        
        bearish_votes = sum([
            swing_bias == "bearish",
            ma_bias == "bearish",
            momentum_bias == "bearish"
        ])
        
        if bullish_votes >= 2:
            return "bullish"
        elif bearish_votes >= 2:
            return "bearish"
        else:
            return None  # Neutral/unclear trend
    
    def _analyze_swing_structure(self, candles: List[MarketData]) -> Optional[str]:
        """
        Analyze swing structure (higher highs/lows or lower highs/lows)
        
        Returns:
            "bullish", "bearish", or None
        """
        if len(candles) < 5:
            return None
        
        # Get recent swing points (highs and lows)
        recent_highs = [c.high for c in candles[-5:]]
        recent_lows = [c.low for c in candles[-5:]]
        
        # Check if making higher highs
        higher_highs = recent_highs[-1] > recent_highs[0]
        
        # Check if making higher lows
        higher_lows = recent_lows[-1] > recent_lows[0]
        
        # Check if making lower highs
        lower_highs = recent_highs[-1] < recent_highs[0]
        
        # Check if making lower lows
        lower_lows = recent_lows[-1] < recent_lows[0]
        
        if higher_highs and higher_lows:
            return "bullish"
        elif lower_highs and lower_lows:
            return "bearish"
        else:
            return None
    
    def _analyze_moving_average(self, candles: List[MarketData]) -> Optional[str]:
        """
        Analyze price position relative to moving average
        
        Returns:
            "bullish", "bearish", or None
        """
        if len(candles) < 20:
            return None
        
        # Calculate simple moving average (20 period)
        closes = [c.close for c in candles]
        ma_period = min(20, len(closes))
        ma = sum(closes[-ma_period:]) / ma_period
        
        current_price = closes[-1]
        
        # Check if price is above or below MA
        if current_price > ma * 1.01:  # 1% above MA
            return "bullish"
        elif current_price < ma * 0.99:  # 1% below MA
            return "bearish"
        else:
            return None
    
    def _analyze_momentum(self, candles: List[MarketData]) -> Optional[str]:
        """
        Analyze momentum (recent price vs older price)
        
        Returns:
            "bullish", "bearish", or None
        """
        if len(candles) < 10:
            return None
        
        # Compare recent average to older average
        recent_avg = sum([c.close for c in candles[-5:]]) / 5
        older_avg = sum([c.close for c in candles[-10:-5]]) / 5
        
        if recent_avg > older_avg * 1.02:  # 2% higher
            return "bullish"
        elif recent_avg < older_avg * 0.98:  # 2% lower
            return "bearish"
        else:
            return None
    
    def is_crt_aligned(self, crt_type: str, htf_bias: Optional[str]) -> bool:
        """
        Check if CRT signal is aligned with HTF bias
        
        Args:
            crt_type: "bullish" or "bearish"
            htf_bias: "bullish", "bearish", or None
            
        Returns:
            True if aligned or HTF bias is neutral, False if misaligned
        """
        # If HTF bias is neutral/unclear, allow the trade
        if htf_bias is None:
            return True
        
        # CRT must match HTF bias
        return crt_type == htf_bias
