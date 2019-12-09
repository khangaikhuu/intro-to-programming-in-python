from PIL import Image
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "07836970-14aa-11ea-aee5-d7338c6410f978bddb0c-dbb5-4e4f-873e-5bba5c7de2fa"
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