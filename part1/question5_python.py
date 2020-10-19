import pandas as pd 
import json
from matplotlib import pyplot as plt

# Read data 
input_file = open ('/Users/mingxuan/Desktop/fp/part1/question5_array.json')
json_array = json.load(input_file)

# Load json into dataframe
data = pd.DataFrame([], columns = ["hour", "sessions"])
for hour in json_array:
    data = data.append({"hour": int(hour["hour"])
                , "sessions": int(hour["sessions"])}, ignore_index = True)
data.sort_values(["hour"], inplace = True)
 
# Plot 
plt.style.use('fivethirtyeight')
plt.bar(data['hour'].tolist(), data['sessions'].tolist(), label = 'Sessions')
 
plt.legend()
plt.xlabel('Hour of the Day')
plt.ylabel('Sessions')
plt.title('Sessions per Hour of the Day')
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.savefig('part1/question5_hour_per_session_plot.png')
