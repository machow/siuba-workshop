__version__ = "0.0.1"

import pandas as _pd
from pkg_resources import resource_filename as _rf


#track_features = _pd.read_csv(_rf("music_top200", "track_features.csv"))
#music_top200   = _pd.read_csv(_rf("music_top200", "music_top200.csv"))

def _load_df(name):
    # There is an artist in the data named "N/A", so tell pandas it's not an NA
    return _pd.read_csv(_rf("music_top200", name + ".csv"), na_values = [])

def __getattr__(x):
    if x in __all__:
        df = _load_df(x)
        globals()[x] = df
        return x

    raise AttributeError("Only these datasets are defined: %s" % __all__)

__all__ = ["track_features", "music_top200"]
