import pandas as pd

df = pd.read_csv("USvideos.csv")

print(df.columns)

# Print first 10 records

print(df.head(10))

# Print second 10 records

print(df[10:].head(10))

# Print column names and the number of columns

print(f"Column names :\n {df.columns}\nNumber of columns = {len(df.columns)}")

# 4- Delete all the columns below and list remaining columns
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)
print(df)
print(df.columns)

# Print average of like and dislike numbers

print(f"Average of likes = {df['likes'].mean():.7}\nAverage of dislikes = {df['dislikes'].mean():.5} ")

# Print first 50 video's like and dislike columns

print(df[["likes","dislikes"]].head(50))

# Which video is the most viewed ?

mostViewedVideoIndex = df["views"].idxmax(axis = 1, skipna = True)
print(f"Most viewed video is = {df['title'][mostViewedVideoIndex]}\nView amount is = {df['views'][mostViewedVideoIndex]}")

# Which video has the lowest view amount ? 

lowestViewedVideoIndex = df["views"].idxmin(axis=1,skipna=True)
print(f"Lowest viewed video is = {df['title'][lowestViewedVideoIndex]}\nView amount is = {df['views'][lowestViewedVideoIndex]}")


# Print first 10 most viewed videos

print(df.nlargest(10,["views"])[["title","views"]])

# Print like averages by categories in ascending order

print(df.groupby("category_id")["likes"].mean())

# Print comment counts by categories in order

print(df.groupby("category_id")["comment_count"].mean())

# How many videos per category?

print(df["category_id"].value_counts(ascending=True))

# Print length of title of each video in a new column

df["title_length"] = df["title"].str.len()
print(df[["title","title_length"]])

# Print tag number of each video in  a new column

def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)

print(df[["tags","tag_count"]])


#Print most popular videos according to likes/dislikes


df["like-dislike-rate"] = df["likes"] / (df["likes"] + df["dislikes"])

print(df.nlargest(20,["like-dislike-rate"])[["title","likes","dislikes","like-dislike-rate"]])



