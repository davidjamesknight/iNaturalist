#  Pull data on pine rockland species from the iNaturalist API

import pandas as pd
import numpy as np

taxonIDs = [
  # Butterflies
  50075, # Atala
  49766,  # Zebra Longwing
  49150, # Gulf Fritillary
  50073, # Julia
  67440, # Bella
  257122, # Fauthful Beauty
  # Snakes
  27138, # Everglades Racer
  # Spiders
  49756 # Golden Orbweaver
]
# Boundary box
nelat = 25.986611
nelng = -80.119651
swlat = 25.379583
swlng = -80.626421

# Call API
results = []

for t in taxonIDs:
  results.append(pd.read_json('https://www.inaturalist.org/observations.json?taxon_id=' + str(t) + '&nelat=' + str(nelat) + '&nelng=' + str(nelng) + '&swlat=' + str(swlat) + '&swlng=' + str(swlng)))
df = pd.concat(results)

# Cleanup
df['taxon_name'] = df['taxon'].apply(lambda x: x["name"])
df['common_name'] = df['taxon'].apply(lambda x: x["common_name"]["name"])
# df['observed_on'] = np.where(df['time_observed_at'].notnull(), df['time_observed_at'], df['observed_on'] )

df[['observed_on', 'time_observed_at', 'taxon_id', 'taxon_name', 'common_name', 'latitude', 'longitude', 'place_guess', 'description', 'user_login']].to_csv("df.csv", index=False)
print("Done!")