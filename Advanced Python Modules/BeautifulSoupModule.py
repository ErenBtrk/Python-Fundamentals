html_doc = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Web Page</title>
</head>
<body>
    <h1 id = "header">
        Python Course
    </h1>
    <div class = "group1">
        <h2>
            Programming
        </h2>

        <ul>
            <li>Menu-1</li>
            <li>Menu-2</li>
            <li>Menu-3</li>
            <li>Menu-4</li>
        </ul>
    </div>
    
    <div class = "group2">
        <h2>
            Modules
        </h2>

        <ul>
            <li>Menu-1</li>
            <li>Menu-2</li>
            <li>Menu-3</li>
            <li>Menu-4</li>
        </ul>
    </div>

    <div class = "group3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menu-1</li>
            <li>Menu-2</li>
            <li>Menu-3</li>
            <li>Menu-4</li>
        </ul>
    </div>

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

    <img src="bats-upside-down.jpg" alt="">


</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")

result = soup.prettify()
print(result)
result = soup.title
print(result)
result = soup.head
print(result)
result = soup.body
print(result)

result = soup.title.name
print(result)
result = soup.title.string
print(result)

result = soup.h1
print(result)
result = soup.h2
print(result)
result = soup.h2.name
print(result)
result = soup.h2.string
print(result)

result = soup.find_all("h2")
print(result)

result = soup.find_all("h2")[0]
print(result)

result = soup.div
print(result)
result = soup.find_all("div")[1]
print(result)
result = soup.find_all("div")[1].ul.find_all("li")
print(result)

result = soup.div.findChildren()
print(result)
result = soup.div.find_next_sibling().find_next_sibling().find_previous_sibling()
print(result)

result = soup.find_all("a")

for link in result:
    print(link.get("href"))


