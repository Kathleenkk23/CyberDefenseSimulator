import unittest
from CyberDefenseSimulator import * 

class CDSFunction(unittest.TestCase):
    def setUp(self):
        # testing OS: __init__(self, id, type, version)
        self.testOS = OperatingSystem(1234, "known", "1.1.1")
        # testing App: __init__(self, id, type, version)
        self.testApp1 = App(1, "email", "1.0")
        self.testApp2 = App(2, "email", "1.1")
        self.testApp3 = App(3, "website", "1.2")
        # testing vulnerability: __init__(self, id, os, vulType, target, minR, maxR):
        self.defaultVul = Vulnerability(1, self.testOS, "unknown", self.testApp1, "1.0", "1.1")
        self.testVul = Vulnerability(2, self.testOS, "unknown", self.testApp2, "1.0", "1.3")
        #testing device: __init__(self, id, OS, address)
        self.testDevice1 = Device(1, self.testOS, "10.0.0")
        self.testDevice2 = Device(2, self.testOS, "10.0.1")
        self.testDevice3 = Device(3, self.testOS, "10.0.2")
        self.testDevice4 = Device(4, self.testOS, "10.0.3")
        self.targetApps = [self.testApp1, self.testApp2, self.testApp3]
        self.targetVul = [self.defaultVul, self.testVul]
        self.targetDevices = [self.testDevice1, self.testDevice2, self.testDevice3]
        self.deviceSamples = [self.testDevice1, self.testDevice2, self.testDevice3, self.testDevice4]
        # testing exploit: __init__(self, id, expType)
        self.testExploit = Exploit(1, "unknown", "1.0", "1.5")
        #testing subnet
        self.testingSubnet = Subnet()

        
    def testingOS(self):
        self.assertEqual(self.testOS.getId(), 1234)
        self.assertEqual(self.testOS.getType(), "known")
        self.assertEqual(self.testOS.getVersion(), "1.1.1")

    def testApp(self):
        self.assertEqual(self.testApp1.getId(), 1)
        self.assertEqual(self.testApp1.getType(), "email")
        self.assertEqual(self.testApp1.getVersion(), "1.0")
    
    def testVul(self):
        self.assertEqual(self.defaultVul.getId(), 1)
        self.assertEqual(self.defaultVul.getMin(), "1.0")
        self.assertEqual(self.defaultVul.getMax(), "1.1")
        self.defaultVul.setRange(None,"1.3")
        self.assertEqual(self.defaultVul.getMin(), "1.0")
        self.assertEqual(self.defaultVul.getMax(), "1.3")
        
    def testDevice(self):
        self.assertEqual(self.testDevice1.getId(), 1)
        self.assertEqual(self.testDevice1.getAddress(), "10.0.0")
        self.testDevice1.addApps(self.targetApps)
        self.assertEqual(self.testDevice1.getApps(), {1:self.testApp1, 2:self.testApp2, 3:self.testApp3})
        
    def testExploit(self):
        self.assertEqual(self.testExploit.getMin(), "1.0")
        self.assertEqual(self.testExploit.getMax(), "1.5")
        self.testExploit.setTargetVul(self.targetVul)

    def testSubnet(self):
        self.testingSubnet.addDevices(self.deviceSamples)
        self.testingSubnet.attack(self.testExploit, self.targetDevices)
        
#     #adding vulnerability
#     # testOS.addVulnerability(defaultVul)
#     # testOS.getinfo()
#     # testOS.removeVulnerability(defaultVul)
#     # testOS.getinfo()
#     # testApp.addVulnerability(defaultVul)
#     # testApp.addVulnerability(testVul)
#     # testApp.removeVulnerability(defaultVul)
#     # testApp.getinfo()
    
#     #adding apps
#     # testingDevice.addApps(testApp)
#     # testingDevice.getinfo()
    
#     #test cybersimulator
#     testingCyberdenSimulator = CyberDefenseSimulator()
#     testingCyberdenSimulator.generateDevices(10)
#     testingCyberdenSimulator.generateVul(5)
#     testingCyberdenSimulator.getinfo()

if __name__ == "__main__":
    unittest.main()


