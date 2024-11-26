import pandas as pd

df = pd.read_excel("results2024-11-25-1426.xlsx")
# # Find the fastest download speed and its timestamp
fastest_download = df["Download (Mb/s)"].max()
fastest_download_time = df.loc[df["Download (Mb/s)"].idxmax(), "Date-time"]

print(f"The fastest download speed recorded is {fastest_download:.3f} Mb/s")
print(f"It was recorded at {fastest_download_time}")

# # Find the slowest download speed
slowest_download = df["Download (Mb/s)"].min()

# # Find the timestamp of the slowest download speed
slowest_download_time = df.loc[df["Download (Mb/s)"].idxmin(), "Date-time"]

# # Display the results
print(f"The slowest download speed recorded is {slowest_download:.3f} Mb/s")
print(f"It was recorded at {slowest_download_time}")

# # Calculate the mean (average) download speed
mean_download = df["Download (Mb/s)"].mean()

# # Display the result
print(f"The mean download speed is {mean_download:.3f} Mb/s")

# # Calculate the median download speed
median_download = df["Download (Mb/s)"].median()

# # Display the result
print(f"The median download speed is {median_download:.3f} Mb/s")

# # Find the fastest upload speed
fastest_upload = df["Upload (Mb/s)"].max()

# # Find the timestamp of the fastest upload speed
fastest_upload_time = df.loc[df["Upload (Mb/s)"].idxmax(), "Date-time"]

# # Display the result
print(f"The fastest upload speed recorded is {fastest_upload:.3f} Mb/s")
print(f"It was recorded at {fastest_upload_time}")

# # Find the slowest upload speed
slowest_upload = df["Upload (Mb/s)"].min()

# # Find the timestamp of the slowest upload speed
slowest_upload_time = df.loc[df["Upload (Mb/s)"].idxmin(), "Date-time"]

# # Display the result
print(f"The slowest upload speed recorded is {slowest_upload:.3f} Mb/s")
print(f"It was recorded at {slowest_upload_time}")

# # Calculate the mean (average) upload speed
mean_upload = df["Upload (Mb/s)"].mean()

# # Display the result
print(f"The mean upload speed is {mean_upload:.3f} Mb/s")

# # Calculate the median upload speed
median_upload = df["Upload (Mb/s)"].median()

# # Display the result
print(f"The median upload speed is {median_upload:.3f} Mb/s")

# # Sort the DataFrame by Upload (Mb/s) in descending order
sorted_df = df.sort_values(by="Upload (Mb/s)", ascending=False)

# # Display the sorted DataFrame
print(sorted_df)

# # Sort the DataFrame by Upload (Mb/s) in ascending order (slowest to fastest)
sorted_df_slowest = df.sort_values(by="Upload (Mb/s)", ascending=True)

# # Display the sorted DataFrame
print(sorted_df_slowest)

# Calculate the mean download speed
mean_download = df["Download (Mb/s)"].mean()

# Filter the rows where the download speed is faster than the mean
faster_than_mean = df[df["Download (Mb/s)"] > mean_download]

# Display the result
print(faster_than_mean)