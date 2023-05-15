class details :
    def __init__(self,id,name,gender):
        self.__id=id
        self.__name=name
        self.__gender=gender
    def showdata(self):
        print("id",self.__id)
        print("name",self.__name)
        print("gender",self.__gender)
        
class Employee(details):
    def __init__(self,id="<no detils>",name="<no details>",gender="<no details>",comp="<no details>",dept="<no details>"):
        details.__init(self,Id,name,gender)
        self.__company=comp
        self.__dept=dept
    def showEmployee(self):
       self.showdata()
       print("company",self.__company)
       print("department",self.__dept)
       
class docter(details):
    def __init__(self,Id="<no detils>",name="<no details>",gender="<no details>",hosp="<no details>",dept="<no details>"):
        details.__init(self,Id,name,gender)
        self.__hospital=hos
        self.__dept=dept
    def showemployee(self):
        self.showdata()
        print("hospital",self.hospital)
        print("department",self.dept)
def main():
    print("\t\t\t\temployee object")
    e=Employee(1,"prem")
    e.showemployee()
    print("\n \t\t\t\t docter object")
    d=Docter(1,"pankaj","male")
    d.showemployee()
if __name__=="__main__":
    main()
