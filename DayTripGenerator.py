import random

list_locations = [ 'to the middle of nowhere', 'downtown', 'to the mountains', 'to the Movies']
restaurants = [ 'the rabbit hole', 'in and out', 'a food truck']
vehicles = ['tigger', 'wilbur', 'probie']
entertainments = ['go to the movies', 'look at the stars', 'people watch']
def start_over():
    final_choice = pick_location()
    pick_food()
    pick_vehicle()
    pick_activity()

def location_generator():
    random_location = random.choice(list_locations)
    return random_location

def pick_location():
    not_satisfied = True
    while (not_satisfied):
        chosen_location = location_generator()
        user_pick = input('Would you like to go to ' + chosen_location + '?: ')
        if user_pick == 'yes':
            not_satisfied = False
            return chosen_location


def restaurant_pick():
    random_restaurant = random.choice(restaurants)
    return random_restaurant

def pick_food():
    dislikes = True
    while (dislikes):
        restaurant_option = restaurant_pick()
        user_pick_food = input('Would you like to eat at ' + restaurant_option + '?: ')
        if user_pick_food == 'yes':
            dislikes = False
            return restaurant_option

def vehicle_choice():
    random_vehicle = random.choice(vehicles)
    return random_vehicle

def pick_vehicle():
    ride_pref = True
    while (ride_pref):
        ride_option = vehicle_choice()
        user_ride_choice = input('Would you like to take ' + ride_option + '? ')
        if user_ride_choice == 'yes':
            ride_pref = False
            return ride_option   

def activity():
    random_activity = random.choice(entertainments)
    return random_activity

def pick_activity():
    activity_pref = True
    while (activity_pref):
        activity_option = activity()
        user_activity_choice = input('Would you like to ' + activity_option + ' afterwards? ')
        if user_activity_choice == 'yes':
            activity_pref = False
            return activity_option


# * Main Function
def confirmation():
    do_over = True
    while(do_over):
        final_loc = pick_location()
        final_food = pick_food()
        final_veh = pick_vehicle()
        final_act = pick_activity()
        decision = input('Are you sure on what you have decided?: ')
        if decision == 'no':
            print('ok, lets try again')
        
        else:
            confirmed(final_loc, final_veh, final_food, final_act)
            do_over = False

def confirmed(fn_loc, fn_veh, fn_food, fn_act):
    print('So we will take ' + fn_veh + ' and go ' + fn_loc + ' but first we will eat at ' + fn_food + ' before we ' + fn_act)

confirmation()



















# print(list_locations[random_location])




# import random
# l = ['a','b','c','d','e']
# i = random.choice(range(len(l)))
# print(l[i])











