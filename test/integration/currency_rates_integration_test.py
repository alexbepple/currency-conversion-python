import pytest

from currency_rates import conversion_rate


def test_finds_rate_from_eur_to_usd():
    rate = conversion_rate('EUR', 'USD')
    assert rate > 0 and rate < 2


def test_complains_about_nonexistent_from_currency():
    with pytest.raises(ValueError):
        conversion_rate('foo', 'USD')
