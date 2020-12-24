import unittest

class TestStringMethods(unittest.TestCase):

    # setup 和 tearDown 方法是在每条测试用例前后分别调用的方式
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tearDown")

    # setUpClass 和 tearDownClass 是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_abc(self):
        print("这是一个测试用例")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print("test_upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("test_isupper")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print("test_split")

if __name__ == '__main__':
    unittest.main()