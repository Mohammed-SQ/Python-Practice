def add_cities():
    cities = []
    while True:
        city = input("Enter city name (or 'done' to stop): ")
        if city == "done":
            break
        cities.append(city)
    return cities

def show_long_cities(city_list):
    long_cities = []
    for city in city_list:
        if len(city) > 5:
            long_cities.append(city)

    if len(long_cities) == 0:
        print("No long city names.")
    else:
        print("Long city names:")
        print(long_cities)

def main():
    # get the list
    travel_list = add_cities()

    # print all cities
    print("\nYour travel list:")
    print(travel_list)
    print()

    # show long cities
    show_long_cities(travel_list)

# MUST call main
main()
