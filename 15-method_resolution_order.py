# Creating class A
class A:
    def show(self):
        print("Method in Class A")

# Creating class B that inherits from A and overrides show()
class B(A):
    def show(self):
        print("Method in Class B")

# Creating class C that inherits from A and overrides show()
class C(A):
    def show(self):
        print("Method in Class C")

# Creating class D that inherits from both B and C
class D(B, C):
    pass

# Creating an object of class D
d = D()

# Calling the show() method
d.show()

# Checking the MRO for class D
print("\nMRO for class D:", D.mro())
