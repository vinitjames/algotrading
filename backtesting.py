from .strategy_runner import StrategyRunner
from typing import Union
from utils import format_time, parse_inetrval

class Backtesting(StrategyRunner):

    def __init__(self, strategy, prof_loss, datafeeder):
        super(Backtesting, self).__init__(strategy, prof_loss, data_feeder)
        

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

        self.start_time = format_time(startTime)
        self.end_time = format_time(endTime)
        if(self.start_time >= self.end_time):
            raise ValueError("Start Time greater than end time")
        interval = parse_interval(interval)
        if(interval == None):
            raise ValueError("Could not parse interval. Unvalid interval passed")
        self.data = self.data_feeder(startTime, endTime, Interval)

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

        
            

        
        
