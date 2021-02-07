from abc import ABCMeta, abstractmethod
from collections import deque 
import talib

class Strategy(metaclass = ABCMeta):

        def __init__(self, data_srcs: list, window_size: int):
                self.data_srcs = data_srcs
                self.data_history = deque([], maxlen = window_size) 

        @abstractmethod
        def iteration_step(self, data:dict):
                pass
                
                
            

