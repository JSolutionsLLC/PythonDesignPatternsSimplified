# Composite Pattern

# Component - Interface for all employees
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        pass


# Leaf - Represents an individual employee
class IndividualEmployee(Employee):
    def display_info(self):
        return f"{self.name} - {self.position}"


# Composite - Represents a group of employees with subordinates
class GroupOfEmployees(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        self.subordinates.remove(employee)

    def display_info(self):
        info = f"{self.name} - {self.position}"
        for subordinate in self.subordinates:
            info += "\n" + "  " + subordinate.display_info()
        return info


# Client Code
if __name__ == "__main__":
    # Individual employees
    emp1 = IndividualEmployee("John Doe", "Manager")
    emp2 = IndividualEmployee("Jane Smith", "Engineer")
    emp3 = IndividualEmployee("Michael Johnson", "Technician")

    # Groups of employees
    group1 = GroupOfEmployees("Engineering Team", "Team Lead")
    group1.add_subordinate(emp2)
    group1.add_subordinate(emp3)

    group2 = GroupOfEmployees("Management Team", "Director")
    group2.add_subordinate(emp1)

    # Company's organizational structure
    company = GroupOfEmployees("ABC Corp", "CEO")
    company.add_subordinate(group2)
    company.add_subordinate(group1)

    # Display company's organizational structure
    print(company.display_info())
