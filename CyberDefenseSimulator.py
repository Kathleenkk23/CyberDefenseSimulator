import copy
#class CyberDefenseSimulator:

# App: Id, type, vulneralbility, version
# OS: ID, type, version, vulnerabilities
# Device: OS, {app}, address
# Subnet: set of devices
# network: set of subnet
# explicit: vulnerability, OS, app
# workflow: source, test, size(# of steps)
# OS: Id, type, version, vulnerabilities
# Vulnerability

#class CyberDefenseSimulator
class CyberDefenseSimulator:
    def __init__(self):
        # Subnet: set of devices
        self.subnet = {}
        # network: set of subnet
        self.network = {}
    
    def getinfo(self):
        print("subnet : " + self.subnet)
        print("OS type: " + self.network)


# OS: ID, type, version, vulnerabilities
class OperatingSystem:
    def __init__(self, id, type, version):
        self.id = id
        self.type = type
        self.version = version
        self.vulnerabilities = {}

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getVersion(self):
        return self.version
    
    def addVulnerability(self, vul):
        if isinstance(vul, Vulnerability):
            if vul in self.vulnerabilities:
                print("already contain the Vulnerability")
            else:
                self.vulnerabilities.add(vul)
                print("Vulnerability "+str(vul.getID)+" added successfully")
        else:
            print("not a Vulnerability")
    
    def removeVulnerabilitiy(self, vul):
        if isinstance(vul, Vulnerability):
            if vul in self.vulnerabilities:
                self.vulnerabilities.remove(vul)
                print("Vulnerability "+str(vul.getID)+" removed successfully")
            else:
                print("doesn't contain the Vulnerability")
        else:
            print("not a Vulnerability")
            
    def getinfo(self):
        stringId = str(self.getId())
        print("OS id: " + stringId)
        print("OS type: " + self.getType())
        print("OS version: " + self.getVersion())
        print("OS vulneralbiblity: " + self.vulnerabilities.name)


# App: Id, type, vulneralbility, version
class App:
    def __init__(self, id, type, version):
        self.id = id
        self.type = type
        self.version = version
        self.vulnerability = {}

    def getId(self):
        return self.id

    def getType(self):
        return self.type
    
    def getVersion(self):
        return self.version
    
    def setVulnerabilities(self, Vul):
        self.vulneralbility.add(Vul)
        
    def getVulnerabilities(self):
        print("Vulternability of app id {" + self.id + "} includes:")
        for vul in self.vulnerability:
            print(vul)
        return self.vulnerability
        
    def getinfo(self):
        stringId = str(self.getId())
        print("app id: " + stringId)
        print("app type: " + self.getType())
        print("app version: " + self.getVersion())
        print(self.getVulnerabilities)

        

# Device: OS, {app}, address
class Device:
    def __init__(self, OS, address):
        self.OS = OS #operatingSystem
        self.apps = {}
        self.address = address
        self.isCompromised = False

    def getAddress(self):
        return self.address
    
    def addApps(self, appName):
        if isinstance(appName, App):
            self.apps[appName.getId()] = App
            print("app "+str(appName.getId())+" added successfully")
        else:
            print("not an app")
            
    def getIsCompromised(self):
        return self.isCompromised
    
    def attackDevice(self):
        if(self.getIsCompromised == False):
            self.isCompromised = True
            print("attacked successful")
            return True
        else:
            print("already compromised")
            return False
    
    def resetIsCompromise(self):
        self.isCompromised = False
    
            
    def getinfo(self):
        print("device address: " + self.address)
        print("OS type: " + self.OS.type)
        print("OS version: " + self.OS.version)
    
class Vulnerability:
    def __init__(self, id, os, vulType, targetApp):
        self.id = id
        self.OS = os
        self.targetApp = targetApp
        self.type = vulType #known, unknwon
        self.versionMin = float('inf')
        self.versionMax = float('-inf')
    
    def getID(self):
        return self.id
    
    def setRange(self, minRange, maxRange):
        self.versionMin = minRange
        self.versionMax = maxRange
        
    def getInfo(self):
        print(f'type is {self.type}')
        print(f'range is min: {self.versionMin} and max: {self.versionMax}')
        
class Exploit:
    def __init__(self, target, expType):
        self.target = target #set of targets
        self.type = expType
        self.versionMin = float('inf')
        self.versionMax = float('-inf')
    
    def setRange(self, minRange, maxRange):
        self.versionMin = minRange
        self.versionMax = maxRange
        
    def getInfo(self):
        print(f'type is {self.type}')
        print(f'range is min: {self.versionMin} and max: {self.versionMax}')


# Subnet: set of devices
class Subnet:
    def __init__(self):
        self.subnet = {}
        self.numOfCompromised = 0

    def addDevices(self, device):
        if isinstance(device, Device):
            self.subnet.add(device)
            print("device "+str(device.getID)+" added successfully")
        else:
            print("not a device")
    
    def attack(self, exploit):
        if isinstance(exploit, Exploit):  
            # exploit.target   
            print("attacking" + exploit.target)
            self.numOfCompromised += len(exploit.target)
        else:
            print("not an exploit, invalid parameter") 
    
    def getCompromisedNum(self):
        return self.getCompromisedNum
            
# network: set of subnet
network = {}

def main():
    testOS = OperatingSystem(1234, "someOS", "1.1.1")
    testOS.setVulnerabilities(3)
    testOS.getinfo()
    print('\n')
    testApp = App(1, "email", "1.0")
    testApp.getinfo()
    print('\n')
    testDevice = Device(testOS, "10.0.0")
    testDevice.getinfo()
    testDevice.addApps(testApp)
    


if __name__ == "__main__":
    main()