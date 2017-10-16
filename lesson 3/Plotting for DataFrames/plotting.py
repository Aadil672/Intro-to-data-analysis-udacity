import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for this block of code to see what it does

# groupby() without as_index
if False:
    first_even = example_df.groupby('even').first()
    print first_even
    print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame
    
# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print first_even
    print first_even['even'] # Now 'even' is still a column in the DataFrame

filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!

group_rain=subway_df.groupby('rain')
#print group_rain.groups
mean_group=group_rain.mean()['ENTRIESn_hourly']

print mean_group

%pylab inline
mean_group.hist()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

group_weather=subway_df.groupby(['weather_lat','weather_lon'],as_index=False).mean()

scaled_entries=group_weather['ENTRIESn_hourly']/group_weather['ENTRIESn_hourly'].std()
%pylab inline
plt.scatter(group_weather['weather_lat'],group_weather['weather_lon'],s=scaled_entries)
