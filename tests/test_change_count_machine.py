import pytest
from src.change_count_machine import compute_change
from src.change_count_machine import compute_loop
from src.change_count_machine import denominations_calc

# Tests for proof of logic
class TestSimpleChange:
    def test_penny(self):
        money = 0.01
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 1 #Check for expected total items
        assert denom_counts == {0.01: 1} #Check for expected breakdown of items

    def test_2_cent(self):
        money = 0.02
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 2
        assert denom_counts == {0.01: 2}

    def test_6_cent(self):
        money = 0.06
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 2
        assert denom_counts == {0.05: 1, 0.01: 1}

    def test_10_cent(self):
        money = 0.10
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 1
        assert denom_counts == {0.1: 1}

    def test_15_cent(self):
        money = 0.15
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 2
        assert denom_counts == {0.1: 1, 0.05: 1}

    def test_20_cent(self):
        money = 0.20
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 2
        assert denom_counts == {0.1: 2}

# Tests for variety of change
class TestVarietyChange:
    def test_103_17(self):
        money = 103.17
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 8
        assert denom_counts == {100: 1, 1: 3, 0.1: 1, 0.05: 1, 0.01: 2}

    def test_99_99(self):
        money = 99.99
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 17
        assert denom_counts == {50: 1, 20: 2, 5: 1, 1: 4, 0.25: 3, 0.1: 2, 0.01: 4}

# Edge case tests
class TestEdgeCases:
    def test_0(self):
        money = 0
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 0
        assert denom_counts == {}

    def test_trailing_0(self):
        money = 5.00000000000
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 1
        assert denom_counts == {5: 1}

    def test_bad_num(self):    #This input is not allowed from the user but still testing expected output
        money = -1
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 0
        assert denom_counts == {}

    def test_rounding(self):    #Currently this input is allowed from the user but any input after the 2nd decimal place is ignored
        money = 7.005
        total_items, denom_counts = compute_change(money)
        
        assert total_items == 3
        assert denom_counts == {5: 1, 1:2}

class TestComputeLoop:
    def test_compute_loop_simple(self):
        money_left = 23.37
        denom_list = [20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
        denom_counts = {}
        total_items = 0
        total_items, denom_counts = compute_loop(money_left, denom_list, denom_counts, total_items)

        assert total_items == 8
        assert denom_counts == {20: 1, 1: 3, 0.25: 1, 0.1: 1, 0.01: 2}

class TestDenominationsCalc:
    def test_single_denomination(self):
        # Test with a single denomination
        money_left = 5.00
        denomination = 1.00
        remaining, items = denominations_calc(money_left, denomination)
        assert remaining == 0.00
        assert items == 5

    def test_partial_denomination(self):
        # Test when money_left is not an exact multiple of the denomination
        money_left = 4.30
        denomination = 1.00
        remaining, items = denominations_calc(money_left, denomination)
        assert remaining == 0.30
        assert items == 4

    def test_no_match(self):
        # Test when money_left is less than the denomination
        money_left = 0.50
        denomination = 1.00
        remaining, items = denominations_calc(money_left, denomination)
        assert remaining == 0.50
        assert items == 0




