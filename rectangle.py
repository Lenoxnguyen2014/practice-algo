class Rectangle: 
   def __init__(self, length, breadth, cost_per_unit =0): 
       self.length = length 
       self.breadth = breadth 
       self.cost_per_unit = cost_per_unit 
   def perimeter(self): 
       return 2 * (self.length + self.breadth) 
   def area(self): 
       return self.length * self.breadth 
   def calculate_cost(self): 
       area = self.area() 
       return area * self.cost_per_unit 
# length = 40 cm, breadth = 30 cm and 1 cm^2 = Rs 100 
r = Rectangle(40, 30, 100) 
print("Area of Rectangle:",r.area()) 
print("Cost of rectangular field is : Rs ",r.calculate_cost()) 