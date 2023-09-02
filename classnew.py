class College(object):
    college_attribute = 'College'

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print(self.name, self.branch, self.college_attribute)

    @staticmethod
    def my_college():
        college_attribute = 'integral'
        print(college_attribute)


College2 = College('integral', 'lucknow')
College2.display()