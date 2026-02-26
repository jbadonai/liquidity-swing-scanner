"""
CRT (Change of Retail Tendency) detector module
Detects liquidity sweep followed by close back in range on 4H timeframe
"""
from typing import Optional, List
from models import MarketData
from datetime import datetime


class CRTDetector:
    """Detects CRT patterns - liquidity sweep with close back in range"""
    
    def __init__(self):
        """Initialize CRT detector"""
        pass
    
    def detect_crt(self, candles: List[MarketData]) -> Optional[dict]:
        """
        Detect CRT pattern in COMPLETED candles only
        
        CRT Pattern Requirements:
        1. Need at least 3 candles (to ensure we're looking at completed candles)
        2. Check candles[-3] and candles[-2] (both fully closed)
        3. Candle 2 must sweep either high OR low of candle 1
        4. Candle 2 must close back within the range of candle 1
        
        NOTE: We intentionally skip candles[-1] as it might still be forming
        
        Bullish CRT: Sweeps low, closes back in range (reversal up expected)
        Bearish CRT: Sweeps high, closes back in range (reversal down expected)
        
        Args:
            candles: List of market candles (need at least 3, most recent last)
            
        Returns:
            Dict with CRT info or None if no valid CRT pattern
        """
        # Need at least 3 candles (to safely check completed candles)
        if len(candles) < 3:
            return None
        
        # Get the last 2 COMPLETED candles (skip the last one as it might be forming)
        candle_1 = candles[-3]  # Previous candle (establishes range) - CLOSED
        candle_2 = candles[-2]  # Current candle (just closed) - CLOSED
        
        # Define candle 1 range
        range_high = candle_1.high
        range_low = candle_1.low
        
        # Check for Bullish CRT
        bullish_crt = self._check_bullish_crt(candle_1, candle_2, range_high, range_low)
        if bullish_crt:
            return {
                "type": "bullish",
                "candle_1_high": range_high,
                "candle_1_low": range_low,
                "candle_2_high": candle_2.high,
                "candle_2_low": candle_2.low,
                "candle_2_close": candle_2.close,
                "candle_2_open": candle_2.open,
                "sweep_low": bullish_crt["sweep_low"],
                "timestamp": datetime.fromtimestamp(candle_2.timestamp / 1000),
                "candle_1_timestamp": datetime.fromtimestamp(candle_1.timestamp / 1000)
            }
        
        # Check for Bearish CRT
        bearish_crt = self._check_bearish_crt(candle_1, candle_2, range_high, range_low)
        if bearish_crt:
            return {
                "type": "bearish",
                "candle_1_high": range_high,
                "candle_1_low": range_low,
                "candle_2_high": candle_2.high,
                "candle_2_low": candle_2.low,
                "candle_2_close": candle_2.close,
                "candle_2_open": candle_2.open,
                "sweep_high": bearish_crt["sweep_high"],
                "timestamp": datetime.fromtimestamp(candle_2.timestamp / 1000),
                "candle_1_timestamp": datetime.fromtimestamp(candle_1.timestamp / 1000)
            }
        
        return None
    
    def _check_bullish_crt(self, candle_1: MarketData, candle_2: MarketData,
                          range_high: float, range_low: float) -> Optional[dict]:
        """
        Check for Bullish CRT pattern
        
        Bullish CRT:
        - Candle 2 low MUST sweep BELOW candle 1 low (takes out sell stops)
        - Sweep means candle 2 low < candle 1 low (not equal, must be lower)
        - Candle 2 MUST close STRICTLY WITHIN candle 1 range (not at boundaries)
        - Close must be: range_low < close < range_high
        - Indicates reversal up (retail trapped short, smart money going long)

        Returns:
            Dict with sweep info or None
        """
        # Candle 2 MUST sweep BELOW candle 1 low (not equal)
        # Use a small threshold to ensure actual sweep
        sweep_threshold = range_low * 0.0001  # 0.01% minimum sweep
        if candle_2.low >= range_low - sweep_threshold:
            return None

        # Candle 2 must close STRICTLY WITHIN candle 1 range (not at boundaries)
        # Use a small threshold to ensure it's actually inside, not at the edge
        range_threshold = (range_high - range_low) * 0.01  # 1% of range as buffer
        if not (range_low + range_threshold < candle_2.close < range_high - range_threshold):
            return None

        # Valid Bullish CRT
        return {
            "sweep_low": candle_2.low
        }

    def _check_bearish_crt(self, candle_1: MarketData, candle_2: MarketData,
                          range_high: float, range_low: float) -> Optional[dict]:
        """
        Check for Bearish CRT pattern

        Bearish CRT:
        - Candle 2 high MUST sweep ABOVE candle 1 high (takes out buy stops)
        - Sweep means candle 2 high > candle 1 high (not equal, must be higher)
        - Candle 2 MUST close STRICTLY WITHIN candle 1 range (not at boundaries)
        - Close must be: range_low < close < range_high
        - Indicates reversal down (retail trapped long, smart money going short)

        Returns:
            Dict with sweep info or None
        """
        # Candle 2 MUST sweep ABOVE candle 1 high (not equal)
        # Use a small threshold to ensure actual sweep
        sweep_threshold = range_high * 0.0001  # 0.01% minimum sweep
        if candle_2.high <= range_high + sweep_threshold:
            return None

        # Candle 2 must close STRICTLY WITHIN candle 1 range (not at boundaries)
        # Use a small threshold to ensure it's actually inside, not at the edge
        range_threshold = (range_high - range_low) * 0.01  # 1% of range as buffer
        if not (range_low + range_threshold < candle_2.close < range_high - range_threshold):
            return None

        # Valid Bearish CRT
        return {
            "sweep_high": candle_2.high
        }

    def is_valid_entry_zone(self, crt: dict) -> bool:
        """
        Validate if CRT provides good entry setup

        Args:
            crt: CRT detection result

        Returns:
            True if valid for entry, False otherwise
        """
        # Additional validation can be added here
        # For now, all detected CRTs are considered valid
        return True