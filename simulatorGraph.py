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
    targetVuls = [simulator.randomSampleGenerator(simulator.vulneralbilities)]
    # generate exploit, pick one exploit, check the compromised device
    simulator.generateExploits(20, True, maxVulperExp, maxVulperExp)
    ranExploit = simulator.randomSampleGenerator(simulator.exploits)
    ranExploit.setTargetVul(targetVuls)
    
   
    targetApps = simulator.generateApps(30, True)
    # simulator.generateDevice(3)
    maxVulperApp = 20
    addApps = 5
    numOfDevice = 1000
    

        
    numOfCompromised = []
    for i in range(1,maxVulperApp+1):
        simulator.subnet.numOfCompromised=0
        simulator.generateSubnet(numOfDevice, addApps, i, i)
        
        simulator.attackSubnet(ranExploit)
        numOfCompromised.append(simulator.subnet.getCompromisedNum())
        print(f'number of compromised: {simulator.subnet.getCompromisedNum()}')
    
    fig, axs = plt.subplots(2)
    fig.suptitle('Cyber Security Simulator')
    
    axs[0].set_title("Max Vulnerabilities per App and Number of Compromised Device")
    axs[0].set(xlabel="# of Compromised Device", ylabel="# Max Vul per App")
    axs[0].plot(range(1,maxVulperApp+1), numOfCompromised)
    axs[0].set_xticks(np.arange(min(range(maxVulperApp)), max(range(maxVulperApp))+1, 1.0))
    axs[0].set_xlim(0, maxVulperApp)
    fig.subplots_adjust(hspace=0.5)
    plt.show()
    
    
    # simulator.plot()