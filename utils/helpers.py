import pandas as pd
import numpy as np

def energy_clean(spath):
    df = pd.read_csv(spath,parse_dates=True,index_col='time')
    df.index = pd.to_datetime(df.index,utc=True)
    df.sort_index()
    #df.index = pd.to_datetime(df.index, utc=True)
    cols=[           'generation marine',
                 'generation geothermal',
                 'generation fossil peat',
                 'generation wind offshore',
                 'generation fossil oil shale',
                 'forecast wind offshore eday ahead',
                 'generation fossil coal-derived gas',
                 'generation hydro pumped storage aggregated']

    df.drop(columns=cols, inplace=True)
    #df = df.drop(pd.Timestamp('2014-12-31 23:00:00+00:00')) 
    #df.sort_index()
    c_January = (df.index.month==1)
    c_February = (df.index.month==2)
    c_March = (df.index.month==3)
    c_April =(df.index.month==4)
    c_May = (df.index.month==5)
    c_June = df.index.month==6
    c_July = df.index.month==7
    c_August = df.index.month==8
    c_September = df.index.month==9
    c_October= df.index.month==10
    c_November = df.index.month==11
    c_December = df.index.month==12

    df['month'] = np.where(c_January,'Jan',np.where(c_February,'Feb',np.where(c_March,'Mar',np.where(c_April,'Apr',np.where(c_May,'May',np.where(c_June,'Jun',np.where(c_July,'Jul',np.where(c_August,'Aug',np.where(c_September,'Sep',np.where(c_November,'Nov',np.where(c_December,'Dec',np.where(c_October,'Oct',np.nan))))))))))))
    return df


def weather_clean(spath):
    df = pd.read_csv(spath,parse_dates=True,index_col='time')
    #df.index = pd.to_datetime(df.index,utc=True)
    df.index = pd.DatetimeIndex(df.index,dtype='datetime64[ns]',freq='H')
    df.sort_index()
    c_January = (df.index.month==1)
    c_February = (df.index.month==2)
    c_March = (df.index.month==3)
    c_April =(df.index.month==4)
    c_May = (df.index.month==5)
    c_June = df.index.month==6
    c_July = df.index.month==7
    c_August = df.index.month==8
    c_September = df.index.month==9
    c_October= df.index.month==10
    c_November = df.index.month==11
    c_December = df.index.month==12

    df['month'] = np.where(c_January,'Jan',np.where(c_February,'Feb',np.where(c_March,'Mar',np.where(c_April,'Apr',np.where(c_May,'May',np.where(c_June,'Jun',np.where(c_July,'Jul',np.where(c_August,'Aug',np.where(c_September,'Sep',np.where(c_November,'Nov',np.where(c_December,'Dec',np.where(c_October,'Oct',np.nan))))))))))))
    return df



def add_freq(idx, freq=None):
    """Add a frequency attribute to idx, through inference or directly.

    Returns a copy.  If `freq` is None, it is inferred.

    Reference: https://stackoverflow.com/questions/46217529/pandas-datetimeindex-frequency-is-none-and-cant-be-set
    """

    idx = idx.copy()
    if freq is None:
        if idx.freq is None:
            freq = pd.infer_freq(idx)
        else:
            return idx
    idx.freq = pd.tseries.frequencies.to_offset(freq)
    if idx.freq is None:
        raise AttributeError('no discernible frequency found to `idx`.  Specify'
                             ' a frequency string with `freq`.')
    return idx

