from unittest import TestCase

from test_python.src.chengyaojin import *
from test_python.src.libai import *

class TestHero(TestCase):
    def test_fight(self):
        chengyaojin = ChengYaoJin()
        libai = LiBai()
        assert chengyaojin.fight(libai) == True

        chengyaojin = ChengYaoJin()
        libai = LiBai()
        assert LiBai.fight(chengyaojin) == False

