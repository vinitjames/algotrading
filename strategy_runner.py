from abc import ABCMeta, abstractmethod

class StrategyRunner(ABCMeta):
    def __init__(self, strategy, ledger, datafeeder):
        self._strategy = strategy
        self._ledger = ledger
        self._datafeeder =  datafeeder

    @property
    @abstractmethod
    def strategy(self):
        pass

    @property
    @abstractmethod
    def ledger(self):
        pass
    
    @abstractmethod
    def run(self,
            startTime: int,
            endTime: int,
            interval: str):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def handle_buy_call(self, symbol: str, **kwargs):
        pass

    @abstractmethod
    def handle_sell_call(self, symbol: str, **kwargs):
        pass

    
