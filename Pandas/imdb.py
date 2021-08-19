import pandas as pd
df = pd.read_csv("imdb.csv")
# Print information about the file
fileInfo = df 
print(fileInfo.info())
print('*'*120)
fileInfo = df.columns
print(fileInfo)
print('*'*120)


# Print first 5 data
print(df.head()[["Title","Year","Rated","Genre"]])
print('*'*120)

# Print first 10 data
print(df.head(10)[["Title","Year","Rated","Genre"]])
print('*'*120)

# Print lsat 5 data
print(df.tail()[["Title","Year","Rated","Genre"]])
print('*'*120)

# Print last 10 data
print(df.tail(10)[["Title","Year","Rated","Genre"]])
print('*'*120)

# Print only Movie_title column
print(df.head(10)["Title"])
print('*'*120)

# Print only first 5 datas which involves Movie_title and rating columns
print(df.head()[["Title","Rated"]])
print('*'*120)

# Print only last 7 datas which involves Movie_title and rating columns
print(df.tail(7)[["Title","Rated"]])
print('*'*120)

# Print second 5 datas which involves Movie_title and rating columns
print(df[5:15].head()[["Title","Rated"]])
print('*'*120)


#Print first 50 datas >= 8.0 imdb pts which involves movie_title and rating columns 
result = df.query("imdbRating >= 8.0").head(50)[["Title","imdbRating"]]
print(result)
print('*'*120)

#Print movie names which has release dates 2014-2015 
result = df.query("Year == 2014 | Year == 2015")[["Title","Year"]]
print(result)
print('*'*120)

#Print movies which has release year 2011 or imdb points between 8-9
result = df.query("(Year == 2011) and (imdbRating >= 8.0 & imdbRating <= 9.0)")[["Title","imdbRating","Year"]]
print(result)
print('*'*120)