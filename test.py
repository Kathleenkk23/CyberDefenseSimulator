import unittest
from CyberDefenseSimulator import *


class testSimulator(unittest.TestCase):
    # def setUp(self):
    #     self.widget = Widget('The widget')

    def testOSinit(self):
        testOS = OperatingSystem(1234, "testOS", "1.1.1")
        self.assertEqual(testOS.getId(), 1234)


if __name__ == '__main__':
    unittest.main()
