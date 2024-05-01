from dataclasses import dataclass

@dataclass
class Rectangle:
    """Class for keeping tracking of an rectangle box"""
    x: float
    y: float
    w: float
    h: float
    
@dataclass
class Circle:
    """Class for keeping tracking of an circle"""
    x: float
    y: float
    r: float

