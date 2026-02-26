"""
CRT Scanner module - monitors 4H candles for CRT patterns
Runs independently alongside the main POI/FVG scanner
"""
from typing import Dict, List, Optional
from models import CRTAlert, MarketData
from crt_detector import CRTDetector
import config


class CRTScanner:
    """Scans pairs for CRT patterns on 4H timeframe"""
    
    def __init__(self):
        self.crt_detector = CRTDetector()
        self.timeframe = config.CRT_TIMEFRAME
        # Track last seen candle to avoid duplicate alerts
        self.last_candle_time: Dict[str, int] = {}
    
    def initialize_pair(self, pair: str):
        """Initialize CRT tracking for a pair"""
        if pair not in self.last_candle_time:
            self.last_candle_time[pair] = 0
    
    def scan_pair(self, pair: str, candles: List[MarketData]) -> Optional[CRTAlert]:
        """
        Scan a pair for CRT pattern on COMPLETED candles only
        
        Args:
            pair: Trading pair
            candles: List of candles (need at least 3, most recent might be forming)
            
        Returns:
            CRTAlert if pattern detected in completed candles, None otherwise
        """
        self.initialize_pair(pair)
        
        # Need at least 3 candles (to ensure we check completed ones)
        if len(candles) < 3:
            return None
        
        # Check the candle that just closed (candles[-2], not candles[-1] which might be forming)
        # This is the candle we're analyzing for CRT pattern
        completed_candle_time = candles[-2].timestamp
        
        # Check if we already sent an alert for this completed candle
        if completed_candle_time == self.last_candle_time[pair]:
            # Already processed this candle
            return None
        
        # Update last candle time
        self.last_candle_time[pair] = completed_candle_time
        
        # Detect CRT pattern (detector now checks candles[-3] and candles[-2])
        crt = self.crt_detector.detect_crt(candles)
        
        if crt is None:
            return None
        
        # Validate entry setup
        if not self.crt_detector.is_valid_entry_zone(crt):
            return None
        
        # Create CRT alert
        sweep_price = crt.get("sweep_low") if crt["type"] == "bullish" else crt.get("sweep_high")
        
        alert = CRTAlert(
            pair=pair,
            crt_type=crt["type"],
            candle_1_high=crt["candle_1_high"],
            candle_1_low=crt["candle_1_low"],
            candle_2_high=crt["candle_2_high"],
            candle_2_low=crt["candle_2_low"],
            candle_2_close=crt["candle_2_close"],
            candle_2_open=crt["candle_2_open"],
            sweep_price=sweep_price,
            timestamp=crt["timestamp"],
            candle_1_timestamp=crt["candle_1_timestamp"],
            timeframe=self.timeframe
        )
        
        return alert
