import pandas as pd
df = pd.read_csv("spotify_songs.csv")

# print(df.shape) #to see how big our data frame is

#tuple stores iits a collection of nfomation like a list (diff because it cannot be changed) in brackets (sefew, eetewr, rere)

#it is used where ORDER is important, USEFUL FOR DATA THAT HAS MEANING E.G. COORDINATES.

# print(df.columns) #lists all of the column names 

# print(df.info) #shows you how many rows and columns 

# print(df["playlist_genre"].value_counts()) #shows you how many times genres appeared., can find the mode - MOST POPULAR

# print(df["playlist_genre"].mode())

# print(df["duration_ms"].median())

# print(df["duration_ms"].mean()) 

# max_ms = df["duration_ms"].max()
# min_ms = df["duration_ms"].min()
# print(max_ms - min_ms) #cant find the range, instead min and max range
#print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"]))

# print(df.groupby('playlist_genre')["duration_ms"].min())

# print(df.query("track_artist=='Ricky Martin'"))

# mean_val = df["duration_ms"].mean()

# print(df.query("track_artist=='Ricky Martin'"))

# print(df.query("duration_ms > mean_val"))

# print(df.query(f"duration_ms >= {mean_val}"))
