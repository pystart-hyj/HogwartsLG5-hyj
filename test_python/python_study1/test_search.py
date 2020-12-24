import unittest

class Serach():

    def search_fun(self):
        print("search")
        return True

class TestSerach(unittest.TestCase):

    # def setUp(self) -> None:
    #     print("setup")
    #
    # def tearDown(self) -> None:
    #     print("tearDown")
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_serach1(self):
        print("testSerach1")
        serach = Serach()
        assert True == serach.search_fun()

    def test_serach2(self):
        print("testSerach2")
        serach = Serach()
        assert True == serach.search_fun()

    def test_euqal(self):
        print("断言相等")
        self.assertEqual(1, 1, "判断1==1")

    def test_noteuqal(self):
        print("断言不相等")
        self.assertNotEqual(1, 2, "判断1! =2")

class TestSerach2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass1")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass1")

    def test_serach1(self):
        print("testSerach1-1")
        serach = Serach()
        assert True == serach.search_fun()

    def test_serach2(self):
        print("testSerach2-1")
        serach = Serach()
        assert True == serach.search_fun()



if __name__ == '__main__':
    # 方法一 执行当前文件所有测试用例
    # unittest.main()
    # 方法二 将测试用例放到测试套件，批量执行测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(TestSerach('test_serach1'))
    # suite.addTest(TestSerach2('test_serach2'))
    # unittest.TextTestRunner().run(suite)
    # 方法三 将测试类放到测试套件，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSerach2)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)




