import pytest
from change_count_machine import main

# Tests for proof of logic
class TestSimpleChange:
    def test_penny(self):
        money = 0.01
        total_items, denom_counts = main(money)
        assert total_items == 1
        assert denom_counts == {0.01: 1}

    def test_2_cent(self):
        money = 0.02
        total_items, denom_counts = main(money)
        assert total_items == 2
        assert denom_counts == {0.01: 2}

    def test_6_cent(self):
        money = 0.06
        total_items, denom_counts = main(money)
        assert total_items == 2
        assert denom_counts == {0.05: 1, 0.01: 1}

    def test_10_cent(self):
        money = 0.10
        total_items, denom_counts = main(money)
        assert total_items == 1
        assert denom_counts == {0.1: 1}

    def test_15_cent(self):
        money = 0.15
        total_items, denom_counts = main(money)
        assert total_items == 2
        assert denom_counts == {0.1: 1, 0.05: 1}

    def test_20_cent(self):
        money = 0.20
        total_items, denom_counts = main(money)
        assert total_items == 2
        assert denom_counts == {0.1: 2}

# Tests for variety of change
class TestVarietyChange:
    def test_103_17(self):
        money = 103.17
        total_items, denom_counts = main(money)
        assert total_items == 8
        assert denom_counts == {100: 1, 1: 3, 0.1: 1, 0.05: 1, 0.01: 2}

    def test_99_99(self):
        money = 99.99
        total_items, denom_counts = main(money)
        assert total_items == 17
        assert denom_counts == {50: 1, 20: 2, 5: 1, 1: 4, 0.25: 3, 0.1: 2, 0.01: 4}

# Edge case tests
class TestEdgeCases:
    def test_0(self):
        money = 0
        total_items, denom_counts = main(money)
        assert total_items == 0
        assert denom_counts == {}

