
import re 

def dms2dec(coord):
    """
    Converts coordinate in DMS (degree, minutes, seconds) to decimal number
    
    Parameters:
    coord: 
        String. Format: '''51*36'9.18"N'''

    Returns:
    --------
    Coordinate as float/decimal

    """
    deg, minutes, seconds, direction =  re.split('[*\'"]', coord)
    return (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)