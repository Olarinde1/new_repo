new = 4
old = 1
temp = new
new = old
old = temp
print(new, old)

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    #Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK.
    temp_var = you.apples
    you.apples = me.apples
    me.apples = temp_var
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    you.ideas = you.ideas + me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation
	highest_elevation = 0
	return_city = ""

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population > min_population:
		if highest_elevation < city1.elevation:
			highest_elevation=city1.elevation
			return_city = ("{}, {}".format(city1.name, city1.country))
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population > min_population:
		if highest_elevation < city2.elevation:
			highest_elevation=city2.elevation 
			return_city = ("{}, {}".format(city2.name, city2.country))
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population > min_population:
		if highest_elevation < city3.elevation:
			highest_elevation = city3.elevation
			return_city = ("{}, {}".format(city3.name, city3.country))

	#Format the return string
	if return_city != "":
		return return_city
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = 'brown'
table.material = 'wood'

couch = Furniture()
couch.color = 'red'
couch.material = 'leather'

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

class Piglet:
    name = "Piglet" # this is an instance variable
    def speak(self):
        print("oink I'm {}! oink!".format(self.name))

hamlet = Piglet()
hamlet.name = 'Hamlet'
hamlet.speak()
cut = Piglet()
cut.speak()
petunia = Piglet()
petunia.name = 'Petunia'
petunia.speak()

# An instance variable is a variable that have different values 
# for different instances of the same class

class NewPig:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = NewPig()
print(piggy.pig_years())
piggy.years = 2
print(piggy.pig_years())

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apples is {} and its flavor is {}".format(self.color, self.flavor)


jonalgold = Apple('red', 'sweet')
print(jonalgold.color)
print(jonalgold.flavor)
print(jonalgold)

# print(help(Apple))

class NewPiglet:
    """Represents piglet that can say their name."""
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print( "Oink! I'm {}! Oink!.".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18

# print(help(NewPiglet))

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom 
        self.top = top
        self.current = current
    def __str__(self):
        return "current floor: {}".format(self.current)
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current<10:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current> 0:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor <= self.top and floor >= self.bottom:
            self.current = floor
        elif floor < 0:
            self.current = 0
        else:
            self.current = 10

elevator = Elevator(-1, 10, 0)
elevator.up() 
print(elevator.current)
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
elevator.go_to(5)
print(elevator)

#----------------------INHERITANCE----------------------
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple('green', 'tart')
crarnelian = Grape("purple","sweet")
print(granny_smith.flavor)

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Moooo"

milky = Cow("Milky White")
milky.speak()

# Always initialize mutable attributes in the constructor
class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package_name, package):
        self.packages[package_name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

    
pac = Repository()
pac.add_package('new_package', 'continue')
pac.add_package('another', 'alpha')
print(pac.packages)

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

