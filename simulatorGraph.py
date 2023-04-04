import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from cyberDefenseSimulator import * 


class CDSimulator():
    
    def __init__(self):
        """
        setUp initialize of different classes
        """
        simulator = CyberDefenseSimulator()
        
    def plot(self):
        num = input("input number: ")
        print(num)
        

if __name__ == "__main__":
    simulator = CyberDefenseSimulator()
    maxVulperExp=3
    simulator.generateVul(20)
    # generate exploit, pick one exploit, check the compromised device
    simulator.generateExploits(20, True, maxVulperExp, maxVulperExp)
    
   
    targetApps = simulator.generateApps(30, True)
    # simulator.generateDevice(3)
    maxVulperApp = 20
    addApps = 6
    numOfDevice = 1000
    

    ranExploit = simulator.randomSampleGenerator(simulator.exploits)
    numOfCompromised1 = []
    # test how num of max Vul per App affect the num of compromised
    for i in range(1, maxVulperApp+1):
        simulator.generateSubnet(numOfDevice, addApps, 0, i)
        
        simulator.attackSubnet(ranExploit)
        numOfCompromised1.append(simulator.subnet.getCompromisedNum())
        print(f'1) number of compromised: {simulator.subnet.getCompromisedNum()}')
        simulator.subnet.numOfCompromised=0
    
    fig, axs = plt.subplots(2)
    fig.suptitle('Cyber Security Simulator')
    
    axs[0].set_title("Max Vulnerabilities per App and Number of Compromised Device")
    axs[0].set(xlabel="# of Compromised Device", ylabel="# Max Vul per App")
    axs[0].plot(range(1,maxVulperApp+1), numOfCompromised1)
    axs[0].set_xticks(np.arange(min(range(maxVulperApp)), max(range(maxVulperApp))+1, 1.0))
    axs[0].set_xlim(0, maxVulperApp)
    fig.subplots_adjust(hspace=0.5)
    
    
    # test how num of apps per device affect the num of compromised
    simulator.subnet.numOfCompromised=0
    ranExploit = simulator.randomSampleGenerator(simulator.exploits)
    numOfCompromised2 = []
    for i in range(1, addApps+1):
        simulator.generateSubnet(numOfDevice, i, maxVulperApp, maxVulperApp)
        simulator.attackSubnet(ranExploit)
        numOfCompromised2.append(simulator.subnet.getCompromisedNum())
        print(f'2) number of compromised: {simulator.subnet.getCompromisedNum()}')
        simulator.subnet.numOfCompromised=0

    axs[1].set_title("Max num App per device and Number of Compromised Device")
    axs[1].set(xlabel="# Max Num App per Device", ylabel="# of Compromised Device")
    axs[1].plot(range(1,addApps+1), numOfCompromised2)
    axs[1].set_xticks(np.arange(min(range(addApps)), max(range(addApps))+1, 1.0))
    axs[1].set_xlim(0, addApps)
    
    
    
    
    
    plt.show()
    
    
    # simulator.plot()