import pandas as pd 

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
rankings = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": rankings})

# df.loc[4] = ["PHP", 11]

# df.loc[3.5] = ["KESL", 28]  #just adds it to the bottom when it was supposed to go between 3 and 4 

# df = df.sort_index() #to put the numbers in order and put 3.5 in the right place 
# df = df.reset_index(drop=True) #resets and uses the old referencing and creates a new column| DROP = TRUE = leave out the new index, keyword arguement. 

print(df)

new_data = pd.DataFrame({
    "Languages": ["PHP"],
    "Ranking": [11]
})

df = pd.concat([df,new_data], ignore_index=True)

df.loc[5] = ["Java", 7]
df.loc[6] = ["Typescript", 5]

print(df)

df["Ranking 2022"] = [4,1,2,3,10,6,5]
df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]

print(df)

df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])

print(df)

df.rename(columns={"Ranking":"Ranking 2023"}, inplace=True)

print(df)

df = df.set_index("Languages")
print(df)


# new_data=pd.DataFrame({"2019":[4,1,2,3,8,5,10]})
# df = pd.concat([df, new_data], axis=1)

# print(df)

#adding to list and data frame, 1) add it to the list at the end, however if you cannot access the orginal data... amend the dataframe. need to add a new row, df.loc -- location df.loc[4](row/poisiton, if not it will go automatically to the bottom) = ["php", 11 (data)]
#adding more than 2 use concat 
#adding a new list df["list name"] = [data, along, in a, list, format ]
#can also concatinate : new_data=pd.DataFrame({"Ranking 2022":[4,1,2,3,10,6,5]}) df = pd.concat([df, new_data], axis=1)