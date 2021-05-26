import unittest
import MyClass

class MyClassTest(unittest.TestCase):
    def setUp(self):
        print('In setUp()')
        self.myclass = MyClass.MyClass()
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.myclass
        del self.fixture

    def test(self):
        print('in test()')
        self.assertEqual(self.fixture, range(1, 10))

    def test_class_function(self):
        print('in test_class_function()')
        self.assertEqual(self.myclass.class_function(), True)

if __name__ == '__main__':
    unittest.main()