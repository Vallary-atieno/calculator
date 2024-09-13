class City:
    def __init__(self,name,country,size):
        self.name=name
        self.country=country
        self.size=size
city1=City("Nairobi","Kenya","Big")
city2=City("Kampala","Uganda","Medium")
print(city1.name, city1.country, city1.size)
print(city2.name,city2.country,city2.size)