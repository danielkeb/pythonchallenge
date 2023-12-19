travel_log=[
    {
        "country":"france",
        "visited_times":12,
        "cities_visted":['paris','lellin','dijon']
    },
    {
        "country":'germany',
        "visited_times":7,
        "cities_visted":['berlin','hamburg','stuttgart']
    }
]

def add_country(country,visited_times,cities_visited):
   new_country_visited={}
   new_country_visited["country"] = country,
   new_country_visited["visited_times"] = visited_times,
   new_country_visited["cities_visited"] = cities_visited,
   travel_log.append(new_country_visited)
   
add_country('Russian',2,['Moscow','Saint','Stuttgart'])
print(travel_log)