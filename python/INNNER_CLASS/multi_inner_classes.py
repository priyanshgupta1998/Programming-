
#Multiple Inner Classes
class Outer:
    """Outer Class"""
    def __init__(self):
        ## Instantiating the 'Inner1' class
        self.inner1 = self.Inner1()
        ## Instantiating the 'Inner2' class
        self.inner2 = self.Inner2()

    def show_classes(self):
        print("This is Outer class's function ")
        self.inner1.inner_display("claass 1 ")
        self.inner2.inner_display("claass 2")

    class Inner1:
        """First Inner Class"""
        def inner_display(self, msg):
            print("This is Inner1 class")
            print(msg)

    class Inner2:
        """Second Inner Class"""
        def inner_display(self, msg):
            print("This is Inner2 class")
            print(msg)
            
            
c1 = Outer()
c1.show_classes()
            
