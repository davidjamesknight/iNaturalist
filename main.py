import pandas as pd
import numpy as np

taxonIDs = [

    # Insects
    50075,  # Atala Butterfly
    49766,  # Zebra Longwing Butterfly
    49150,  # Gulf Fritillary Butterfly
    50073,  # Julia Heliconian Butterfly
    257122,  # Faithful Beauty Butterfly
    67440,  # Ornate Bella Moth

    # Reptiles
    27138,  # Everglades Racer
    26575,  # Ringneck snake
    36514,  # Green anole

    # Spiders
    49756,  # Golden Orbweaver
    53467,  # Orchard orbweaver
    49540,  # Spiny backed orbweaver

    # Snails
    49755,  # Lined tree snail

    # Birds
    14995,  # Gray Catbird
    199916,  # Black-throated blue warbler
    7493,  # Blue gray gnatcatcher
    18205,  # Red bellied woodpecker
    6432,  # Ruby-throated hummingbird
    145249,  # Prairie warbler
    8229,  # Blue jay
    9083,  # Northern cardinal
    14886,  # Northern mockingbird

    # Mammals
    42076  # Gray fox
]
# Boundary box for Miami-Dade County
nelat = 25.986611
nelng = -80.119651
swlat = 25.379583
swlng = -80.626421

# Call API
results = []

for t in taxonIDs:
    results.append(pd.read_json('https://www.inaturalist.org/observations.json?taxon_id='
        + str(t)
        + '&nelat=' + str(nelat)
        + '&nelng=' + str(nelng)
        + '&swlat=' + str(swlat)
        + '&swlng=' + str(swlng)))
df = pd.concat(results)

# Extract data from the object in the 'taxon' column
df['taxon_name'] = df['taxon'].apply(lambda x: x["name"])
df['common_name'] = df['taxon'].apply(lambda x: x["common_name"]["name"])

df[['observed_on', 'time_observed_at', 'taxon_id', 'taxon_name', 'common_name', 'latitude',
    'longitude', 'place_guess', 'description', 'user_login']].to_csv("ctpn.csv", index=False)
print("Done!")
