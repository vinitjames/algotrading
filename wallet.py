from abc import ABCMeta, abstractmethod
class WalletHandler(object):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def get_coin_list(self):
        pass
    @abstractmethod
    def get_coin_quantity(self, symbol: str):
        pass

    @abstractmethod
    def get_tradable_coin_quantity(self, symbol:str):
        pass
        


class DummyWalletHandler(WalletHandler):

    def __init__(self, coinQtyPair:dict = {}):
        self.coinQtyPair = coinQtyPair

    def get_coin_list(self) -> list:
        return [*self.coinQtyPair]

    def get_coin_quantity(self, symbol: str) -> float:
        return self.coinQtyPair[symbol] if symbol in self.coinQtyPair.keys() else None

    def get_tradable_coin_quantity(self, symbol:str) -> float:
        return get_coin_quantity

    def add_coin_qty(self, symbol: str, quantity: float):
        if symbol in self.coinQtyPair.keys():
            self.coinQtyPair[symbol]+= quantity
            return
        self.coinQtyPair[symbol] = quantity

    def reduce_coin_qty(self, symbol: str, quantity: float):
        if symbol not in self.coinQtyPair.keys():
            raise ValueError("{} is not available in wallet".format(symbol))
        if self.coinQtyPair[symbol] < quantity :
            raise ValueError("{} quantity is less than {}".format(symbol, quantity))
        self.coinQtyPair[symbol]-= quantity
        
    
        
