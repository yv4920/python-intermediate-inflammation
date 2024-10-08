"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import os
import pytest

@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0]),
            ([ [1,2], [3,4], [5,6] ], [3,4]),
        ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

def test_load_from_json(tmpdir):
    from inflammation.models import load_json
    example_path = os.path.join(tmpdir, 'example.json')
    with open(example_path, 'w') as temp_json_file:
        temp_json_file.write('[{"observations":[1, 2, 3]},{"observations":[4, 5, 6]}]')
    result = load_json(example_path)
    npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])


@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0] ),
            ([ [10, 21], [32, 14], [15, 62] ], [32, 62]),
            ([ [10.4, 21.112], [32.101, 114.5], [15.9, 6.082] ], [32.101, 114.5])
        ])
def test_daily_max(test, expected):
    """Test max function works for array of positive integers and floats."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0] ),
            ([ [10, 21], [32, 14], [15, 62] ], [10, 14]),
            ([ [10.4, 21.112], [32.101, 114.5], [15.9, 6.082] ], [10.4, 6.082])
        ])

def test_daily_min(test, expected):
    """Test max function works for array of positive integers and floats."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])