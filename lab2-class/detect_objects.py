from __future__ import print_function
from google.cloud import vision
import sys
"""Acknowledgements: this script is based on the example 
found at https://cloud.google.com/vision/docs/object-localizer """


def detect_objects(image_uri, verbose=False):
    """Localize objects in the image on Google Cloud Storage

    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    """
    
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)

    print('Labels (and confidence score):')
    print('=' * 30)
    for label in response.label_annotations:
        print(label.description, '(%.2f%%)' % (label.score*100.))
    
    return	
            
if __name__ == '__main__' : 
    if len(sys.argv) ==2:   
        detect_objects(sys.argv[1])
    else: 
        print("This takes 1 argument, the URI of an image")
        print("For example: python detect_labels_text.py gs://bucketname/imagename.jpg")
        print("Using default image at 'gs://cloud-vision-codelab/otter_crossing.jpg'")
        print("View at 'https://storage.googleapis.com/cloud-vision-codelab/otter_crossing.jpg'")
        detect_objects('gs://cloud-vision-codelab/otter_crossing.jpg')