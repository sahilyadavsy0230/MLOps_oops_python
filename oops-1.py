#initiallize the class

class employee:
    def __init__(self):
        
        self.id=123
        self.salary=50000
        self.role="SDE"
        print("declare the attributes")
    
    def travel(self,destination):
        print(f"I am travelling from {destination}")

#initiallize object
sam=employee()
print(sam.id)
sam.travel("kerala")