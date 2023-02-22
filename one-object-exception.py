# class Innova:
#     def __init__(self, rlease_date, model):
#         self.rlease_date = rlease_date
#         self.model = model



class Employee:
    _name = None
    def __new__(self):
        if self._name is None:
            print("Creating object using new")
            self._name = super().__new__(self)
            return self._name
        else:
            raise Exception('class can have only one object')
obj=Employee()
print(obj)
