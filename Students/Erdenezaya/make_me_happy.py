from PIL import Image
import requests
# This function will store your text in one of the training
# buckets in your machine learning project
def classify(text):
    key = "2d54ab10-14ae-11ea-aee5-d7338c6410f916c4e9b8-698d-4bb8-a7bd-68ce0a06c07d"
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