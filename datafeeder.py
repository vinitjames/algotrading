import numpy as np
from utils import format_time, interval_to_ms

class DataFeeder(object):
    
    def __init__(self, client):
        self.client = client
        self.cached_data = {}
        
    def get_open_price(self,
                       symbol,
                       interval: int,
                       startTime: int = None,
                       endTime:int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 1]
                 
    def get_close_price(self,
                        symbol,
                        interval: int,
                        startTime: int = None,
                        endTime:int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 4]

    def get_volume(self,
                   symbol,
                   interval: str,
                   startTime: int = None,
                   endTime:int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 5]
    
    def get_high_price(self,
                       symbol,
                       interval: int,
                       startTime: int = None,
                       endTime:int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 2]
        
    def get_low_price(self,
                      symbol,
                      interval: int = None,
                      startTime: int = None,
                      endTime:int = None):
        kwargs = locals()
        del kwargs['self']
        return self.get_klines(**kwargs)[:, 3]

    def get_aggregate_price(self):
        pass

    def get_klines(self,
                   symbol: str,
                   interval: str,                   
                   startTime: int = None,
                   endTime:int = None):
        params= {}
        params['interval'] = interval
        params['symbol'] = symbol
        params['startTime'] = format_time(startTime)
        params['endTime'] = format_time(endTime)
        import ipdb; ipdb.set_trace()
        data = self._get_cached_klines(**params)
        if(data is None):
            data = getattr(self.client, 'get_historical_klines')(**params)
            data = np.asarray(data).astype(float)
            self._add_klines_to_cache(data, **params)
            return data
        
        
        if (params['startTime'] < data[0][0]):
            params['endTime'] = int(data[0][0]) - interval_to_ms(interval)
            data = np.concatenate((self.get_klines(**params),
                                   data))     
        if (params['endTime'] > data[-1][0]):
            params['endTime'] = endTime
            params['startTime'] = int(data[0][-1]) + interval_to_ms(interval)
            data = np.concatenate((data, self.get_klines(**params)))
            
        return data.astype(float)
        
    def _get_cached_klines(self,
                          symbol,
                          startTime: int = None,
                          endTime:int = None,
                          interval: int = None):
        data = self._iter_cache(keys = ['klines', symbol, interval])
        print('This is data' , data)

        if(data is None):
            return None
        if(endTime <= data[0][0])or(startTime >= data[-1][0]):
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
            self.cached_data['klines'][symbol][interval] = data
            return 
        if(endTime < int(data_dict[0][0])):
            self.cache_data['klines'][symbol][interval] = np.concatenate((data, data_dict))
           
        if(startTime > int(data_dict[0][-1])):
           self.cached_data['klines'][symbol][interval] = np.concatenate((data_dict, data))

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
    datafeeder = DataFeeder(client)
    data = datafeeder.get_klines('ETHEUR', '1h', '1/12/2020', '12/12/2020')
    data = datafeeder.get_closing_price('ETHEUR', '1h', '1/12/2020', '12/12/2020')
    print(data)
    data = datafeeder.get_open_price('ETHEUR', '1h', '1/12/2020', '12/12/2020')
    print(data)
    data = datafeeder.get_high_price('ETHEUR', '1h', '1/12/2020', '12/12/2020')
    print(data)
    data = datafeeder.get_low_price('ETHEUR', '1h', '1/12/2020', '12/12/2020')
    print(data)
    data = datafeeder.get_klines('ETHEUR', '1h', '1/11/2020', '11/12/2020')
    
