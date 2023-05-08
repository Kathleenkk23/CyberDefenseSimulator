# CyberDefenseSimulator

A development for a cybersecurity simulation environment that is well suited for high-resolution game-theoretic modeling and reinforcement learning approaches.


Basic Structure of the Simulator

# App: Id, type, vulneralbility, version
# OS: ID, type, version, vulnerabilities
# Device: OS, {app}, address
# Subnet: set of devices
# Network: set of subnet
# Exploit: vulnerability, OS, app
# workflow: source, test, size(# of steps)
# OS: Id, type, version, vulnerabilities
# Vulnerability

Files:

    - Simulator:
        CDSimulator.py: contains the assembled CyberSecurity Denfebse Simulator and import components from CDSimulatorComponents, including network, subnet, etc. 
        CDSimulatorComponents.py:  contains all the sub classes, including App, OS, Device, Vulnerability, Subnet, Exploit, etc.


    - Testing/Graphing:
        functionTest.py: this file is for unit testing the functionality of the Simulator Components, especially for CDSimulatorComponents.py
        simulatorTest.py: this file build upon the functionTest.py and test the functionality of the simulator, espcially for CDSimulator.py.
        simulatorGraph.py: testing output of different parameters and graph the result: 
            SetUp: 
            1) source env/bin/activate 
            2) python3 simulatorGraph.py

            - test how num of compromised change with time (main)
            - test how num of max Vul per App affect the num of compromised
            - test how num of apps per device affect the num of compromised

    - Digrams:
        Structure.pdf and IMG_6418.HEIC: outline/diagram of the CyberSecurity Denfebse Simulator. Refer to Structure.pdf for visual layout of the Simulator

    Notes reference:
        - check notes.md for all the notes and todo list.
        

next step:

ref link: 
- https://cve.mitre.org/index.html
- https://nvd.nist.gov/

- start populating input data sheet
    - gives vul, but prob not exploit(manually generate exploit with med to high severity)
    - need to pre populate the data: OS, apps, etc

