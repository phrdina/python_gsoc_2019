#!/usr/bin/env python3

def convert(base, currency, value, date=None):
    """
    Converts @value from @base currency to desired @currency.
    There is option @date argument where user can set specific
    date to get the exchange rates, otherwise current date is used.

    @base and @currency accepts mix of lowercase and uppercase, if
    user provides currency that doesn't exists raise RuntimeError.

    If value cannot be converted to float raise RuntimeError.

    If date is not provided in format YYYY-MM-DD raise RuntimeError.

    Returns converted value.
    """
    pass
