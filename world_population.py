import json
from country_codes import get_country_code
import pygal
from pygal.style import LightColorizedStyle, RotateStyle

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

# Group countries into 3 population levels.
lvl1, lvl2, lvl3 = {}, {}, {}
for cc, population in cc_population.items():
    if population < 10_000_000:
        lvl1[cc] = population
    elif population < 1_000_000_000:
        lvl2[cc] = population
    else:
        lvl3[cc] = population

# See how many countries are in each level.
print(len(lvl1), len(lvl2), len(lvl3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', lvl1)
wm.add('10-1bn', lvl2)
wm.add('>1bn', lvl3)

wm.render_to_file('world_population.svg')
