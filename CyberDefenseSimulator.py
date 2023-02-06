from enum import Enum
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
        self.vulnerabilities = Vulnerability.noVulneralbility

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getVersion(self):
        return self.version
    
    def setVulnerabilities(self, num):
        self.vulnerabilities = Vulnerability(num)
        
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
        self.vulnerability = Vulnerability(0)

    def getId(self):
        return self.id

    def getType(self):
        return self.type
    
    def getVersion(self):
        return self.version
    
    def setVulnerabilities(self, num):
        self.vulneralbility = Vulnerability(num)
        
    def getinfo(self):
        stringId = str(self.getId())
        print("app id: " + stringId)
        print("app type: " + self.getType())
        print("app version: " + self.getVersion())
        print("app vulneralbiblity: " + self.vulnerability.name)

        

# Device: OS, {app}, address
class Device:
    def __init__(self, OS, address):
        self.OS = OS #operatingSystem
        self.apps = {}
        self.address = address

    def getAddress(self):
        return self.address
    
    def addApps(self, appName):
        if isinstance(appName, App):
            self.apps[appName.getId()] = App
            print("app "+str(appName.getId())+" added successfully")
        else:
            print("not an app")
            
    def getinfo(self):
        print("device address: " + self.address)
        print("OS type: " + self.OS.type)
        print("OS version: " + self.OS.version)


class Vulnerability(Enum):
    noVulneralbility = 0
    vultnerability1 = 1
    vultnerability2 = 2
    vultnerability3 = 3


# Subnet: set of devices
subnet = {}

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