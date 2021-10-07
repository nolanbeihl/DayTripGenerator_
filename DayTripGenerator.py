import random

list_locations = [ 'Middle of nowhere', 'downtown', 'mountains', 'The Movies']
restaurants = [ 'rabbit hole', 'in and out', 'food truck']
vehicles = ['tigger', 'wilbur', 'probie']
entertainments = ['movie', 'stars', 'people watching']
def start_over():
    get_location()
    pick_food()
    pick_vehicle()
    pick_activity()

def location_generator():
    random_location = random.choice(list_locations)
    location_pick = random_location
    return location_pick

def get_location():
    user_pick = input('Would you like to go to ' + location_generator() + '?: ')
    if user_pick == 'no':
        get_location()
    else:
        location_pref = location_generator  
        return location_pref 
get_location()

def restaurant_pick():
    random_restaurant = random.choice(restaurants)
    restaurant_picked = random_restaurant
    return restaurant_picked

def pick_food():
    food_choice = input('Would you like to eat ' + restaurant_pick() + '?: ')
    if food_choice == 'no':
        pick_food()
    else:
        food_pref = restaurant_pick
        return food_pref
pick_food()

def vehicle_choice():
    random_vehicle = random.choice(vehicles)
    vehicle_pick = random_vehicle
    return vehicle_pick

def pick_vehicle():
    which_vehicle = input('Would you like to take' + vehicle_choice() + '?: ')
    if which_vehicle == 'no':
        pick_vehicle()
    else:
        vehicle_pref = vehicle_choice
        return vehicle_pref
pick_vehicle()        

def activity():
    random_activity = random.choice(entertainments)
    activity_picked = random_activity
    return activity_picked

def pick_activity():
    what_to_do = input(' Do you want to' + activity() + '?: ' )
    if what_to_do == 'no':
        pick_activity()
    else:
        activity_pref = activity()
        return activity_pref
pick_activity()

def confirmed():
    print(' So we will take ' + vehicle_pref + ' and go ' + location_pref + ' but first we will ' + food_pref + ' before we ' + activity_pref)

def confirmation():
    decision = input('Are you sure on what you have decided?: ')
    if decision == 'no':
        print('well then I do not know what to tell you')
        start_over()
    else:
        confirmed()

confirmed()


















# print(list_locations[random_location])




# import random
# l = ['a','b','c','d','e']
# i = random.choice(range(len(l)))
# print(l[i])











