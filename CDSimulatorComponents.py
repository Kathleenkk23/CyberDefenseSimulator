import copy
import matplotlib.pyplot as plt
import math



class OperatingSystem:
    """Opoerating System (OS) contains ID, type, version, vulnerabilities
    """
    def __init__(self, id, type, version):
        self.id = id
        self.type = type  # "known", "unknown"
        self.version = version
        self.vulnerabilities = {}

    def getId(self):
        """return OS ID
        Returns:
            int: id of the OS
        """
        return self.id

    def getType(self):
        """return OS type
        Returns:
            str: type of the OS
        """
        return self.type

    def getVersion(self):
        """return version of the OS

        Returns:
            str: version of the OS
        """
        return self.version

    def addVulnerability(self, vul):
        """add vulnerability to the OS, if OS already contains the vulnerbility, no vul will be added
        else, the vulnerability will be added to the OS

        Args:
            vul (Vulnerability): specifies vulnerabiltiy to be added
        """
        if isinstance(vul, Vulnerability):
            if vul in self.vulnerabilities:
                print("already contain the Vulnerability")
            else:
                self.vulnerabilities.update({vul.getId(): vul})
                # print("Vulnerability "+str(vul.getId())+" added successfully")
        else:
            print("not a Vulnerability")

    def removeVulnerability(self, vul):
        """remove vulnerability from the OS, if OS doesn't contains the vulnerbility, no vul will be remove
        else, the vulnerability will be removed from the OS

        Args:
            vul (Vulnerability): specifies vulnerabiltiy to be removed
        """
        if isinstance(vul, Vulnerability):
            if vul.getId() in self.vulnerabilities.keys():
                self.vulnerabilities.pop(vul.getId())
                print("Vulnerability "+str(vul.getId())+" removed successfully")
            else:
                print("doesn't contain the Vulnerability")
        else:
            print("not a Vulnerability")

    def getinfo(self):
        """print info about the OS object, mainly for DEBUGGING
        """
        stringId = str(self.getId())
        print("OS id: " + stringId)
        print("OS type: " + self.getType())
        print("OS version: " + self.getVersion())
        print("OS vulneralbiblity: ")
        for vulId, vul in self.vulnerabilities.items():
            print("\tvul id: " + str(vul.getId()))


class App:
    """App containing Id, type, vulneralbility, version
    """
    def __init__(self, id, type, version):
        self.id = id
        self.type = type
        self.version = version
        self.vulnerabilities = {}

    def getId(self):
        """return App's unique ID
        Returns:
            int: id of the App
        """
        return self.id

    def getType(self):
        """return App type
        Returns:
            str: type of the App
        """
        return self.type

    def getVersion(self):
        """return version of the App

        Returns:
            str: version of the App
        """
        return self.version

    def addVulnerability(self, vul):
        """add vulnerability to the App, if App already contains the vulnerbility, no vul will be added
        else, the vulnerability will be added to the App
        Args:
            vul (Vulnerability): specifies vulnerabiltiy to be added
        """
        if isinstance(vul, Vulnerability):
            if vul in self.vulnerabilities:
                print("already contain the Vulnerability")
            else:
                self.vulnerabilities.update({vul.getId(): vul})
                # print("Vulnerability "+str(vul.getId())+" added successfully")
        else:
            print("not a Vulnerability")

    def removeVulnerability(self, vul):
        """remove vulnerability from the OS, if OS doesn't contains the vulnerbility, no vul will be remove
        else, the vulnerability will be removed from the OS

        Args:
            vul (Vulnerability): specifies vulnerabiltiy to be removed
        """
        if isinstance(vul, Vulnerability):
            if vul.getId() in self.vulnerabilities.keys():
                self.vulnerabilities.pop(vul.getId())
                print("Vulnerability "+str(vul.getId())+" removed successfully")
            else:
                print("doesn't contain the Vulnerability")
        else:
            print("not a Vulnerability")

    def getVulnerabilities(self):
        """get existing vulnerbility(s) from the App
        Returns:
            List: List of vulnerabilities returned
        """
        print("Vulternability of app id {" + self.id + "} includes:")
        for vul in self.vulnerabilities:
            print(vul)
        return self.vulnerabilities

    def getinfo(self):
        """print info about the App object, mainly for DEBUGGING
        """
        stringId = str(self.getId())
        print("\napp id: " + stringId)
        print("app type: " + self.getType())
        print("app version: " + str(self.getVersion()))
        print("app vulneralbiblity: ")
        for vulId, vul in self.vulnerabilities.items():
            print("\tvul id: " + str(vul.getId()))


class Device:
    """Device class with ID, OS, {app}, address, isCompromised
    """
    def __init__(self, id, OS, address):
        self.id = id
        self.OS = OS  # operatingSystem
        self.apps = {}
        self.address = address
        self.isCompromised = False

    def getId(self):
        """return Device's unique ID
        Returns:
            int: id of the Device
        """
        return self.id

    def getAddress(self):
        """return Device's unique address
        Returns:
            int: addr of the Device
        """
        return self.address

    def getApps(self):
        """return Device's apps
        Returns:
            dict: dictionary of Apps in the Device
        """
        return self.apps

    def addSingleApp(self, appName):
        """add single App to the device

        Args:
            appName (App): App to be added
        """
        if isinstance(appName, App):
            self.apps[appName.getId()] = appName
            # print("app "+str(appName.getId())+" added successfully")
        else:
            print("not an app")

    # Apps is a name
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

    def attackSingleDevice(self, exploitTargetVul):
        """_summary_
        attack a single device, helper method for attack Device method (see below)
        Args:
            exploitTargetVul (dictionary): passes the diction of the exploit's target vulnerability

        Returns:
            boolean: true of false depends on whether if the attack was successful
        """
        for vulId, vul in exploitTargetVul.items():
            for appId, app in self.apps.items():
                if (vul in app.vulnerabilities.values()):
                    self.isCompromised = True
                    return True

                if vul in self.OS.vulnerabilities.values():
                    self.isCompromised = True
                    print("OS attacked!!!!!!!!!!!!!")
                    print(f'Device {self.getId()} attacked successful')
                    return True

        # print(f'Device {self.getId()} not attacked ')
        return False

    def attackDevice(self, exploit):
        if isinstance(exploit, Exploit) != True:
            print("not a valid exploit")
            return False
        # check if device vulnerable to exploit
        if self.getIsCompromised():
            # if not vulnerable, return false
            return False
            # if vulnerable:
        else:
            return self.attackSingleDevice(exploit.target)

    def resetIsCompromise(self):
        #return true if compromise state reseted to false, return false is ALREADY NOT COMPROMISED
        if self.getIsCompromised():
            self.isCompromised = False
            return True
        else:
            # if not compromised and not reseted, return false
            return False

    def getinfo(self):
        """print info about the Device object, mainly for DEBUGGING
        """
        stringId = str(self.getId())
        print("device id: " + stringId)
        print("device address: " + str(self.getAddress()))
        print("device OS type: " + self.OS.type)
        print("device OS version: " + str(self.OS.version))
        print("device apps: ")
        for appID, app in self.apps.items():
            print("\t app id: " + str(app.getId()))


class Vulnerability:
    def __init__(self, id, vulType, target, minR=None, maxR=None):
        self.id = id
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
        if self.Vultarget != None:
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
        self.target = {}  # dict of target vulnerability
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

    # assume targets is a single vul, list/set of vulnerabilities
    def setTargetVul(self, targetVul):
        if (type(targetVul) != list):
            if (isinstance(targetVul, Vulnerability)):
                targetVul = [targetVul]
            else:
                targetVul = list(targetVul)
        for vul in targetVul:
            if isinstance(vul, Vulnerability):
                if vul.getId() in self.target.keys():
                    continue
                else:
                    self.target.update({vul.getId(): vul})
                    # print("target vul "+str(vul.getId()) +" added successfully")
            else:
                print("not a valid vul target")

    def getInfo(self):
        print(f'type is {self.type}')
        print(f'range is min: {self.versionMin} and max: {self.versionMax}')
        print("targeted apps: ")
        for targetID, targetApp in self.target.items():
            print("\t target id: " + str(targetApp.getId())+" vul")


# Subnet: set of devices
class Subnet:
    def __init__(self):
        self.net = {}
        self.numOfCompromised = 0

    def convert(self, lst):
        res_dct = {lst[i].getId(): lst[i] for i in range(0, len(lst))}
        # print(res_dct)
        return res_dct

    def addDevices(self, device):
        if type(device) == list:
            for dev in device:
                self.net.update({dev.getId(): dev})
                # print("device "+str(dev.getId())+" added successfully")
        elif isinstance(device, Device):
            self.net.update({device.getId(): device})
            # print("device "+str(device.getId())+" added successfully")
        else:
            print("not a device")

    # targetDevices is a dict
    def attack(self, exploit, targetDevices):

        if type(targetDevices) != dict:
            print("target Device is not a dict")
        if isinstance(exploit, Exploit):
            # exploit.target
            print("attacking: ")
            for devId, device in targetDevices.items():
                # exploit.target.items():
                if (devId in self.net.keys()):
                    success = self.net.get(devId).attackDevice(exploit)
                    if success:
                        self.numOfCompromised += 1

        else:
            print("not an exploit, invalid parameter")

    def getDeviceNumber(self):
        return self.len(self.net)

    def getCompromisedNum(self):
        return self.numOfCompromised

        
    def resetAllCompromisedSubnet(self):
        for deviceId, device in self.net.items():
            device.resetIsCompromise()
        self.numOfCompromised = 0
    
    def resetSomeCompromisedSubnet(self, DevIDList):
        for devID in DevIDList:
            state = self.net.get(devID).resetIsCompromise()
            if state:
                self.numOfCompromised-=1
            

    def getinfo(self):
        print("num of compromised: " + str(self.getCompromisedNum()))
        print("subnet devices:")
        for deviceid, device in self.net.items():
            print("\t device id: " + str(deviceid))
