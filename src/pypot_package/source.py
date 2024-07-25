# Requirements for this module

# 2 inputs, float
# 1 output, float
# external library? No
# Create a function - calculate hypotenuse


def pypot(base, perpendicular):
    """This is a hypotenuse calculation function...
    Args:
        base: Projection on horizontal axis
        perpendicular: Projection on vertical axis
    
    Returns:
        float: hypotenuse 
    """
    return sqrt((base**2)+(perpendicular**2))
    
def sqrt(num):
    """_summary_

    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """
    return num**0.5
