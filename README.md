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


notes feb 21:
- Exploit class: target should be vul instead of device (implemented)
- vul <-> one app, or one os (target one thing), but a seq of version (implemented)
    - constraint can be implmented in vulnerability; make sure vulnerability not assigned multiple times.
    - problem: multiple version having the same vulnerability, violates the constraint.

- python unit testing for simulator
    - generate exploit, pick one exploit, check the compromised device
    - typicial inputs and unnormal inputs
    - output plot of the result (time vs numebr of compromised devices)

- github repo (implemented)


notes march 21:
- attacker (new)
