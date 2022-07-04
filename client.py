class Client():
    def __init__(self, id, name, email, phone, cpf, rg, new) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.cpf = cpf
        self.rg = rg
        self.new = new


    def getId(self):
        return self.id
    def getNew(self):
        return self.new
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getCPF(self):
        return self.cpf
    def getRG(self):
        return self.rg
    
    def setNew(self, new):
        self.new = new
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