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
        
        self.simulator.generateDevice(3)
        self.simulator.generateSubnet(200,4)
        self.simulator.generateVul(5)
        self.targetVuls = [self.simulator.randomSampleGenerator(self.simulator.vulneralbilities)]
        
        self.targetApps = self.simulator.generateApps(30)
        self.assertEqual(len(list(self.targetApps)), 30)
        self.assertEqual(type(list(self.targetApps)[0].type), str)
        
        # generate exploit, pick one exploit, check the compromised device
        self.ranExploit = self.simulator.randomSampleGenerator(self.simulator.exploits)
        self.assertEqual(type(self.ranExploit), Exploit)
        self.ranExploit.setTargetVul(self.targetVuls)
        self.simulator.attackSubnet(self.ranExploit)
        print(f'number of compromised: {self.simulator.subnet.getCompromisedNum()}')
        
        
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
