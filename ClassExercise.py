class Cars(object):
    def __init__(self,model,company,color):
        self.model = model
        self.company = company
        self.color = color

    def  getModelName(self):
        print(self.model)

    def getCompanyName(self):
        print(self.company)

Honda = Cars("civic","Honda","Black")
Honda.getModelName()
Honda.getCompanyName()