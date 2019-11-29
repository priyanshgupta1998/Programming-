#Multilevel Inner Classes
#In multilevel inner classes, the inner class contains another class which inner classes to the previous one. 



class Outer:
    """Outer Class"""
    def __init__(self):
        ## instantiating the 'Inner' class
        self.inner = self.Inner()
        ## instantiating the multilevel 'InnerInner' class
        self.innerinner = self.inner.InnerInner()
        
    def show_classes(self):
        print("This is Outer class's function")
        self.inner.inner_display('message 1 ' )
        self.innerinner.inner_display('message 3' )

    ## inner class
    class Inner:
        """First Inner Class"""
        def inner_display(self, msg):
            print("This is Inner class's function")
            print(msg)  
            
        def __init__(self):
            ## instantiating the 'InnerInner' class
            self.innerinner = self.InnerInner()
            
        def show_classes(self):
            print("This is Inner class's function ")
            self.innerinner.inner_display('message 2 ' )
            
        ## multilevel inner class
        class InnerInner:
            def inner_display(self, msg):
                print("This is Inner's Inner class function")
                print(msg)
c1 = Outer()
c1.show_classes()
c1.Inner().show_classes()



#output
'''
This is Outer class's function
This is Inner class's function
message 1 
This is Inner's Inner class function
message 3
This is Inner class's function 
This is Inner's Inner class function
message 2 
'''
