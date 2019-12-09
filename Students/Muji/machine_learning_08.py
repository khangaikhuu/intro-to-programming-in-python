import requests
from PIL import Image
# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "59060b50-16ed-11ea-bcc8-6b735d134c7e3df3ec51-a6a1-4848-9222-fab05b94d05a"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

"""
# CHANGE THIS to something you want your machine learning model to classify
demo = classify("The text that you want to test")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))
"""

input =input("What do you want to tell me? >")

recognized=classify(input)

label=recognized["class_name"]
if label=="kind_things":
    print("You're so nice")
    img=Image.open("C:/Users/ASUS/Desktop/MEIN/my_project/happy.png")
    img.show()
else: 
    print("You're so mean")
    img=Image.open("C:/Users/ASUS/Desktop/MEIN/my_project/sad.png")
    img.show()



