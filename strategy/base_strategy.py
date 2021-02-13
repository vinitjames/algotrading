from abc import ABCMeta, abstractmethod
from collections import deque 
import talib

class Strategy(metaclass = ABCMeta):

        @property
        @abstractmethod
        def history_size(self):
                pass
        @abstractmethod
        def get_params(self):
                pass
        
        @abstractmethod
        def iteration_step(self, data:dict):
                pass
                
                
            

