import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.squishy_utils import SquishyUtils

def test_random_dumpling():
    result = SquishyUtils.random_dumpling()
    assert result in SquishyUtils.DUMPLING_TYPES

def test_calculate_squish_factor():
    factor = SquishyUtils.calculate_squish_factor("spicy", 2.0)
    assert factor == 3.0  # 2.0 * 1.5

def test_generate_race_lap_time():
    time = SquishyUtils.generate_race_lap_time("classic", 1.0)
    assert 8.0 <= time <= 12.0  # base 10 +/- 2

def test_all_dumpling_types():
    for dtype in SquishyUtils.DUMPLING_TYPES:
        factor = SquishyUtils.calculate_squish_factor(dtype, 1.0)
        assert factor > 0.0