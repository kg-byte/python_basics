class Vehicle:
    '''
    Vehicle is a type that describes a machine for traveling.
    '''
    class_variable = 'accessible for all methods'
    def __init__(self, distance_traveled=0, unit='miles', **kwargs):
        '''
        Customizes the initialization of the object
        '''
        self.distance_traveled = distance_traveled
        self.unit = unit

    # multiple constructor workaround
    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)

    # doesn't need access to class var.. basically a method that
    # is attached to a class... can takes in a input/output...
    # @staticmethod
    
    def description(self):
        return f'A {self.__class__.__name__} has traveled {self.distance_traveled} {self.unit}'
