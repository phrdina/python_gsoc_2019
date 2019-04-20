#!/usr/bin/env python3

import pytest
import subprocess
import sys

import rates

@pytest.mark.parametrize(
    "base, currency, value, date, converted",
    [
        ("EUR", "USD", 10, "2019-04-20", 11.25),
        ("USD", "EUR", 11.25, "2019-04-20", 10),
        ("eur", "usd", 10, "2019-01-20", 11.40),
        ("usd", "eur", 11.40, "2019-01-20", 10),
    ]
)
def test_convert_valid(base, currency, value, date, converted):
    res = rates.convert(base, currency, value, date)
    assert converted == round(res, 2)

@pytest.mark.parametrize(
    "base, currency, value, date, converted",
    [
        ("FOO", "USD", 10, "2019-04-20", 11.25),
        ("EUR", "USD", 10, "2019-20-04", 11.25),
        ("EUR", "USD", "abc", "2019-04-20", 11.25),
    ]
)
def test_convert_invalid(base, currency, value, date, converted):
    with pytest.raises(RuntimeError):
        res = rates.convert(base, currency, value, date)

@pytest.mark.parametrize(
    "base, currencies, values, date, output",
    [
        ("EUR", ["USD"], ["10"], "2019-04-20", "10.00 EUR is 11.25 USD\n"),
        ("eur", ["usd"], ["10", "20", "100"], "2019-04-20", "10.00 EUR is 11.25 USD\n20.00 EUR is 22.50 USD\n100.00 EUR is 112.50 USD\n"),
        ("EUR", ["USD", "CZK", "CNY"], ["10"], "2019-04-20", "10.00 EUR is 11.25 USD\n10.00 EUR is 256.82 CZK\n10.00 EUR is 75.45 CNY\n"),
    ]
)
def test_command(base, currencies, values, date, output):
    cmd = ["./rates.py", "-b", base, "-d", date]
    for currency in currencies:
        cmd.extend(["-c", currency])
    cmd.extend(values)
    res = subprocess.run(cmd, capture_output=True)
    assert res.stdout.decode() == output
    assert res.stderr.decode() == ""

pytest.main(sys.argv)
