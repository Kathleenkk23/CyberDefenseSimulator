class CyberDefenseSimulator:
    class OperatingSystem:
        def init(self, id, type, verson, vulnerability):
            self.id = id
            self.type = type
            self.verson = verson
            self.vulnerability = vulnerability
        
        def getId(self):
            return self.id
        
        def getType(self):
            return self.type
        
    
    class App:
        def init(self, id, type, verson, vulnerability):
            self.id = id
            self.type = type
            self.verson = verson
            self.vulnerability = vulnerability
            
        def getId(self):
            return self.id
        
        def getType(self):
            return self.type
        
            
    class Device:
        def init(self, OS, apps, address):
            self.OS = OS
            self.apps = apps
            self.address = address
        
        def getAddress(self)
            return self.address
            
    
    

Subnet = {}
   
            