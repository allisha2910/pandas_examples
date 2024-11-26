import pandas as pd
#--------------------------------------------------------

# languages = pd.Series(["Python", "Javascript", "HTML", "SQL"]) #series = like a list, naming out the contents in a indexed list

# # print(languages)

# # #object = strings or a mix of data types, cannot find the median and mean

# rankings = pd.Series([3, 1, 2, 4])

# print(rankings)

# df = pd.DataFrame([("Anne", 30),("Bill", 27),("Charlie", 55)], columns=["Name", "Age"])

# print(df)

# df = pd.DataFrame({
#     "Languages": languages,
#     "Ranking": rankings
# })

# print(df)

#concat = joing 2 lists together
#------------------------------------------------------
#3 ways of adding column labels :
# 1) columns = ["name", ...] 
# 2) adding columns to 2 or more separate pieces of information pd.DataFrame({ "Languages": languages, "Ranking": rankings }) and 
# 3) to bring 2 strings/lists together df = pd.concat([languages, rankings], axis = 1) df.columns = ["Languages", "Ranking"] df = pd.concat([languages, rankings], axis = 1) df.columns = ["Languages", "Ranking"]
#-----------------------------------------------------

# df = pd.concat([languages, rankings], axis = 1)
# df.columns = ["Languages", "Ranking"]
# print(df)

#------------------------------------------------------
#exisiting structures
#spaces separate one value from another
#in data a COMMA is used as a delimiter to separate the values apart. 
#if its already in CSV format u can read the file

# df = pd.read_csv("speeds.csv")

# print(df)

#------------------------------------------------------

#activity 1 - 

# df = pd.DataFrame({
#     "Name": [
#         "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
#         ],
#     "Average Temp": [
#         167, 464, 15, -65, -110, -140, -195, -200
#         ],
#     "Radius (km)": [
#         2437.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622
#         ],
#     "Colour": [
#         "Grey", "Grey", "Blue", "Red", "Orange", "Yellow", "Blue"
#         ],
#     "Interesting Feature": [
#         "It is the smallest planet in the Solar System", "Most densest atmosphere", "Only planet sustaining liquid surface water", "Covered in iron-oxide dust.", "Its diameter is eleven times that of Earth", "Second largest in the solar system", "42 years of sunlight and 42 years of darkness", "Has winds reaching speeds of almost 600 m/s (2,200 km/h; 1,300 mph)"
#         ]
#  })

# print(df)
#-----------------------------------------------------------------

df = pd.DataFrame({
    "Name": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Average Temp": [167, 464, 15, -65, -110, -140, -195, -200],
    "Radius (km)": [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622],
    "Colour": ["Grey", "Yellow", "Blue", "Red", "Orange", "Yellow", "Blue", "Blue"],
    "Interesting Feature": ["It is the smallest planet in the Solar System", 
                            "Most densest atmosphere", 
                            "Only planet sustaining liquid surface water", 
                            "Covered in iron-oxide dust", 
                            "Its diameter is eleven times that of Earth", "Second largest in the solar system", "42 years of sunlight and 42 years of darkness", "Has winds reaching speeds of almost 600 m/s"]
})

df = pd.DataFrame(df)

print(df)

#adding a new column - who found the planets

new_data=pd.DataFrame({"Founded by":["Galileo", "Galileo", "Nicolaus Copernicus", "Galileo", "Galileo", "Galileo", "William Herschel", "Johann Galle"]}) 
df = pd.concat([df, new_data], axis=1)

print(df)

new_data=pd.DataFrame({"Year discovered":["17thC", "16thC", "1515", "1610", "1610", "1610", "1781", "1846"]})
df = pd.concat([df, new_data], axis=1)

print(df)

new_data=pd.DataFrame({"Elements of comp":["Iron, Nickel, Oxygen", "Dioxide, Nitrogen, Sulfur Dioxide", "Nitrogen, Oxygen, Argon", "Carbon Dioxide, Nitrogen, Argon", "Hydrogen, Helium, Methane", "Hydrogen, Helium, Ammonia", "Hydrogen, Helium, Methane", "Hydrogen, Helium, Methane"]})
df = pd.concat([df, new_data], axis=1)

print(df)