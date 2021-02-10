import numpy as np

class DataLoader(object):
    
    def __init__(self, client, symbols: list= []):
        self.symbols = symbols
        self.client = client
        self.cached_data = {}
        
    def get_open_price(self,
                       symbol,
                       startTime: int = None,
                       endTime:int = None,
                       interval: int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 1]
                 
    def get_closing_price(self,
                          symbol,
                          startTime: int = None,
                          endTime:int = None,
                          interval: int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 2]

    def get_volume(self,
                   symbol,
                   startTime: int = None,
                   endTime:int = None,
                   interval: int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_lines(**kwargs)[:, 3]
    
    def get_high_price(self,
                       symbol,
                       startTime: int = None,
                       endTime:int = None,
                       interval: int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_lines(**kwargs)[:, 4]
        
    def get_low_price(self,
                      symbol,
                      startTime: int = None,
                      endTime:int = None,
                      interval: int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_lines(**kwargs)[:, 5]

    def get_aggregate_price(self):
        pass

    def get_klines(self,
                   symbol: str,
                   interval: str,
                   startTime: int = None,
                   endTime:int = None):
        
        params = locals()
        del params['self']
        data = self._get_cached_klines(**params)
        if(data is None):
            data = getattr(self.client, 'get_klines')(**params)
            #add data to cached_data
            return np.asarray(data).astype(float)
        if (startTime < data[0, 0]):
            params['endTime'] = data[0,0]
            data = np.concatenate(getattr(self.client, 'get_klines')(**params),
                                  data)     
        if (endTime > data[-1, 0]):
            params['endTime'] = endTime
            params['startTime'] = data[0,-1]
            data = np.concatenate(getattr(self.client, 'get_klines')(**params),
                                  data)
            
        return data.astype(float)
        
    def _get_cached_klines(self,
                          symbol,
                          startTime: int = None,
                          endTime:int = None,
                          interval: int = None):
        data = self._iter_cache(keys = ['klines', symbol, interval])
        if(data == None):
            return None
        if(endTime <= data[0,0])or(startTime >= data[-1,0]):
            return None
        return data[np.squeeze(np.argwhere((data[:,0]>= startTime)
                                           & (data[:,0]<= endTime))), :]
   
    def _add_klines_to_cache(self,
                             data,
                             symbol,
                             startTime: int = None,
                             endTime:int = None,
                             interval: int = None):
        data_dict  = self._iter_cache(keys = ['klines', symbol, interval])
        if(data_dict is None):
            self._create_cache_struct(keys = ['klines', symbol, interval])
            self.data_cache['klines'][symbol][interval] = data
            return 
        if(endTime < data_dict[0,0]):
            self.data_cache['klines'][symbol][interval] = np.concatenate(data, data_dict)
           
        if(startTime > data_dict[0,-1]):
           self.data_cache['klines'][symbol][interval] = np.concatenate(data_dict, data)

    def _create_cache_struct(self, keys: list):
        data = self.cached_data
        for key in keys:
            if(not isinstance(data, dict)):
               return None
            if(key not in data.keys()):
                data[key] = {}
                data = data[key]
            

    def _iter_cache(self, keys: list):
        if len(keys) == 0:
            return None
        data = self.cached_data
        for key in keys:
            if(not isinstance(data, dict)):
               return None
            if(key not in data.keys()):
                return None
            data = data[key]
        return data 

   

    
if __name__ == '__main__':
    
    from binance.public_client import PublicClient

    client  = PublicClient()
    datafeeder = DataLoader(client)
    data = datafeeder.get_klines('ETHEUR', '1h', '1/12/2020', '12/12/2020')
    print(data)
