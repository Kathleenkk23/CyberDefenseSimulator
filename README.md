# CyberDefenseSimulator

A development for a cybersecurity simulation environment that is well suited for high-resolution game-theoretic modeling and reinforcement learning approaches.


Basic Structure
# App: Id, type, vulneralbility, version
# OS: ID, type, version, vulnerabilities
# Device: OS, {app}, address
# Subnet: set of devices
# network: set of subnet
# explicit: vulnerability, OS, app
# workflow: source, test, size(# of steps)
# OS: Id, type, version, vulnerabilities
# Vulnerability

notes feb 6:
vulnerability: a set
set up a simulator
- generate set of random devices
- generate set of random vul that can target specific os, apps, etc
- make up random os, app(diff version), each with set a vulnerability 
- vul <-> one app, or one os, but a seq of version

class exploit: (implmented)
- target, data type -> vul
- function: tells which os, system
- function: a range for highest version, lowest version

class subnet:(implemented)
set of devices
attack method -> exploit as argumet, attacks all device
getCompromise num -> returns # of compromised devices

device class -> implement attack, return true or false (implemented)
internal state of the device -> underattack
another method: isCompromise -> t or f
reset: resets attack state to f (deep copy)
-  resetdefault to default application

class vulnerability:(implmented)
id, os, app, version range that it can attack,
initialized the os and device to the same default vulnerability