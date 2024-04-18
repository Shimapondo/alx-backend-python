#!/usr/bin/env python3
'''task 6 module
'''
from typing import List, Union


def sum_mixed_list(mxd_1st: List[Union[int, float]]) -> float:
    '''computes the sum of a list of integers and floating numbers
    '''
    return float(sum(mxd_1st))
