import copy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import time
import datetime
import random

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
        self.subnet = Subnet()
        # network: set of subnet
        self.network = set()
        self.vulneralbilities = set()
        self.exploits = set()
        self.defaultOS = OperatingSystem(0, "OS", 1.0)
        self.defaultApp = App(0, "game", 1.0)

    def getSubnetSize(self):
        return len(self.subnet.net)
    
    def getNetworkSize(self):
        return len(self.network)
    
    def getVulneralbilitiesSize(self):
        return len(self.vulneralbilities)
    
    def getExploitsSize(self):
        return len(self.exploits)
    
    def generateApps(self, numOfApps):
        """_summary_
        generates a list of apps with the specified number of apps to be added to the device.
        hence returns a list of apps.
        Args:
            numOfApps (int): number of apps to be generated
        """
        app_list = []
        if type(numOfApps) == int:
            for count in range(numOfApps):
                random_app = App(count, self.AppTypeGenerator(), self.randomNumberGenerator(1.0,3.0))
                app_list.append(random_app)
        return app_list
            
    def generateDevice(self, numOfApps=3):
        if type(numOfApps) == int:
            AppsList = self.generateApps(numOfApps)
            currSize = self.getSubnetSize()
            newDevice = Device(currSize, self.defaultOS, 0)
            newDevice.addApps(AppsList)
            # newDevice.getinfo()
            print(f'{len(AppsList)} of apps added to device')
            return newDevice
        else:
            print("not a valid input for generate Device")
    
    # add devices to subnet
    def generateSubnet(self, numOfDevice, numOfApps=None):
        if type(numOfDevice) == int:
            currSize = self.getSubnetSize()
            for count in range(numOfDevice):
                if numOfApps is None:
                    newDevice = self.generateDevice()
                else:
                    newDevice = self.generateDevice(numOfApps)
                self.subnet.addDevices(newDevice)
            print(f'{numOfDevice} of devices added to subnet')
        else:
            print("not a valid input for generate subnet")
            
    #  def generateNetwork

    def generateVul(self, numOfVul):
        if type(numOfVul) == int:
            currSize = self.getVulneralbilitiesSize()
            for count in range(numOfVul):
                minR, maxR = self.randomRangeGenerator(1.0, 1.3)
                vulType = self.VulTypeGenerator()
                newVul = Vulnerability(currSize+count, self.defaultOS, vulType, self.defaultApp, minR, maxR)
                self.vulneralbilities.add(newVul)
                # newVul.getInfo()
            print(f'{numOfVul} of Vulnerabilities added to vulnerabilities')
        else:
            print("not a valid input")
    
    def generateExploits(self, numOfExploits):
        if type(numOfExploits) == int:
            currSize = self.getExploitsSize()
            for count in range(numOfExploits):
                minR, maxR = self.randomRangeGenerator(1.0,1.5)
                ExpType = self.ExpTypeGenerator()
                newExploits = Exploit(int(currSize+count), ExpType, minR, maxR)
                self.exploits.add(newExploits)
                # newExploits.getInfo()
            print(f'{numOfExploits} of Exploits added to exploits')
        else:
            print("not a valid input for generate Exploits")
            
    def attackSubnet(self, exploit):
        """_summary_
            attack the subnet with a SINGLE Exploit that has valid vulnerabilities
        Args:
            Exploit (Exploit): one Exploit
        """
        print(self.subnet.net[1].getId())
        self.subnet.attack(exploit, exploit.target)

    def randomNumberGenerator(self, a, b):
        """
        generates 1 decimal point random number in range a to b
        Args:
            a (int): lower bound
            b (int): higher bound
        """
        randomNum = random.randint(a*10,b*10)/10
        return randomNum
    
    def randomRangeGenerator(self, a=1.0, b=1.0):
        num1 = self.randomNumberGenerator(a,b)
        num2 = self.randomNumberGenerator(a,b)
        maxR = max(num1, num2)
        minR = min(num1, num2)
        return minR, maxR
        
    def AppTypeGenerator(self):
        types = ["game", "lifestype", "social", "entertainment", "productivity"]
        randomNum = random.randrange(0,len(types)-1)
        return types[randomNum]
    
    def VulTypeGenerator(self):
        types = ["unknown","misconfigurations", "outdated software", "unauthorized access", "weak user credentials", "Unsecured APIs"]
        randomNum = random.randrange(0,len(types)-1)
        return types[randomNum]
    
    def ExpTypeGenerator(self):
        types = ["unknown", "known"]
        randomNum = random.randrange(0,len(types)-1)
        return types[randomNum]
    
    def randomSampleGenerator(self, sampleSet):
        """_summary_
        generates specified number of samples basd on chosen set given by the argument
        Args:
            set (set): specifies which set to chose (from the private var in constructor)
        Returns:
            type of the set: sample
        """
        listSet = list(sampleSet)
        return random.choice(listSet)
    
    def plot(self):
        """
        plot time (x-axis) vs number of compromised devices (y-axis)
        """
        plt.title("Number of Compromised Devices with respect to Time")
        dataframe = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i+1)
                                                    for i in range(7)]),
                          'classes': [5, 6, 8, 2, 3, 7, 4]})
 
        # To draw scatter time series plot of the given dataframe
        plt.plot_date(dataframe.date_of_week, dataframe.classes)
        
        plt.xticks(rotation=30, ha='right')
        plt.xlabel("time")
        plt.ylabel("number of compromised device")
        plt.show()
        
    def getinfo(self):
        print("subnet : ")
        for dev in self.subnet.net:
            print("\t device id: " + str(dev.getId()))
        print("vulnerabilities : ")
        for vul in self.vulneralbilities:
            print("\t vulnerability id: " + str(vul.getId()))
        print("exploits : ")
        for exp in self.exploits:
            print("\t exploits id: " + str(exp.getId()))



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
        print("\napp id: " + stringId)
        print("app type: " + self.getType())
        print("app version: " + str(self.getVersion()))
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
            print(f'Device {self.getId()} attacked successful')
            self.isCompromised = True
            return True

    def attackDevice(self, exploit):
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
        print("device address: " + str(self.getAddress()))
        print("device OS type: " + self.OS.type)
        print("device OS version: " + str(self.OS.version))
        print("device apps: ")
        for appID, app in self.apps.items():
            print("\t app id: " + str(app.getId()))


class Vulnerability:
    def __init__(self, id, os, vulType, target, minR=None, maxR=None):
        self.id = id
        self.OS = os
        # vul <-> one app, or one os (target 1 thing), but a seq of version
        self.Vultarget = None
        self.setTarget(target)
        self.type = vulType  # known, unknwon
        self.versionMin = 1.0
        self.versionMax = 1.0
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
        if self.Vultarget!= None:
            print("already assigned vulnerability")         
        if isinstance(target, OperatingSystem) or isinstance(target, App):
                self.Vultarget = target
        else:
            print("not a valid vul target")

    def getInfo(self):
        print(f'type is {str(self.type)}')
        print(f'range is min: {self.versionMin} and max: {self.versionMax}')


class Exploit:
    def __init__(self, id, expType, minR=None, maxR=None):
        self.id = id
        self.target = {}  # dict of target devices
        self.type = expType  # known and unknown
        self.versionMin = 1.0
        self.versionMax = 1.0
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
        if(type(targetVul)!=list):
            targetVul=list(targetVul)
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
        self.net = {}
        self.numOfCompromised = 0

    def addDevices(self, device):
        if type(device) == list:
            for dev in device:
                self.net.update({dev.getId(): dev})
                print("device "+str(dev.getId())+" added successfully")
        elif isinstance(device, Device):
            self.net.update({device.getId(): device})
            print("device "+str(device.getId())+" added successfully")
        else:
            print("not a device")

    # targetDevices is a dict
    def attack(self, exploit, targetDevices):
        if isinstance(exploit, Exploit):
            # exploit.target
            print("attacking: ")
            for devId, device in targetDevices.items():
                # exploit.target.items():
                if(devId in self.net.keys()):
                    success = self.net.get(devId).attackDevice(exploit)
                    if success:
                        self.numOfCompromised += 1

        else:
            print("not an exploit, invalid parameter")

    def getDeviceNumber(self):
        return self.len(self.net)
    
    def getCompromisedNum(self):
        return self.numOfCompromised

    def getinfo(self):
        print("num of compromised: " + str(self.getCompromisedNum()))
        print("subnet devices:")
        for deviceid, device in self.net.items():
            print("\t device id: " + str(deviceid))

