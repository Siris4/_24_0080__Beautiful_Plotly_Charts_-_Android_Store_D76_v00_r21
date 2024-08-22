import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0080__Day76_Beautiful_Plotly_Charts_&_Android_Store__240820\NewProject\r00-r09 START\r00_env_START\apps.csv'
df = pd.read_csv(file_path)

# Count the number of occurrences of each genre in the 'Genres' column
genre_counts = df['Genres'].value_counts()

# Create a bar chart with varying colors
fig = px.bar(
    x=genre_counts.index,  # Genre names
    y=genre_counts.values, # Count of each genre
    labels={'x': 'Genre', 'y': 'Count'},
    title="Number of Apps by Genre",
    color=genre_counts.values,  # Use the count as the color scale
    color_continuous_scale=px.colors.sequential.Viridis  # You can choose different color scales
)

# Show the bar chart
fig.show()
