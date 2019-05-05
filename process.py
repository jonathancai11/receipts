import json
from google.cloud import vision
from google.protobuf.json_format import MessageToJson

# Client to Vision API
client = vision.ImageAnnotatorClient()

# Name of file in google bucket (must be anonymously accessible)
filename = 'gs://johnnys-receipt-bucket/receipt-ocr-original.jpg'

# Make request and store response
response = client.annotate_image({
  'image': {'source': {'image_uri': filename}},
  'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
})

# Serialize response
serialized = MessageToJson(response)

# Write serialized to json file
with open(filename.split('/')[len(filename.split('/')) - 1] + '-data.json', 'w') as outfile:  
    json.dump(serialized, outfile)


# with open('out.json') as json_file:  
#     data = json.load(json_file)
#     # print(data)

#     # The first "textAnnotation" contains ALL of the annotations.
#     print(data["responses"][0]["textAnnotations"][0]["description"])
    
#     # Afterwards, the annotations have the positions/descriptions of each separate annotation.
#     print("\n\nNEXT\n\n")
#     print(data["responses"][0]["textAnnotations"][1]["description"])
