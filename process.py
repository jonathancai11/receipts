import json
from google.cloud import vision, storage
from google.protobuf.json_format import MessageToJson

import google.auth as auth

# Client to Vision API
client = vision.ImageAnnotatorClient()

# Client to Storage API
storage_client = storage.Client()

bucket_name = "random-bucket-name-lmao"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)


# credentials = auth.credentials.Credentials()
# storage_client = storage.client.Client(token="AIzaSyC6gIZ9kp98JrKTsICuEia4G_P5DAMMVmk")

# projectid = "carbide-booth-239600"

# bucket = storage.bucket.Bucket(storage_client, name="random-bucket-name-lmao")

# bucket.create(project=projectid)

# # Name of file in google bucket (must be anonymously accessible)
# filename = 'gs://johnnys-receipt-bucket/receipt-ocr-original.jpg'

# # Make request and store response
# response = client.annotate_image({
#   'image': {'source': {'image_uri': filename}},
#   'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
# })

# # Serialize response
# serialized = MessageToJson(response)

# # Write serialized to json file
# with open(filename.split('/')[len(filename.split('/')) - 1] + '-data.json', 'w') as outfile:  
#     json.dump(serialized, outfile)


# with open('out.json') as json_file:  
#     data = json.load(json_file)
#     # print(data)

#     # The first "textAnnotation" contains ALL of the annotations.
#     print(data["responses"][0]["textAnnotations"][0]["description"])
    
#     # Afterwards, the annotations have the positions/descriptions of each separate annotation.
#     print("\n\nNEXT\n\n")
#     print(data["responses"][0]["textAnnotations"][1]["description"])
