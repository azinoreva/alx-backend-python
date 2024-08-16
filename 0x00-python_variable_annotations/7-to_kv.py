#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
Function to_kv that takes str k and an int OR float v
Returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Typed-annotated function
    to_kv returns tuple
    """
    return (k, v * v)
