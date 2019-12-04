from PIL import Image
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "c4c37dc0-168c-11ea-bcc8-6b735d134c7e05880a7e-254e-4a45-97c5-761dedbc3894"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

input = input("What do you want to tell me? > ")
recognized = classify(input)
label = recognized["class_name"]
if label == "kind_things":
    print ("You're so nice!")
    img = Image.open("happy.png")
    img.show()
else:
    print ("You're so mean!")
    img = Image.open("sad.png")
    img.show()

