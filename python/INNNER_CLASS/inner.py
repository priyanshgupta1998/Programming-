class Outer:
    """Outer Class"""
     #self constructer accessing the inner class in the outer class
    def __init__(self):
        ## instantiating the 'Inner' class
        self.inner = self.Inner()

    def reveal(self):
        ## calling the 'Inner' class function display
        self.inner.inner_display("Calling Inner class function from Outer class")

    class Inner:
        """Inner Class"""

        def inner_display(self, msg):
            print(msg)
            
c1 = Outer()
c1.reveal()
