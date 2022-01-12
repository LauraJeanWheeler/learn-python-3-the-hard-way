# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'Sanfran',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some more cities 
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print out some states
print('-' * 10)
print(f"Michigan's abbreviation is: {states['Michigan']}")
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print(f"Michigan has {cities[states['Michigan']]}")

#print every state abbreviation
print('-' * 10)
#tuple unpacking, items 
# The method items() returns a list of dict's (key, value) tuple pairs
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# The method get() returns a value for the given key. 
# If key is not available then returns default value None.
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with a default value 
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")