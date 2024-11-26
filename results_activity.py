import pandas as pd
df = pd.read_csv("results.csv")

# print(df.shape)
# print(df.columns)
# print(df.info)
# print(df["tournament"].value_counts()) #147 #Friendly = 17773, FIFA World Cup qualification, 8016, UEFA Euro qualification  2815
# print(df["home_team"].mode()) #brazil most common home team
# print(df["away_team"].mode()) uruguay most common away team 

# min_ms = df["home_team"].min()#least reported away team 
# print(df["home_team"].min())
# max_ms = df["home_team"].mode()#most reported way team 
# print(df["home_team"].mode())

# min_ms = df["away_team"].min()#least reported away team 
# print(df["away_team"].min())
# max_ms = df["away_team"].mode()#most reported way team 
# print(df["away_team"].mode())

print(df.query("home_team=='England'")) #how many times england playedat home in each tournament
#how many times england scored a more than average amounts of goals at a home match
#how many times england scored a more than average amount of goals at an away match 
#what is englands average amount of goals scored at home?
#what is each teams average home score and away score?