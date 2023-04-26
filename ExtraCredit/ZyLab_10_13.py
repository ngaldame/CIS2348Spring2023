# Nathan Galdamez Gomez, 2141118
# This is ZyLab 10.13

# A class called Triangle is below
class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    # set_base method will set the triangle's base
    def set_base(self, user_base):
        self.base = user_base

    # set_height method will set the triangle's height
    def set_height(self, user_height):
        self.height = user_height

    # get_area method will calculate the triangle's area
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    # print_info method just prints the triangle's info
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')


if __name__ == '__main__':
    # Create 2 objects of the Triangle class
    triangle1 = Triangle()
    triangle2 = Triangle()

    # Read and set base and height inputs for triangle1 (use set_base() and set_height())
    triangle1.set_base(float(input()))
    triangle1.set_height(float(input()))
    # Read and set base and height inputs for triangle2 (use set_base() and set_height())
    triangle2.set_base(float(input()))
    triangle2.set_height(float(input()))

    # Determine smaller triangle (use get_area()) and output smaller triangle's info (use print_info())
    print('Triangle with smaller area:')