from __future__ import print_function
from google.cloud import vision
import sys
"""Acknowledgements: this script is based on the example 
    found at https://cloud.google.com/vision/docs/ocr and
    https://cloud.google.com/translate/docs/basic/quickstart
"""

def detect_labels_text(image_uri, target_language='en',  verbose=False):
    """Detect text in the image on Google Cloud Storage then
    translates text into the target language.

    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    target_language: ISO 639-1 language code
    """
    
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.text_detection(image=image)

    print('Text detected:' )

    for text in response.text_annotations:
        print('=' * 30)
        print(text.description)
        vertices = ['(%s,%s)' % (v.x, v.y) for v in text.bounding_poly.vertices]
        print('bounds:', ",".join(vertices))
    
    all_text =  ' '.join(response.text_annotations[0].description.split('\n'))

    translate_text(target_language, all_text )	
    return

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate
    
    print("Translating...")
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Original text: {}".format(result["input"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    print(u"Translation: {}".format(result["translatedText"]))

    return
            
if __name__ == '__main__' : 
    if len(sys.argv) == 2:   
        detect_labels_text(sys.argv[1])
    elif len(sys.argv) == 3 : 
        detect_labels_text(sys.argv[1], sys.argv[2])
    else: 
        print("This takes 2 arguments, the URI of an image and target language")
        print("For example: python detect_labels_text.py gs://bucketname/imagename.jpg fr")
        print("Using default image at 'gs://cloud-vision-codelab/otter_crossing.jpg'")
        print("View at 'https://storage.googleapis.com/cloud-vision-codelab/otter_crossing.jpg'")
        detect_labels_text('gs://cloud-vision-codelab/otter_crossing.jpg', 'af')