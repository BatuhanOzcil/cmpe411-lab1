"""Starter tests for Lab 1. Add your own tests below the examples."""
import pytest

from shipping import shipping_fee


def test_light_parcel_non_member():
    assert shipping_fee(1) == 30


def test_member_gets_half_price():
    assert shipping_fee(5, is_member=True) == 25


def test_zero_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(0)


# TODO (Task 2): replace the list below with the boundary values you derived.
@pytest.mark.parametrize(
    "weight, expected",
    [
        (0.01, 30),
        (1.99, 30),
        (2, 30),
        (2.01, 50),
        (9.99, 50),
        (10, 50),
        (10.01, 90),
        (29.99, 90),
        (30, 90),    ],
)
def test_base_fee_by_weight(weight, expected):
    assert shipping_fee(weight) == expected


@pytest.mark.parametrize("weight", [-0.01, 0, 30.01, 31])
def test_invalid_weight(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)


@pytest.mark.parametrize(
    "is_member, expected",
    [(False, 50), (True, 25)]
)
def test_membership_discount(is_member, expected):
    assert shipping_fee(5, is_member=is_member) == expected
