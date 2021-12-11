import pandas as pd

df = pd.read_csv('final.csv')

articals = df[21]

output = articals[['contentId', 'personId', 'contentType', 'total_views']].head(20).values.tolist()