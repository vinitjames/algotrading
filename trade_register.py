
class Ledger(object):

    def  __init__(self, initial_assets: dict, base_asset:str = 'EUR'):
        self._init_assets = initial_assets
        self._base_asset = base_asset
        self._curr_assets = initial_assets
        self._trade_list = []

    @property
    def initial_assets(self) -> dict:
        return self._init_assets

    @property
    def base_asset(self) -> str:
        return self._base_asset

    @property
    def current_assets(self) -> dict:
        return self._curr_assets

    @property
    def trade_list(self) -> list:
        return self._trade_list

    def add_trade(self,
                  asset: str,
                  trade_type: str,
                  price: float,
                  quantity: float,
                  base_asset: str = None
                  ):
        if(currency not in self.valid_currency):
            pass
        if(trade_type.lower() not in ['buy', 'sell']):
            raise ValueError("Trade type entered not 'buy' or 'sell' ")
        if(not isinstance(price, (int,float))):
            raise ValueError("price entered should be decimal value")
        if(not isinstance(quantity, (int,float))):
            raise ValueError("Quantity entered should be decimal value")
        if base_asset is None:
            base_asset = self.base_asset
        trade  = {
            'asset': symbol,
            'type' : trade_type,
            'price' : price,
            'quantity' : quantity,
            'base_asset' : base_asset
            }
        
        self._balance_ledger(trade)
        self.trade_list.append(trade)
    
    def _balance_ledger(self, trade: dict):
        if(trade['type'] == 'buy'):
            self._add_asset(trade['asset'], trade['quantity'])
            self._remove_asset(trade['base_asset'], trade['price'])
        else:
            self._remove_asset(trade['asset'], trade['quantity'])
            self._add_asset(trade['base_asset'], trade['price'])

    def _add_asset(self, asset: str, qty: float):
        if(asset not in self.curr_assets.keys()):
            self.curr_assets[asset] = qty
        self.curr_assets[asset] += qty

    def _remove_asset(self, asset: str, qty: float):
        if(not _check_asset_availability(asset, qty)):
            raise ValueError("{} {} Asset not available".format(asset, qty)) 
        self.curr_assets[asset] -= qty
        
    def _check_asset_availability(self, asset: str, qty: float) -> bool:
        if(asset not in self.curr_assets.keys()):
            return False
        return self.curr_assets[asset] >= qty
    
     
