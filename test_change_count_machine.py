import pytest
from change_count_machine import main

#Tests for proof of logic 

class TestSimpleChange:
    def test_penny(self):
        money = .01
        assert main(money) == 1

    def test_2_cent(self):
        money = .02
        assert main(money) == 2

    def test_6_cent(self):
        money = .06
        assert main(money) == 2
    
    def test_10_cent(self):
        money = .10
        assert main(money) == 1
    
    def test_15_cent(self):
        money = .15
        assert main(money) == 2

    def test_20_cent(self):
        money = .20
        assert main(money) == 2


#Start of testing for refined calculator

class TestVarietyChange:
    def test_103_17(self):
        money = 103.17
        assert main(money) == 8
    
    def test_99_99(self):
        money = 99.99
        assert main(money) == 17


#Edge cases tests

class TestEdgeCases:
    def test_0(self):
        money = 0
        assert main(money) == 0
