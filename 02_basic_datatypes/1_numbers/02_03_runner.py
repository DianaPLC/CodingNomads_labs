'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
distance_in_miles = 10
time_minutes_part = 30
time_seconds_part = 30

time_in_hours = (time_minutes_part/60)+(time_seconds_part/3600)
distance_in_km = distance_in_miles*1.6

km_per_hour = distance_in_km/time_in_hours

print(km_per_hour)
