from boat import Boat
from car import Car

class AmphibiousVehicle(Car, Boat):
    #AmphibiousVehicle.__mro__ @ shows--- resolution order
#(<class '__main__.AmphibiousVehicle'>, <class 'car.Car'>, <class 'boat.Boat'>, <class 'vehicle.Vehicle'>, <class 'object'>)
    def __init__(self, engine, tires = [], distance_traveled=0, unit='miles', **kwargs):
        super().__init__(engine=engine, tires = tires, distance_traveled=distance_traveled, unit=unit)
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)

    # have a string representation of class/object for debugging or accessing
    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}"

if __name__ == '__main__':
    water_car = AmphibiousVehicle('4 cyl')
    print(water_car)

'''
Notes:
>>> AmphibiousVehicle.__bases__
(<class 'car.Car'>, <class 'boat.Boat'>)

>>> Vehicle.__subclasses__() --- currently loaded only
[<class 'boat.Boat'>, <class 'car.Car'>]

>>> from bicycle import Bicycle
>>> Vehicle.__subclasses__()
[<class 'boat.Boat'>, <class 'car.Car'>, <class 'bicycle.Bicycle'>]

>>> dir(AmphibiousVehicle)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_variable', 'default_tire', 'description', 'drive', 'travel', 'voyage']

>>> hasattr(Boat, 'boat_type')
False
>>> boat = Boat()
>>> hasattr(boat, 'boat_type')
True
>>> hasattr(Car, 'default_tire')
True

>>> issubclass(Boat, Vehicle)
True
>>> issubclass(Boat, Bicycle)
False


>>> Vehicle.__subclasses__()
[<class 'boat.Boat'>, <class 'car.Car'>, <class 'bicycle.Bicycle'>]
>>> issubclass(AmphibiousVehicle, Vehicle)
True



>>> water_car = AmphibiousVehicle('4 cyl')
>>> isinstance(water_car, Bicycle)
False
>>> isinstance(water_car, AmphibiousVehicle)
True
>>> isinstance(water_car, Boat)
True
>>> type(water_car)
<class '__main__.AmphibiousVehicle'>

water_car.__dict__
{'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'tires': ['tire', 'tire', 'tire', 'tire']}
>>> dir(water_car)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'boat_type', 'class_variable', 'default_tire', 'description', 'distance_traveled', 'drive', 'tires', 'travel', 'unit', 'voyage']

<class '__main__.AmphibiousVehicle'>
>>> Boat.__module__
'boat'
>>> AmphibiousVehicle.__module__
'__main__' (mains the module that the shell is in)


'''