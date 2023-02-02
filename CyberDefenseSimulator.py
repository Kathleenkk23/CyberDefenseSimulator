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
    def init(self):
        # Subnet: set of devices
        self.subnet = {}
        # network: set of subnet
        self.network = {}
    
    def getinfo(self):
        print("subnet : " + self.subnet)
        print("OS type: " + self.network)


# OS: ID, type, version, vulnerabilities
class OperatingSystem:
    def init(self, id, type, verson):
        self.id = id
        self.type = type
        self.verson = verson
        self.vulnerabilities = Vulnerability.noVulneralbility

    def getId(self):
        print("OS id: " + self.id)
        return self.id

    def getType(self):
        print("OS type: " + self.type)
        return self.type

    def getVersion(self):
        print("OS version: " + self.verion)
        return self.version
    
    def setVulnerabilities(self, num):
        self.vulneralbilities = Vulnerability(num)
        
    def getinfo(self):
        print("OS id: " + self.getId)
        print("OS type: " + self.getType)
        print("OS version: " + self.getVersion)
        print("OS vulneralbiblity: " + self.vulnerabilities.name)


# App: Id, type, vulneralbility, version
class App:
    def init(self, id, type, verson):
        self.id = id
        self.type = type
        self.verson = verson
        self.vulnerability = Vulnerability.noVulneralbility

    def getId(self):
        return self.id

    def getType(self):
        return self.type
    
    def getVersion(self):
        return self.version
    
    def setVulnerabilities(self, num):
        self.vulneralbilities = Vulnerability(num)
        
    def getinfo(self):
        print("app id: " + self.getId)
        print("app type: " + self.getType)
        print("app version: " + self.getVersion)
        print("app vulneralbiblity: " + self.vulnerabilities.name)

        

# Device: OS, {app}, address
class Device:
    def init(self, OS, address):
        self.OS = OS #operatingSystem
        self.apps = {}
        self.address = address

    def getAddress(self):
        return self.address
    
    def addApps(self, appName):
        if isinstance(appName, App):
            self.apps.add(appName)
            print("app added successfully")
        else:
            print("not an app")
            
    def getinfo(self):
        print("device address: " + self.address)
        print("OS type: " + self.OS.type)
        print("OS version: " + self.OS.verion)


class Vulnerability(Enum):
    noVulneralbility = 0
    vultnerability1 = 1
    vultnerability2 = 2
    vultnerability3 = 3


# Subnet: set of devices
subnet = {}

# network: set of subnet
network = {}
