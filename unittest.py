import unittest
from CyberDefenseSimulator import *


class testSimulator(unittest.TestCase):


    def testOSinit(self):
        testOS = OperatingSystem(1, "known", "1.1.1")
        self.assertEqual(testOS.getId(), 1)
    
    def testAppinit(self):
        testApp1 = App(1, "email", "1.0")
        self.assertEqual(testApp1.getId(), 1)


if __name__ == '__main__':
    unittest.main()
