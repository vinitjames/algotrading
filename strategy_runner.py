from abc import ABCMeta, abstractmethod

class StrategyRunner(ABCMeta):
    def __init__(self, strategy, prof_loss, datafeeder):
        self._strategy = strategy
        self._prof_loss = prof_loss
        self.datafeeder =  datafeeder

    @property
    @abstractmethod
    def strategy(self):
        pass

    @property
    @abstractmethod
    def prof_loss(self):
        pass
    
    @abstractmethod
    def start(self,
              startTime: int,
              endTime: int,
              interval: str):
        pass

    @abstractmethod
    def stop(self):
        pass

    
