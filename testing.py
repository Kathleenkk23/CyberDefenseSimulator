from CyberDefenseSimulator import * 

def main():
    # testing OS
    testOS = OperatingSystem(1234, "known", "1.1.1")
    # testOS.getinfo()
    
    # testing App
    testApp1 = App(1, "email", "1.0")
    testApp2 = App(2, "email", "1.1")
    testApp3 = App(3, "email", "1.2")
    

    
    # testing vulnerability
    defaultVul = Vulnerability(1, testOS, "unknown", testApp1)
    testVul = Vulnerability(2, testOS, "unknown", testApp1)
    # defaultVul.getInfo()
    
    #testing device
    testingDevice1 = Device(1, testOS, "10.0.0")
    testingDevice2 = Device(2, testOS, "10.0.0")
    testingDevice3 = Device(3, testOS, "10.0.0")
    testingDevice4 = Device(4, testOS, "10.0.0")
    # testingDevice.getinfo()
    targets=[testingDevice1, testingDevice2, testingDevice3]
    deviceSamples=[testingDevice1, testingDevice2, testingDevice3, testingDevice4]
  
    # testing exploit
    testingExploit = Exploit("unknown")
    testingExploit.setTarget(targets)
    # testingExploit.getInfo()
    
    
    #testing subnet
    testingSubnet = Subnet()
    testingSubnet.addDevices(deviceSamples)
    testingSubnet.getinfo()
    testingSubnet.attack(testingExploit)
    
    #adding vulnerability
    # testOS.addVulnerability(defaultVul)
    # testOS.getinfo()
    # testOS.removeVulnerability(defaultVul)
    # testOS.getinfo()
    # testApp.addVulnerability(defaultVul)
    # testApp.addVulnerability(testVul)
    # testApp.removeVulnerability(defaultVul)
    # testApp.getinfo()
    
    #adding apps
    # testingDevice.addApps(testApp)
    # testingDevice.getinfo()
    
    #test cybersimulator
    testingCyberdenSimulator = CyberDefenseSimulator()
    testingCyberdenSimulator.generateDevices(10)
    testingCyberdenSimulator.generateVul(5)
    testingCyberdenSimulator.getinfo()

if __name__ == "__main__":
    main()


