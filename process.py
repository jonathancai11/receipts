import json
from google.cloud import vision

client = vision.ImageAnnotatorClient()
response = client.annotate_image({
  'image': {'source': {'image_uri': 'gs://johnnys-receipt-bucket/receipt-ocr-original.jpg'}},
  'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
})

print(response)

# with open('out.json') as json_file:  
#     data = json.load(json_file)
#     # print(data)

#     # The first "textAnnotation" contains ALL of the annotations.
#     print(data["responses"][0]["textAnnotations"][0]["description"])
    
#     # Afterwards, the annotations have the positions/descriptions of each separate annotation.
#     print("\n\nNEXT\n\n")
#     print(data["responses"][0]["textAnnotations"][1]["description"])
