mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
#initializing empty variables to be added to 
totalMissions = 0
successfulMissions = 0
missionsBefore2000 = []

for i in range(len(mission_names)):
    totalMissions += 1

successfulMissions = sum(mission_success) # i learned this counts all the trues in a list

successRate = successfulMissions / totalMissions * 100

for i in range(len(mission_names)): #for everytime it sees a mission year before 2000, it will add the mission name from the called list and add it to the empty list
    if mission_years[i] < 2000:
        missionsBefore2000.append(mission_names[i])

print(f"Total number of missions: {totalMissions}.")
print(f"Total number of successful missions: {successfulMissions}.")
print(f"This is the success rate: {successRate:.2f}%")
print("Below is the missions launched before the year 2000.")
for i in missionsBefore2000:
    print(f"-{i}")