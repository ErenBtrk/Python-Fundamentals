import requests

class MovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "90121eb457d5689cc4b2291ba093bb74"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&language=en-US&page=1")
        return response.json()

movieApi = MovieDB()

while True:
    choice = input("1- Popular Movies\n2- Search Movies\n3- Exit\nYour Choice : ")

    if choice == "3":
        break
    else:
        if choice == "1" :
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])
        elif choice == "2":
            keyword = input("Keyword : ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie["name"])

