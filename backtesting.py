from .strategy_runner import StrategyRunner
from typing import Union
from utils import format_time, interval_to_ms

class Backtesting(StrategyRunner):

    def __init__(self, strategy):
        super(Backtesting, self).__init__(strategy, prof_loss, data_feeder)
        self.symbol = symbol

    @property
    def strategy(self):
        return self._strategy

    @property
    def prof_loss(self):
        return self._prof_loss

    def start(self,
              startTime: Union[int, str],
              endTime: Union[int, str],
              interval: Union[int, str]):
        self.strategy_params = self.strategy.get_params()
        symbol = self.strategy_params['assest'] + self.strategy_params['base_asset']
        data_feed = getattr(self._datafeeder, 'get_' + self.strategy_params['data_feed'])
        self.data = self.data_feed(symbol = symbol, 
                                   startTime = startTime,
                                   endTime = endTime,
                                   interval = interval)

        for data in self.data:
            call = strategy.iteration_step(data)
            if call.ishold():
                continue
            if call.isbuy():
                self.handle_buy_call()
                continue
            if call.issell():
                self.handle_sell_call()
                continue

    def handle_buy_call(self, symbol: str, **kwargs):
        pass

    def handle_sell_call(self, symbol: str, **kwags):
        pass
        


    
