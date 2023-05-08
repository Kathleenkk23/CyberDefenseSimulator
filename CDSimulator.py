import copy
import matplotlib.pyplot as plt
import math
import time
import datetime
import random
from CDSimulatorComponents import *
# class CyberDefenseSimulator:

# App: Id, type, vulneralbility, version
# OS: Id, type, vulnerabilities, version
# Device: Id, OS, {app}, address, isCompromised
# Subnet: set of devices
# network: set of subnet
# exploit: vulnerability, OS, app
# workflow: source, test, size(# of steps)
# Vulnerability

# class CyberDefenseSimulator


class CyberDefenseSimulator:
    """
    The simulator, including method to generate subnet, apps, network (which contains a set of subnet), vulnerabilities, exploits.
    Constructor initialize the default OS, App, and Vulnerability.
    """

    def __init__(self):
        # Subnet: set of devices
        self.subnet = Subnet()
        self.apps = set()
        # network: set of subnet
        self.network = set()
        self.vulneralbilities = set()
        self.exploits = set()
        self.defaultOS = OperatingSystem(0, "OS", 1.0)
        self.defaultApp = App(0, "game", 1.0)
        self.defaulVul = Vulnerability(0, "unknown", self.defaultApp)

    def resetAllSubnet(self):
        """
        reset everything in the subnet, meaning DELETING all
        """
        self.subnet.net.clear()
        self.subnet.resetAllCompromisedSubnet()
        # num = input("1 to comfirm: ")
        # if num == "1":
        #     print("here")
        #     self.subnet.net.clear()
        #     print(self.getNetworkSize())
        
    def resetByNumSubnet(self, resetNum):
        #randomDevices are a LIST of randomly selected device's ID
        randomDevices = self.randomSampleGenerator(self.subnet.net.keys(), resetNum)
        self.subnet.resetSomeCompromisedSubnet(randomDevices)

            

    def getSubnetSize(self):
        """
        Returns:
            int: returns the size of the subnet, equivalent to the number of devices
        """
        return len(self.subnet.net)

    def getNetworkSize(self):
        """
        Returns:
            int: returns the size of the network, equivalent to the number of subnet in the network
        """
        return len(self.network)

    def getVulneralbilitiesSize(self):
        """
        Returns:
            int: returns the size of the vulerability set
        """
        return len(self.vulneralbilities)

    def getExploitsSize(self):
        """
        Returns:
            int: returns the size of the Exploit set
        """
        return len(self.exploits)

    def generateApps(self, numOfApps, addVul=False, numOfVul=1):
        """_summary_
        generates a list of apps with the specified number of apps to be added to the device.
        hence returns a list of apps.
        Args:
            numOfApps (int): number of apps to be generated
        """
        app_list = []
        if type(numOfApps) == int:
            for count in range(numOfApps):
                random_app = App(count, self.AppTypeGenerator(),
                                 self.randomNumberGenerator(1.0, 3.0))
                if addVul:
                    appVul = self.generateVul(numOfVul, random_app)
                    # if(len(self.vulneralbilities)>=numOfVul):
                    #     for i in range(numOfVul):
                    #         random_app.addVulnerability(self.randomSampleGenerator(self.vulneralbilities))
                    # else:
                    #     random_app.addVulnerability(self.defaulVul)
                app_list.append(random_app)
                self.apps.add(random_app)
        return app_list

    def generateDevice(self, numOfApps=3, minVulperApp=0, maxVulperApp=0):
        """_summary_
        generates a list of Devices with the specified number of app,
        number range of vulnerabilities to be added to the device.
        hence returns a list of Devices.
        Args:
            numOfApps (int, optional): number of apps per device. Defaults to 3.
            minVulperApp (int, optional): min vulnerability per app. Defaults to 0.
            maxVulperApp (int, optional): max vulnerability per app, can be none. Defaults to 0.
        Returns:
            List: return list of devices as specified from the input
        """
        if type(numOfApps) == int:
            AppsList = []
            # self.generateApps(numOfApps, True, int(self.randomNumberGenerator(minVulperApp,maxVulperApp)))
            for i in range(minVulperApp, maxVulperApp):
                AppsList.append(self.randomSampleGenerator(self.apps))
            currSize = self.getSubnetSize()
            newDevice = Device(currSize, self.defaultOS, 0)
            newDevice.addApps(AppsList)
            return newDevice
        else:
            print("not a valid input for generate Device")

    # add devices to subnet
    def generateSubnet(self, numOfDevice, addApps=None, minVulperApp=0, maxVulperApp=0):
        """_summary_
        add device to our subnet with the specified number of app(optional),
        number range of vulnerabilities to be added to the device.
        no returns

        Args:
            numOfDevice (int): specifies number of app to be added to the subnet
            addApps (List, optional): allows specified apps to be added. Defaults to None.
            minVulperApp (int, optional): min vulnerability per app. Defaults to 0.
            maxVulperApp (int, optional): max vulnerability per app, can be none. Defaults to 0.

        """
        if type(numOfDevice) == int:
            currSize = self.getSubnetSize()
            for count in range(numOfDevice):
                if addApps is None:
                    newDevice = self.generateDevice()
                else:
                    newDevice = self.generateDevice(
                        addApps, minVulperApp, maxVulperApp)
                self.subnet.addDevices(newDevice)
            # print(f'{numOfDevice} of devices added to subnet')
        else:
            print("not a valid input for generate subnet")

    #  def generateNetwork

    def generateVul(self, numOfVul, targetApp=None, targetOS=None):
        """Generate Vulnerability, either target App is given or target OS is given, cannot be both
            numOfVul specifies the number of vul given to the target OS or App
        Args:
            numOfVul (int): specifies number of vul generated to be added to the Vulnerability set
            targetApp (App, optional): target app of the vulnerability. Defaults to None.
            targetOS (OS, optional): target OS of the vulnerability. Defaults to None.
        """
        if type(numOfVul) == int:
            currSize = self.getVulneralbilitiesSize()
            for count in range(numOfVul):
                minR, maxR = self.randomRangeGenerator(1.0, 1.3)
                vulType = self.VulTypeGenerator()
                # initially given dummy app
                target = self.defaultApp
                if targetApp != None:
                    target = targetApp
                elif targetOS != None:
                    target = targetOS
                newVul = Vulnerability(
                    currSize+count, vulType, target, minR, maxR)
                self.vulneralbilities.add(newVul)
                if targetApp != None or targetOS != None:
                    target.addVulnerability(newVul)
                    # print("Vulnerability added to target app/os")
                # newVul.getInfo()
            # print(f'{numOfVul} of Vulnerabilities added to vulnerabilities')
        else:
            print("not a valid input")

    def changeVulTarget(self):
        """
        after vul generated and app generated, this method can be used to reset the vul target from dummy target to a randomized app
        """
        if len(self.apps) == 0:
            print("not enough apps")
        if len(self.apps) < len(self.vulneralbilities):
            print("apps less than vul")
        for vul in self.vulneralbilities:
            vul.setTarget(self.randomSampleGenerator(self.appss))

    def generateExploits(self, numOfExploits, addVul=False, minVulperExp=0, maxVulperExp=0):
        """generate specified input number of exploits that is added to the simulator's exploit subnet. generated exploits can
        be given a range of vuleralbility, randomized during generation. If a specific number of Vulnerability per expliot, giv min and max the same number

        Args:
            numOfExploits (int): specified input number of exploits that is added to the simulator's exploit subnet
            addVul (bool, optional): whether to add Vul to the expoit. Defaults to False.
            minVulperApp (int, optional): lower boundary of vulernability to be added to the exploit. Defaults to 0.
            maxVulperExp (int, optional): upper boundary of vulernability to be added to the exploit. Defaults to 0.
        """
        if type(numOfExploits) == int:
            currSize = self.getExploitsSize()
            for count in range(numOfExploits):
                minR, maxR = self.randomRangeGenerator(1.0, 1.5)
                ExpType = self.ExpTypeGenerator()
                newExploits = Exploit(int(currSize+count), ExpType, minR, maxR)
                if addVul:
                    #  if(len(self.vulneralbilities)>=maxVulperExp):
                    for i in range(int(self.randomNumberGenerator(minVulperExp, maxVulperExp))):
                        newExploits.setTargetVul(
                            self.randomSampleGenerator(self.vulneralbilities))
                    # else:
                    #     newExploits.addVulnerability(self.defaulVul)
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
        print(
            f'expected target is vulneralbility with id:{exploit.target.keys()}')
        self.subnet.attack(exploit, self.subnet.net)

    def randomNumberGenerator(self, a, b):
        """
        generates and return 1 decimal point random number in range a to b
        Args:
            a (int): lower bound
            b (int): higher bound
        """
        if (a == b):
            return a
        randomNum = random.randint(a*10, b*10)/10
        return randomNum

    def randomRangeGenerator(self, a=1.0, b=1.0):
        """randomly generates a lower bound and a higher bound from the input range
        Args:
            a (float, optional): input lowest boundary. Defaults to 1.0.
            b (float, optional): input upper boundary. Defaults to 1.0.

        Returns:
            range: returns 2 parameter, first the lower boundary, then the higher boundary
        """
        num1 = self.randomNumberGenerator(a, b)
        num2 = self.randomNumberGenerator(a, b)
        maxR = max(num1, num2)
        minR = min(num1, num2)
        return minR, maxR

    def AppTypeGenerator(self):
        """generate app type from the 5 most common types shown below. SUBJECT TO CHANGE
        Returns:
            AppType: returns one of the the App type
        """
        types = ["game", "lifestype", "social",
                 "entertainment", "productivity"]
        randomNum = random.randrange(0, len(types)-1)
        return types[randomNum]

    def VulTypeGenerator(self):
        """generate vulnerability type from the common types shown below. SUBJECT TO CHANGE
        Returns:
            VulType: returns one of the the Vul type
        """
        types = ["unknown", "misconfigurations", "outdated software",
                 "unauthorized access", "weak user credentials", "Unsecured APIs"]
        randomNum = random.randrange(0, len(types)-1)
        return types[randomNum]

    def ExpTypeGenerator(self):
        """generate exploit type from the 2 types shown below. SUBJECT TO CHANGE
        Returns:
            Exploit Type: returns one of the the exploit type
        """
        types = ["unknown", "known"]
        randomNum = random.randrange(0, len(types)-1)
        return types[randomNum]

    def randomSampleGenerator(self, sampleSet, numOfSample=1):
        """_summary_
        generates 1 sample basd on chosen set given by the argument
        Args:
            sampleSet (set): specifies which set to chose (from the private var in constructor)
            numOfSample (int): specifies the number of Sample to be returned. default to 1
        Returns:
            type of the set: 1 sample or a list depending on the parameter numOfSample
        """
        
        listSet = list(sampleSet)
        if numOfSample==1 or len(sampleSet)<numOfSample:
            return random.choice(listSet)
        else:
            multiSample = set()
            i=0
            while(len(multiSample)!=numOfSample):
                app = random.choice(listSet)
                multiSample.add(app)
                i=i+1
                if i>1000:
                    break
            return list(multiSample)

   

    def getinfo(self):
        print("subnet : ")
        for devId, dev in self.subnet.net.items():
            print("\t device id: " + str(dev.getId()))
        print("vulnerabilities : ")
        for vul in self.vulneralbilities:
            print("\t vulnerability id: " + str(vul.getId()))
        print("exploits : ")
        for exp in self.exploits:
            print("\t exploits id: " + str(exp.getId()))

