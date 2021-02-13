from .base_strategy import Strategy
from calls import Call
from collections import deque

class MACDStrategy(Strategy):
    
    def __init__(self, data_src: list,
                 fast_period: int = 12,
                 slow_period:int = 26,
                 signal_period:int = 9):
        self._data_history  = deque([], maxlen = slow_period + signal_period -1)

    @property
    def history_size(self):
        return self._data_history.max_len
    
    def get_params():
        return {
            'symbol': self.asset,
            'base_asset' : self.base_asset,
            'data_feed' : 'closing_price'  
        }
    
    def iteration_step(self, data:dict):
        if 'closing_price' not in data.key():
            raise ValueError("price not in data")

        self._data_history.append(data[price]);
        if(len(self._data_history) < self._data_history.max_len):
            return Call('hold')

        macd, macdsignal, macdhist = talib.MACD(self.data_history,
                                                slowperiod = self.slow_period,
                                                fast_period = self.fast_period,
                                                signal_period = self.signal_period)

        if(macdhist[-1] > 0):
            return Call('buy')
        if(macdhist[-1] < 0):
            return Call('sell')
        return Call('hold')

            
        
        
