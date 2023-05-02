__version__ = "0.0.1"

import siuba
from siuba.dply.verbs import DPLY_FUNCTIONS
from siuba.siu.dispatchers import NoArgs
from functools import wraps
import itertools

class Blank:
    def __call__(self, *args, **kwargs):
        return self.__class__()

    def __repr__(x):
        return "⚠️: <b>Don't forget to replace all the blanks!</b>"

    def _repr_html_(x):
        return "⚠️: <b>Don't forget to replace all the blanks!</b>"

    def __rshift__(self, x):
        return self.__class__()

    def __rrshift__(self, x):
        return self.__class__()


def blanks_wrapper(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        all_vals = itertools.chain(args, kwargs.values())
        if any(isinstance(x, Blank) for x in all_vals):
            return Blank()

        return f(*args, **kwargs)
    
    return wrapper

def dispatch_wrapper(f):
    @wraps(f)
    def wrapper(cls):
        impl = f(cls)
        return blanks_wrapper(impl)
    
    return wrapper

def return_blank(*args, **kwargs):
    return Blank()

def wrap_func(func_name):
    import pandas as pd
    from pandas.core.groupby import DataFrameGroupBy

    verb = getattr(siuba, func_name)
    # TODO: fix joins not have register attribute
    if hasattr(verb, 'register'):

        verb.register(Blank, return_blank)
        verb.register(NoArgs, blanks_wrapper(verb.registry.get(NoArgs)))
        verb.register(pd.DataFrame, blanks_wrapper(verb.registry.get(pd.DataFrame)))
        verb.register(DataFrameGroupBy, blanks_wrapper(verb.registry.get(DataFrameGroupBy)))

# Replaces verb dispatchers with one that always wraps the implementation
# in blanks_wrapper. This allows it to propogate maybe under a number of cases
# that would normally dispatch on regular verb, which may handle blanks in 
# surprising ways. E.g.
#    - data >> mutate(argname = ___)
#    - mutate(data, argname = ___)
#
# Note that all other cases are handled by the Blanks class itself
#    - data >> ___
#    - data >> ___ >> ___
#    - data >> ___()
#    - data >> ___(___)
for _func_name in DPLY_FUNCTIONS:
    wrap_func(_func_name)
