import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from CDSimulator import * 


class CDSimulator():
    
    def __init__(self):
        """
        setUp initialize of different classes
        """
        simulator = CyberDefenseSimulator()
        

if __name__ == "__main__":
    simulator = CyberDefenseSimulator()
    
    targetApps = simulator.generateApps(30, True, 2)
    print(simulator.getVulneralbilitiesSize())
    
    # simulator.generateVul(20)
    # generate exploit, pick one exploit, check the compromised device
    minVulperExp=1
    maxVulperExp=3
    simulator.generateExploits(20, True, minVulperExp, maxVulperExp)
    

    
    print(f'exploit size is {simulator.getExploitsSize()}')
    ranExploit = simulator.randomSampleGenerator(simulator.exploits)
    print (ranExploit.getInfo())
    numOfCompromised1 = []
    
   
    # test how num of compromised change with time
    numOfCompromisedDev = []
    numOfIteration = int(input("num of iterations (suggested 50): "))
    resetNum = 300
    resetStep = 5 #number of step before resetting some devices
    maxVulperApp = 4
    addApps = 6
    numOfDevice = 500
    
    
    simulator.generateSubnet(numOfDevice, addApps, 0, maxVulperApp+1)
    for timeStep in range(0, numOfIteration):
        ranExploit = simulator.randomSampleGenerator(simulator.exploits)

        simulator.attackSubnet(ranExploit)
        numOfCompromisedDev.append(simulator.subnet.getCompromisedNum())
        if(timeStep%resetStep==0):
            simulator.resetByNumSubnet(resetNum)
            print("num of compromised is now: "+str(simulator.subnet.getCompromisedNum())+
                  "\nnum of device is now: " +str(simulator.getSubnetSize()))
            
    print(numOfCompromisedDev)
    fig, axs = plt.subplots(3)
    fig.suptitle('Cyber Security Simulator')
    axs[0].set_title("test how num of compromised change with time")
    axs[0].set(ylabel="# of Compromised Device", xlabel="# of Iteration")
    axs[0].plot(range(numOfIteration), numOfCompromisedDev)
    axs[0].set_xticks(np.arange(min(range(numOfIteration)), max(range(numOfIteration))+1, 2.0))
    axs[0].set_xlim(0, numOfIteration)
    fig.subplots_adjust(hspace=2)
    
    
    
    # test how num of max Vul per App affect the num of compromised
    # simulator.generateDevice(3)
    maxVulperApp = 10
    addApps = 20
    ranExploit = simulator.randomSampleGenerator(simulator.exploits)
    simulator.subnet.resetAllCompromisedSubnet()
  
    for i in range(1, maxVulperApp+1):
        simulator.generateSubnet(numOfDevice, addApps, 0, i)
        
        simulator.attackSubnet(ranExploit)
        numOfCompromised1.append(simulator.subnet.getCompromisedNum())
        # simulator.subnet.resetAllCompromisedSubnet()
        simulator.resetAllSubnet()
    
    axs[1].set_title("Max Vulnerabilities per App and Number of Compromised Device")
    axs[1].set(ylabel="# of Compromised Device", xlabel="# Max Vul per App")
    axs[1].plot(range(maxVulperApp), numOfCompromised1)
    axs[1].set_xticks(np.arange(min(range(maxVulperApp)), max(range(maxVulperApp))+1, 1.0))
    axs[1].set_xlim(1, maxVulperApp+1)
    fig.subplots_adjust(hspace=1)
    
    
    # test how num of apps per device affect the num of compromised
    maxVulperApp = 5
    addApps = 20
    ranExploit = simulator.randomSampleGenerator(simulator.exploits)
    numOfCompromised2 = []
    for i in range(1, addApps+1):
        simulator.generateSubnet(numOfDevice, i, maxVulperApp-1, maxVulperApp)
        simulator.attackSubnet(ranExploit)
        currentCompromised = simulator.subnet.getCompromisedNum()
        numOfCompromised2.append(currentCompromised)
        simulator.resetAllSubnet()


    axs[2].set_title("Max num App per device and Number of Compromised Device")
    axs[2].set(xlabel="# Max Num App per Device", ylabel="# of Compromised Device")
    axs[2].plot(range(1,addApps+1), numOfCompromised2)
    axs[2].set_xticks(np.arange(min(range(addApps)), max(range(addApps))+1, 1.0))
    axs[2].set_xlim(0, addApps)
    fig.subplots_adjust(hspace=1)
    
    
    
    
    
    plt.show()
    
    
    # simulator.plot()