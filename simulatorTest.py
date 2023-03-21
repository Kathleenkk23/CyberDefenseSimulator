import unittest
from cyberDefenseSimulator import * 

class testSimulator(unittest.TestCase):
    """
    test specifically the simulator
    """
    
    def setUp(self):
        """
        initialize cyber security simulator and exploits
        """
        self.simulator = CyberDefenseSimulator()
        
    def test(self):
        """
        - generate exploit, pick one exploit, check the compromised device
        - typicial inputs and unnormal inputs
        - output plot of the result (time vs numebr of compromised devices)
        """
        self.simulator.generateExploits(20)
        self.assertEqual(type(list(self.simulator.exploits)[0].getMin()), float)
        self.assertEqual(type(list(self.simulator.exploits)[0].type), str)

        Apps = self.simulator.generateApps(3)
        self.assertEqual(len(list(Apps)), 3)
        self.assertEqual(type(list(Apps)[0].type), str)
        
        self.simulator.generateDevice(3)
        self.simulator.generateSubnet(5,4)
        self.simulator.generateVul(5)
        
        
        # self.simulator.plot()
        
        
        
        
        
        
        
    def Functionality(self):
        """
        quick test of the simulator's function
        """
        self.testCDS = CyberDefenseSimulator()
        self.testCDS.generateSubnet(10)
        self.testCDS.generateSubnet(10)
        self.testCDS.generateVul(5)
        self.testCDS.generateVul(5)
        self.testCDS.generateExploits(3)
        self.assertEqual(self.testCDS.getSubnetSize(), 20)
        self.assertEqual(self.testCDS.getVulneralbilitiesSize(), 10)
        self.assertEqual(self.testCDS.getExploitsSize(), 3)
        # self.testCDS.getinfo()

if __name__ == "__main__":
    unittest.main(verbosity=2)
