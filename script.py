from collections import deque
import typing


def number_coma_separation(val: typing.Union[int, float, str]) -> str:
    """
    This function will convert an integer or float or string (positive or
    negative) into a Indian style coma separated number.

    Example
    =======
    123456789 will be returned as '12,34,56,789'
    12.123 will be returned as '12.123'
    '123' will be returned as '123'
    -12475 will be returned as '-12,475'
    -12345.123 will be returned as '-12,345.123'

    Parameters
    ==========
    val: an integer or float or string

    Returns
    =======
    a string

    """
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # data type checks
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    error = f'{val} is not a valid format. Acceptable formats are either int ' \
            f'or float or string'
    
    assert isinstance(val, int) | isinstance(val, float) | \
           isinstance(val, str), error
    assert not isinstance(val, bool), error
    
    try:
        float(val)
    except ValueError as _:
        print(f'ERROR: {val} is not a valid number')
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Split the value into two (before and after decimal)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    # Converting the value to string
    val = str(val)
    
    # is the number negative
    is_neg, abs_val = (True, val.replace('-', '')) if '-' in val \
        else (False, val)
    
    # splitting into two: before and after decimal portions
    bf_dec, af_dec = abs_val.split('.') if '.' in abs_val \
        else (abs_val, None)
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Append comas
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    # If the length is <=3, return as is
    # Else, first cut the last three characters
    # On the rest, run a loop to cut the last two characters at a time
    if len(bf_dec) > 3:
        csn = deque()
        csn.append(bf_dec[-3:])
        bf_dec = bf_dec[:-3]
        while True:
            if len(bf_dec) > 2:
                csn.appendleft(bf_dec[-2:])
                bf_dec = bf_dec[:-2]
            else:
                csn.appendleft(bf_dec)
                break
        
        csn = ','.join(csn)
    else:
        csn = bf_dec
    
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Append '-' (negative) and decimal parts
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    # Appending '-' if the original value was a negative number
    csn = '-' + csn if is_neg else csn
    
    # Appending the decimal part
    csn = '.'.join([csn, af_dec]) if af_dec else csn
    
    return csn
