counties = ["Arapahoe", "Denver", "Jefferson"]

if "Arapahoe" in counties and "El Paso" not in counties:
        print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson" : 432438}

numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)
for i in range(len(counties)):
        print(counties[i])

for counties in counties_dict:
    print(county)

for county in counties_dict: 
    print(counties)
for voters in counties_dict.values():
    print(voters)

for county in counties_dict :
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key, value)
for county, voters in counties_dict.items():
        print(county, voters)
for key, value in counties_dict.items():
        if key == "Arapahoe":
            print(str((key)) + " county has " + str((value)) + " registered voters")
for key, value in counties_dict.items():
        if key == "Denver":
            print(str((key)) + " county has " + str((value)) + " registered voters")
for key, value in counties_dict.items():
        if key == "Jefferson":
            print(str((key)) + " county has " + str((value)) + " registered voters")
my_votes = int(input("how many did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print(f"I recieved {my_votes / total_votes * 100} % of the total votes")
