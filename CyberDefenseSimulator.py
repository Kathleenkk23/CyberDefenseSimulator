import copy
# class CyberDefenseSimulator:

# App: Id, type, vulneralbility, version
# OS: ID, type, version, vulnerabilities
# Device: OS, {app}, address
# Subnet: set of devices
# network: set of subnet
# explicit: vulnerability, OS, app
# workflow: source, test, size(# of steps)
# OS: Id, type, version, vulnerabilities
# Vulnerability

# class CyberDefenseSimulator


class CyberDefenseSimulator:
    def __init__(self):
        # Subnet: set of devices
        self.subnet = set()
        # network: set of subnet
        self.network = set()
        self.vulneralbilities = set()
        self.exploits = set()


    def generateDevices(self, numOfDevice):
        if type(numOfDevice) == int:
            for count in range(numOfDevice):
                newDevice = Device(
                    count, OperatingSystem(count, "unknown", 0), 0)
                self.subnet.add(newDevice)
        else:
            print("not a valid input")

    def generateVul(self, numOfVul):
        if type(numOfVul) == int:
            for count in range(numOfVul):
                newVul = Vulnerability(count, OperatingSystem(
                    count, "unknown", 0), "unknown", App(count, "email", "1.0"))
                self.vulneralbilities.add(newVul)
        else:
            print("not a valid input")
    
    def generateExploits(self, numOfExploits):
        if type(numOfExploits) == int:
            for count in range(numOfExploits):
                newExploits = Exploit("unknown");
                
                self.subnet.add(newExploits)
        else:
            print("not a valid input")

    def getinfo(self):
        print("subnet : ")
        for device in self.subnet:
            print("\t device id: " + str(device.getId()))
        print("vulnerabilities : ")
        for vul in self.vulneralbilities:
            print("\t vulnerability id: " + str(vul.getId()))

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
                self.vulnerabilities.update({vul.getId(): vul})
                print("Vulnerability "+str(vul.getId())+" added successfully")
        else:
            print("not a Vulnerability")

    def removeVulnerability(self, vul):
        if isinstance(vul, Vulnerability):
            if vul.getId() in self.vulnerabilities.keys():
                self.vulnerabilities.pop(vul.getId())
                print("Vulnerability "+str(vul.getId())+" removed successfully")
            else:
                print("doesn't contain the Vulnerability")
        else:
            print("not a Vulnerability")

    def getinfo(self):
        stringId = str(self.getId())
        print("OS id: " + stringId)
        print("OS type: " + self.getType())
        print("OS version: " + self.getVersion())
        print("OS vulneralbiblity: ")
        for vulId, vul in self.vulnerabilities.items():
            print("\tvul id: " + str(vul.getId()))


# App: Id, type, vulneralbility, version
class App:
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
                self.vulnerabilities.update({vul.getId(): vul})
                print("Vulnerability "+str(vul.getId())+" added successfully")
        else:
            print("not a Vulnerability")

    def removeVulnerability(self, vul):
        if isinstance(vul, Vulnerability):
            if vul.getId() in self.vulnerabilities.keys():
                self.vulnerabilities.pop(vul.getId())
                print("Vulnerability "+str(vul.getId())+" removed successfully")
            else:
                print("doesn't contain the Vulnerability")
        else:
            print("not a Vulnerability")

    def getVulnerabilities(self):
        print("Vulternability of app id {" + self.id + "} includes:")
        for vul in self.vulnerabilities:
            print(vul)
        return self.vulnerabilities

    def getinfo(self):
        stringId = str(self.getId())
        print("app id: " + stringId)
        print("app type: " + self.getType())
        print("app version: " + self.getVersion())
        print("app vulneralbiblity: ")
        for vulId, vul in self.vulnerabilities.items():
            print("\tvul id: " + str(vul.getId()))


# Device: OS, {app}, address
class Device:
    def __init__(self, id, OS, address):
        self.id = id
        self.OS = OS  # operatingSystem
        self.apps = {}
        self.address = address
        self.isCompromised = False

    def getId(self):
        return self.id

    def getAddress(self):
        return self.address
    
    def getApps(self):
        return self.apps

    def addSingleApp(self, appName):
        if isinstance(appName, App):
            self.apps[appName.getId()] = appName
            print("app "+str(appName.getId())+" added successfully")
        else:
            print("not an app")
    
    #Apps is a name
    def addApps(self, Apps):
        if isinstance(Apps, list):
            for app in Apps:
                self.addSingleApp(app)
        else:
            print("not a valid app list")

    def removeApp(self, appName):
        if isinstance(appName, App):
            if appName.getId() in self.apps.keys():
                self.apps.pop(appName.getId())
                print("App "+str(appName.getId())+" removed successfully")
            else:
                print("doesn't contain the App")
        else:
            print("not a App")

    def getIsCompromised(self):
        return self.isCompromised

    def attackSingleDevice(self):
        if(self.getIsCompromised() == False):
            print("attacked successful")
            self.isCompromised = True
            return True

    def attackDevices(self, exploit):
        if isinstance(exploit, Exploit)!=True:
            print("not a valid exploit")
            return False
        # check if device vulnerable to exploit
        if self.getIsCompromised():
            # if not vulnerable, return false
            return True
            # if vulnerable:
        else:
            return self.attackSingleDevice()

    def resetIsCompromise(self):
        self.isCompromised = False

    def getinfo(self):
        stringId = str(self.getId())
        print("device id: " + stringId)
        print("device address: " + self.getAddress())
        print("device OS type: " + self.OS.type)
        print("device OS version: " + self.OS.version)
        print("device apps: ")
        for appID, app in self.apps.items():
            print("\t app id: " + str(app.getId()))


class Vulnerability:
    def __init__(self, id, os, vulType, target, minR, maxR):
        self.id = id
        self.OS = os
        # vul <-> one app, or one os (target 1 thing), but a seq of version
        self.Vultarget = None
        self.setTarget(target)
        self.type = vulType  # known, unknwon
        self.versionMin = None
        self.versionMax = None
        self.setRange(minR, maxR)

    def getId(self):
        return self.id
    
    def getMax(self):
        return self.versionMax
    
    def getMin(self):
        return self.versionMin

    def setRange(self, minRange=None, maxRange=None):
        if minRange is not None:
            self.versionMin = minRange
        if maxRange is not None:
            self.versionMax = maxRange
        
    def setTarget(self, target):            
        if isinstance(target, Vulnerability) or isinstance(target, App):
            if self.Vultarget!= None:
                print("already assigned vulnerability")
            else:
                self.Vultarget = target
            
        else:
            print("not a valid vul target")

    def getInfo(self):
        print(f'type is {self.type}')
        print(f'range is min: {self.versionMin} and max: {self.versionMax}')


class Exploit:
    def __init__(self, id, expType, minR, maxR):
        self.id = id
        self.target = {}  # dict of target devices
        self.type = expType  # known and unknown
        self.versionMin = None
        self.versionMax = None
        self.setRange(minR, maxR)

    def getId(self):
        return self.id
    
    def getMax(self):
        return self.versionMax
    
    def getMin(self):
        return self.versionMin

    def setRange(self, minRange=None, maxRange=None):
        if minRange is not None:
            self.versionMin = minRange
        if maxRange is not None:
            self.versionMax = maxRange
    
    # assume targets is a list/set of vulnerabilities
    def setTargetVul(self, targetVul):
        for vul in targetVul:
            if isinstance(vul, Vulnerability):
                if vul.getId() in self.target.keys():
                    continue
                else:
                    self.target.update({vul.getId(): vul})
                    print("target vul "+str(vul.getId()) +
                          " added successfully")
            else:
                print("not a valid vul target")

    def getInfo(self):
        print(f'type is {self.type}')
        print(f'range is min: {self.versionMin} and max: {self.versionMax}')
        print("targeted apps: ")
        for targetID, targetApp in self.target.items():
            print("\t target id: " + str(targetApp.getId()))


# Subnet: set of devices
class Subnet:
    def __init__(self):
        self.subnet = {}
        self.numOfCompromised = 0

    def addDevices(self, device):
        if type(device) == list:
            for dev in device:
                self.subnet.update({dev.getId(): dev})
                print("device "+str(dev.getId())+" added successfully")
        elif isinstance(device, Device):
            self.subnet.update({device.getId(): device})
            print("device "+str(device.getId())+" added successfully")
        else:
            print("not a device")

    # targetDevices is a list
    def attack(self, exploit, targetDevices):
        if isinstance(exploit, Exploit):
            # exploit.target
            print("attacking: ")
            for target in targetDevices:
                # exploit.target.items():
                if(target.getId() in self.subnet.keys()):
                    success = self.subnet.get(target.getId()).attackSingleDevice(exploit)
                    if success:
                        self.numOfCompromised += 1

        else:
            print("not an exploit, invalid parameter")

    def getCompromisedNum(self):
        return self.numOfCompromised

    def getinfo(self):
        print("num of compromised: " + str(self.getCompromisedNum()))
        print("subnet devices:")
        for deviceid, device in self.subnet.items():
            print("\t device id: " + str(deviceid))


# network: set of subnet
network = {}
