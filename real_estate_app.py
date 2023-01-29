class Project:
    def __init__(self, name, location, price, bedrooms, bathrooms, sqft):
        self.name = name
        self.location = location
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.sqft = sqft

projects = [
    Project("Project A", "City A", 100000, 2, 1, 1000),
    Project("Project B", "City B", 200000, 3, 2, 1500),
    Project("Project C", "City C", 300000, 4, 3, 2000)
]

def display_projects(projects):
    for project in projects:
        print("Name:", project.name)
        print("Location:", project.location)
        print("Price:", project.price)
        print("Bedrooms:", project.bedrooms)
        print("Bathrooms:", project.bathrooms)
        print("Square Feet:", project.sqft)
        print("---")

display_projects(projects)
