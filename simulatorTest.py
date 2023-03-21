import unittest
from cyberDefenseSimulator import * 

class testSimulator(unittest.TestCase):
    """
    - generate exploit, pick one exploit, check the compromised device
    - typicial inputs and unnormal inputs
    - output plot of the result (time vs numebr of compromised devices)
    """
    def setUp(self):
        """
        initialize cyber security simulator
        """
        self.simulator = CyberDefenseSimulator()
        self.testCyberDefenseSimulator = CyberDefenseSimulator()

        
    def checkFunctionality(self):
        self.testCyberDefenseSimulator.generateDevices(10)
        self.testCyberDefenseSimulator.generateDevices(10)
        self.testCyberDefenseSimulator.generateVul(5)
        self.testCyberDefenseSimulator.generateVul(5)
        self.testCyberDefenseSimulator.generateExploits(3)
        self.assertEqual(self.testCyberDefenseSimulator.getSubnetSize(), 20)
        self.assertEqual(self.testCyberDefenseSimulator.getVulneralbilitiesSize(), 10)
        self.assertEqual(self.testCyberDefenseSimulator.getExploitsSize(), 4)
        self.testCyberDefenseSimulator.getinfo()

if __name__ == "__main__":
    unittest.main(verbosity=0)
