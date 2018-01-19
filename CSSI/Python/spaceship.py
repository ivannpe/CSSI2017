class Spaceship:
    def __init__(self, name, color, destination, origin, launched):
        self.name = name
        self.color = color
        self.destination = destination
        self.origin = origin
        self.launched = launched
    def description(self):
        return "The {0} is {1} and is going to {2} from {3}".format(self.name,self.color,self.destination,self.origin)
    def is_launched(self):
        if self.launched:
            return " Launched : Yes"
        else:
            return " Launched : Returned"
Apollo11 = Spaceship('Apollo 11', 'Silver', 'Moon', 'Kennedy Space Center', False)
Rover = Spaceship('Mars Rover', 'Silver', 'Mars', 'Kennedy Space Center', True)

print Apollo11.description()
print Apollo11.is_launched()

print Rover.description()
print Rover.is_launched()
