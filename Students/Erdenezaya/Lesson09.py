import requests

# This function will store your text in one of the training
# buckets in your machine learning project
def storeTraining(text, label):
    key = "2d54ab10-14ae-11ea-aee5-d7338c6410f916c4e9b8-698d-4bb8-a7bd-68ce0a06c07d"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })

    if response.ok == False:
        # if something went wrong, display the error
        print response.json()


# CHANGE THIS to the text that you want to store
training = "The text that you want to store"

# CHANGE THIS to the training bucket to store it in
label = "Kind_things"

storeTraining(training, label)