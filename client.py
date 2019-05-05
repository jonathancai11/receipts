import json
from google.cloud import vision, storage
from google.protobuf.json_format import MessageToJson


def create_bucket(bucket_name):
    """ Creates bucket with name bucket_name """
    # Client to Storage API
    storage_client = storage.Client()
    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    client = storage.Client()
    try:
        bucket = client.get_bucket(bucket_name)
    except:
        print("Sorry, either bad credentials or that bucket does not exist!")
    else:
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        print(blob.name)


def annotate_image(bucket_name, file_name, output):
    """ Annotate file_name, outputs to json if output is True """
    # Client to Vision API
    client = vision.ImageAnnotatorClient()

    # Name of file in google bucket (must be anonymously accessible)
    file_name = 'gs://' + bucket_name + '/' + file_name

    # Make request and store response
    response = client.annotate_image({
        'image': {'source': {'image_uri': file_name}},
        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
    })

    # Serialize response
    serialized = MessageToJson(response)

    if (output):
        # Write serialized to json file
        with open(file_name.split('/')[len(file_name.split('/')) - 1] + '-data.json', 'w') as outfile:  
            json.dump(serialized, outfile)

    return serialized


def read_response_json(output_file_name):
    """ Reads the response json file output_file_name """
    with open('out.json') as json_file:  
        data = json.load(json_file)
        # print(data)

        # The first "textAnnotation" contains ALL of the annotations.
        print(data["responses"][0]["textAnnotations"][0]["description"])
        
        # Afterwards, the annotations have the positions/descriptions of each separate annotation.
        print(data["responses"][0]["textAnnotations"][1]["description"])
        print("\n\nNEXT\n\n")


def make_blob_public(bucket_name, blob_name):
    """ Makes blob file public read (read access to anonymouse users) """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    blob.make_public()
    print("Blob {} made public".format(blob_name))

bucket = "johnnys-receipt-bucket"
image = "lmao-blob"
# make_blob_public(bucket, image)
upload_blob("johnnys-receipt-bucket", "test/safeway.jpg", "safeway-blob")
# file = 'gs://johnnys-receipt-bucket/receipt-ocr-original.jpg'
# resp = annotate_image(bucket, image, False)
# print(resp)
