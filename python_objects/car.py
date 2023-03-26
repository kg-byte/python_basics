from vehicle import Vehicle

class Car(Vehicle):
    default_tire = ['tire', 'tire', 'tire','tire']

    def __init__(self, engine, tires=None, distance_traveled=0, unit='miles', **kwargs):
        super().__init__(engine = engine, distance_traveled=distance_traveled, unit=unit, **kwargs)
        if not tires:
            self.tires = self.default_tire
    
    def drive(self, distance):
        self.distance_traveled += distance
