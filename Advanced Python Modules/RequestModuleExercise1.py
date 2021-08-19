import requests
import json

result = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=06a7079dabb988173a4a63647ecd49b2&format=1")

result = json.loads(result.text)


for key,value in result.items():
    if(key == "rates"):
        for key,value in result["rates"].items():
            print(key,value,end="\n")



convertedUnit = input("Please enter domestic monetary unit you want to convert : ")
amount = float(input("Please enter the amount you want to convert : "))

print(f"1 EUR = {result['rates'][convertedUnit]:.2f} {convertedUnit}")
print(f"{amount} EUR = {amount * result['rates'][convertedUnit]:.2f} {convertedUnit}")
