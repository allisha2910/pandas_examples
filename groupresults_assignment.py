import pandas as pd

csv_file = "group_results(Sheet1).csv"  # Replace with your CSV file path
df = pd.read_csv(csv_file)

excel_file = "output_file.xlsx"  # Desired output file path
df.to_excel(excel_file, index=False)

# print(df)

# average_download = df["Mean Download"].mean()
# average_upload = df["Mean Upload"].mean()

# print(f"Average Download Speed: {average_download:.2f} Mbps")
# print(f"Average Upload Speed: {average_upload:.2f} Mbps")

# # Calculate the fastest, slowest, and median speeds
# fastest_download = df["Fastest Download"].max()
# slowest_download = df["Slowest Download"].min()
# fastest_upload = df["Fastest Upload"].max()
# slowest_upload = df["Slowest Upload"].min()

# print(f"Fastest Download Speed: {fastest_download} Mbps")
# print(f"Slowest Download Speed: {slowest_download} Mbps")
# print(f"Fastest Upload Speed: {fastest_upload} Mbps")
# print(f"Slowest Upload Speed: {slowest_upload} Mbps")

# # # Calculate the mean (average) download speed
# mean_download = df["Mean Download"].mean()
# # # Display the result
# print(f"The mean download speed is {mean_download:.3f} Mb/s")

# # # Calculate the median download speed
# median_download = df["Median Download"].median()

# # # Display the result
# print(f"The median download speed is {median_download:.3f} Mb/s")

# # # Calculate the mean (average) upload speed
# mean_upload = df["Mean Upload"].mean()

# # # Display the result
# print(f"The mean upload speed is {mean_upload:.3f} Mb/s")

# # Calculate the median upload speed
median_upload = df["Median Upload"].median()

# # Display the result
print(f"The median upload speed is {median_upload:.3f} Mb/s")