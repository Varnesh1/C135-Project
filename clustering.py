import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('stargravity.csv')

correct_distance = []

for index, planet_data in data.iterrows():
  if float(planet_data[2]) > 150 and float(planet_data[2]) < 350:
    correct_distance.append(planet_data)

print(correct_distance)

planet_name = []
planet_distance = []
planet_mass = []
planet_radius = []
planet_gravity = []

for p in correct_distance:
  planet_name.append(p[1])
  planet_distance.append(p[2])
  planet_mass.append(p[3])
  planet_radius.append(p[4])
  planet_gravity.append(p[5])




datafreame = pd.DataFrame(
  list(zip(planet_name, planet_distance, planet_mass, planet_radius, planet_gravity)), 
  columns= ['Name', 'Distance', 'Mass', 'Gravity', 'Radius'] 
)
datafreame.to_csv('stargravityfinal.csv')
 