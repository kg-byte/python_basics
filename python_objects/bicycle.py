from vehicle import Vehicle

class Bicycle(Vehicle):
    default_tire = ['tire', 'tire']

    def __init__(self, tires=None, distance_traveled=0, unit='miles', **kwargs):
        super().__init__(distance_traveled, unit, **kwargs)
        if not tires:
            self.tires = self.default_tire
        
    def description(self):
        initial = super().description()
        return f"{initial} on {len(self.tires)} tires"