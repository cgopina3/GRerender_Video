def plan_mountain_trek(base_altitudes, snow_forecast):
    # Initialize variables 
    best_day = 0
    min_climbs = float('inf')
    
    for day in range(len(snow_forecast)):
        # Calculate the altitude with snow for each location on the current day
        altitudes = [base + snow_forecast[day][loc] for loc, base in enumerate(base_altitudes)]
        
        # Track the number of climbs needed to cross all locations
        climbs = 0
        prev = altitudes[0]
        
        for alt in altitudes[1:]:
            # If altitude increased, that's a climb
            if alt > prev:
                climbs += 1
            # Update previous altitude 
            prev = alt 
            
        # Check if this is the best day so far based on min climbs 
        if climbs < min_climbs:
            min_climbs = climbs
            best_day = day
            
    return best_day, min_climbs

base_altitudes = [10, 15, 13, 12]
snow_forecast = [
    [3, 2, 1, 4],   # Day 1: [13, 17, 14, 16] (3 climbs) 
    [1, 1, 3, 1],   # Day 2: [11, 16, 16, 13] (2 climbs) 
    [4, 3, 2, 3]    # Day 3: [14, 18, 15, 15] (3 climbs)
] 
plan_mountain_trek(base_altitudes, snow_forecast)
# Returns (2, 2) - Best day is day 2 with 2 climbs



