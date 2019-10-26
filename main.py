""" Main python file for our project """
import io
import os
import finder
import instacrawl
from time import sleep

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def logo_find_local(image_path):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    file_name = os.path.abspath(image_path)
    print("File name = {0}".format(file_name))

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    #response = client.label_detection(image=image)
    #labels = response.label_annotations
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    response = client.annotate_image({
        'image' : file_name,
        'features': [{'type': vision.enums.Feature.Type.LOGO_DETECTION}]
        })
    logos = len(response.annoatation)

    print('Logos:')
    for logo in logos:
        print(logo.description)  

def logo_find_uri(uri):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    print("uri: {0}".format(uri))
    image = vision.types.Image()
    image.source.image_uri = uri
    # Performs label detection on the image file
    #response = client.label_detection(image=image)
    #labels = response.label_annotations
    response = client.logo_detection(image=image)
    logos = response.logo_annotations


    print('Logos:')
    for logo in logos:
        if logo.score > 0.8:
            print(logo.description)
        else:
            print("score too low! ommitting image")


def main():
    insta_url = input("Enter the instagram url you would like to analyze:")
    insta_posts = instacrawl.find_posts(insta_url)
    for post in insta_posts:
        logo_find_uri(post.url)
        print("\n")


    image_folder = os.getcwd() + "/images/"
    current_files = []
    new_files = []
    while(True):
        new_files, current_files = finder.image_finder(directory=image_folder, file_list=current_files)
        if new_files:
            for image in new_files:
                print("New image found: {0}".format(image))
                logo_find(image_folder + image)
        sleep(3)


if __name__ == "__main__":
    main()