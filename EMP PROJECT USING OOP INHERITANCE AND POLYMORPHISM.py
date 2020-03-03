#BLL Start
class Emp:
    listEmp=[]
    @staticmethod
    def getTypeById(id):
        for e in Emp.listEmp:
            if(e.id==id):
                return e.type

    @staticmethod
    def getEmpById(id):
        for e in Emp.listEmp:
            if (e.id == id):
                if(e.type=='Dir'):
                    return Dir()
                elif(e.type=='Mgr'):
                    return Mgr()

    def __init__(self):
        self.id=0
        self.name=None
        self.type=None
    def __str__(self):
        return "Id: "+str(self.id)+" Name: "+self.name+" Type "+self.type
    def add(self):
        Emp.listEmp.append(self)
    def getDetails(self,id):
        for e in Emp.listEmp:
            if(e.id==id):
                self.id=e.id
                self.name=e.name
                self.type=e.type
                return
        print("Id not found")

    def delete(self, id):
        for e in Emp.listEmp:
            if (e.id == id):
                Emp.listEmp.remove(e)
                return
        print("Id not found")

class Dir(Emp):
    def __init__(self):
        self.dirSpecial=None
        self.share=None
        super().__init__()
    def __str__(self):
        return super().__str__()+ "Dir Special: "+self.dirSpecial+" Share: "+self.share
    def add(self):
        super().add()
    def getDetails(self,id):
        for e in Emp.listEmp:
            if(e.id==id):
                self.dirSpecial=e.dirSpecial
                self.share=e.share
                super().getDetails(id)
                return
        print("Id not found")

    def delete(self, id):
        for e in Emp.listEmp:
            if (e.id == id):
                super().delete()
                return
        print("Id not found")
class Mgr(Emp):
    def __init__(self):
        self.mgrSpecial=None
        self.incentive=None
        super().__init__()
    def __str__(self):
        return super().__str__()+ "Mgr Special: "+self.mgrSpecial+" Incentive: "+self.incentive
    def add(self):
        super().add()
    def getDetails(self,id):
        for e in Emp.listEmp:
            if(e.id==id):
                self.mgrSpecial=e.mgrSpecial
                self.incentive=e.incentive
                super().getDetails(id)
                return
        print("Id not found")

    def delete(self, id):
        for e in Emp.listEmp:
            if (e.id == id):
                super().delete()
                return
        print("Id not found")
#BLL End

#PL Start
while(True):
    print("1.add\n2.Search\n3.Delete\n4.Modify\n0.Exit")
    ch=input("Enter ur choice")
    if(ch=='1'):
        #write code for add
        print("1.Dir\n2.Mgr\n3.TT")
        ch1=input("Enter your choice")
        if(ch1=='1'):
            #write code for add dir
            obDir=Dir()
            obDir.type="Dir"
            obDir.id=int(input("Enter Id"))
            obDir.name=input("Enter Name")
            obDir.dirSpecial=input("Enter Dir Special")
            obDir.share=input("Enter Share")
            obDir.add()
            print("Director Added Sucessfully")
            pass
        elif(ch1=='2'):
            #write code for add Mgr
            obMgr = Mgr()
            obMgr.type = "Mgr"
            obMgr.id = int(input("Enter Id"))
            obMgr.name = input("Enter Name")
            obMgr.mgrSpecial = input("Enter Mgr Special")
            obMgr.incentive = input("Enter Incentive")
            obMgr.add()
            print("Manager Added Sucessfully")
            pass
        elif (ch1 == '3'):
            # write code for add TT
            pass


    elif(ch=='2'):
        id=int(input("Enter Id"))
        obj=Emp.getEmpById(id)
        obj.getDetails(id)
        print(obj)
        #write code for getDetails
        pass
    elif (ch == '3'):
        # write code for Delete
        pass
    elif (ch == '4'):
        # write code for Modify
        pass
    elif (ch == '0'):
        # write code for Exit
        pass
    break

#PL End