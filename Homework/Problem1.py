#Task1:
class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name 
        self.__budget = budget  

   
    def get_name(self):
        return self.__name

    
    def set_name(self, name):
        self.__name = name

    
    def get_budget(self):
        return self.__budget

   
    def set_budget(self, budget):
        self.__budget = budget

#Task2:

    def get_name(self):
        return self.__name


    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Name must be a string")


    def get_budget(self):
        return self.__budget


    def set_budget(self, budget):
        if isinstance(budget, (int, float)) and budget > 0:
            self.__budget = budget
        else:
            raise ValueError("Budget must be a positive number")
        
#Task3:
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__budget:
                self.__budget -= amount
            else:
                raise ValueError("Expense exceeds the allocated budget")
        else:
            raise ValueError("Expense amount must be a positive number")
        

#Task4:
    def display_category_summary(self):
        print(f"Category: {self.get_name()}")
        print(f"Allocated Budget: {self.get_budget()}")
        print(f"Remaining Budget: {self.get_budget()}")


