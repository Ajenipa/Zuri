class geek:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def change_num1(self,new_num):
        self.num1 = new_num
    def change_num2(self,new_num2):
        self.num2 = new_num2
    def sum(self):
       return self.num1 + self.num2
number1 = geek(2,5)
number1.change_num1(99)
number1.change_num2(88)
print(number1.num1)
print(number1.num2)
sum()


class Student:
    # [assignment] Skeleton class. Add your code here  
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name (self, new_name):
        self.new_name = new_name
    def change_age (self, new_age):
        self.new_age = new_age
    def add_track (self,new_track):
        self.new_track = new_track
        print(new_track)
    def get_score (self):
        return self.score

Jamiu = Student(name="Jamiu", age=26, tracks=["FT","NT","PT"],score=55.90) 
# Expected methods
Jamiu.change_name("Peter")
Jamiu.change_age(34)
Jamiu.add_track(["FoT","NppT","PkkkT"])
print(Jamiu.get_score())

