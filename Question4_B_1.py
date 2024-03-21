'''
1. Read the provided CSV file ‘data.csv’. https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing
2. Show the basic statistical description about the data.
3. Check if the data has null values.
a. Replace the null values with the mean
4. Select at least two columns and aggregate the data using: min, max, count, mean.
5. Filter the dataframe to select the rows with calories values between 500 and 1000.
6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
8. Delete the “Maxpulse” column from the main df dataframe
9. Convert the datatype of Calories column to int datatype.
'''
import pandas

# Read and display file
dataFrame = pandas.read_csv("data.csv")
pandas.set_option('display.max_rows', None)
#print(dataFrame)

# replace NaNs with the mean
dataFrame.fillna(dataFrame.mean(), inplace=True)
#print(dataFrame)

# Select 2 columns and aggregate data
result = dataFrame.groupby('Duration').agg({'Pulse' : ['min', 'max', 'count', 'mean']})
#print(result)

# Filter dataframe by calories
#print('Rows between 500 and 1000 Calories:\n', dataFrame[(dataFrame['Calories'] >= 500) & (dataFrame['Calories'] <= 1000)])

# Filter dataframe by calories and pulse
#print('Rows with Calories > 500 and Pulse < 100:\n', dataFrame[(dataFrame['Calories'] > 500) & (dataFrame['Pulse'] < 100)])

# Create a new dataframe
df_modified = dataFrame[[ 'Duration', 'Pulse', 'Calories']].copy()
#print(df_modified)

# Delete column from main dataframe
del dataFrame['Maxpulse']
#print(dataFrame)

# Convert datatype of Calories
dataFrame = dataFrame.astype({'Calories' : 'int'})
print(dataFrame)