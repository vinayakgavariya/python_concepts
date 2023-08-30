n = int(input())  # Read the total number of country stamps
country_stamps = set()  # Create an empty set to store distinct country names

for _ in range(n):
    country_name = input()  # Read the country name for each stamp
    country_stamps.add(country_name)  # Add the country name to the set

total_distinct_stamps = len(country_stamps)  # Get the count of distinct stamps
print(total_distinct_stamps)  # Print the total number of distinct country stamps
