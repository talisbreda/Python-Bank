class Client():
    def __init__(self, passcode, name, email, phone, cpf, rg) -> None:
        self.passcode = passcode
        self.name = name
        self.email = email
        self.phone = phone
        self.cpf = cpf
        self.rg = rg
    
    def getPasscode(self):
        print(self.passcode)
    def getName(self):
        print(self.name)
    def getEmail(self):
        print(self.email)
    def getPhone(self):
        print(self.phone)
    def getCPF(self):
        print(self.cpf)
    def getRG(self):
        print(self.rg)
    
    def setPasscode(self, passcode):
        self.passcode = passcode
    def setName(self, name):
        self.name = name
    def setEmail(self, email):
        self.email = email
    def setPhone(self, phone):
        self.phone = phone
    def setCPF(self, cpf):
        self.cpf = cpf
    def setRG(self, rg):
        self.rg = rg