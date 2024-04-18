#!/usr/bin/env python3
'''Task 7 module
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''converts a key to tuple to square of its value
    '''
    return (k, float(v**2))
