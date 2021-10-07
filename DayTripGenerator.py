import random

list_locations = [ 'Middle of nowhere', 'downtown', 'mountains', 'The Movies']
restaurants = [ 'rabbit hole', 'in and out', 'food truck']
vehicles = ['tigger', 'wilbur', 'probie']
entertainments = ['go to the movies', 'look at the stars', 'people watch']
def start_over():
    get_location()
    pick_food()
    pick_vehicle()
    pick_activity()

def location_generator():
    random_location = random.choice(list_locations)
    return random_location

def get_location():
    user_pick = input('Would you like to go to ' + location_generator() + '?: ')
    if user_pick == 'no':
        get_location()
    else:
        return location_generator()

get_location()

def restaurant_pick():
    random_restaurant = random.choice(restaurants)
    return random_restaurant

def pick_food():
    food_choice = input('Would you like to eat ' + restaurant_pick() + '?: ')
    if food_choice == 'no':
        pick_food()
    else:
        return restaurant_pick()
pick_food()

def vehicle_choice():
    random_vehicle = random.choice(vehicles)
    return random_vehicle

def pick_vehicle():
    which_vehicle = input('Would you like to take ' + vehicle_choice() + '?: ')
    if which_vehicle == 'no':
        pick_vehicle()
    else:
        return vehicle_choice()
pick_vehicle()        

def activity():
    random_activity = random.choice(entertainments)
    return random_activity

def pick_activity():
    what_to_do = input('Do you want to ' + activity() + '?: ' )
    if what_to_do == 'no':
        pick_activity()
    else:
        return activity()
pick_activity()

def confirmation():
    decision = input('Are you sure on what you have decided?: ')
    if decision == 'no':
        print('ok, lets try again')
        start_over()
    else:
        confirmed()

def confirmed():
    print('So we will take ' + pick_vehicle() + ' and go ' + get_location() + ' but first we will eat at ' + pick_food() + ' before we ' + pick_activity())

confirmed()


















# print(list_locations[random_location])




# import random
# l = ['a','b','c','d','e']
# i = random.choice(range(len(l)))
# print(l[i])











