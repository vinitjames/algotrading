class Call(object):
    
    def __init__(self, call_type:str):
        self.call_type = self._type_from_str(call_type)
        if(self.call_type not in [1,-1,0]):
            raise ValueError("Call type not created with buy sell or hold call type")
            

    def __str__(self):
        if(self.call_type == -1):
            return 'sell'
        if(self.call_type == 1):
            return 'buy'
        if(self.call_type == 0):
            return 'hold'
        
    def is_buy(self):
        if(self.call_type == 1):
            return True
        return False

    def is_sell(self):
        if(self.call_type == -1):
            return True
        return False

    def is_hold(self):
        if(self.call_type == 0):
            return True
        return False

    @classmethod
    def _type_from_str(cls, call_type: str) -> int:
        if(call_type.lower() == 'buy'):
            return 1
        if(call_type.lower() == 'sell'):
            return -1
        if(call_type.lower() == 'hold'):
            return 0
        
        
        
