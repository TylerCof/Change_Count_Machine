import pytest
from change_machine import main

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

