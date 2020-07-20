from PIL import Image
import cv2 as cv
import os
import numpy as np
import logging

# set the debug file name 
logging.basicConfig(filename='debug.log',filemode='w', level=logging.DEBUG)

def l_print(line):
    """ custom log printer for debugging """
    logging.debug(line)

# initialise image path variable 
DATASET_PATH = "./datasets/RubberWhale/"

def get_image_shape(img):
    """ returns the shape of the image """
    return img.shape

def get_image_size(img):
    """ returns the size of the image """
    return img.size

def get_image_paths(path=DATASET_PATH, image_type='png'):
    """ returns list of image filenames of type image_type in the given location path """
    return [os.path.join(path, item) for item in os.listdir(path) if item.split('.')[-1] == image_type]

def convert_to_grayscale(img):
    """ returns grayscale of the input image """
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
def get_images(path=DATASET_PATH, image_type='png'):
    """ returns list of PIL Image objects using files in the given location path """
    
    # save the current directory and change directory to path
    current_directory = os.getcwd()
    os.chdir(path)

    # list items in directory
    folder_items = os.listdir()

    # build the list of Image objects
    img_list = []
    if len(folder_items) > 0:
        img_list = [Image.open(item) for item in folder_items if item.split('.')[-1] == image_type]
    
    # change back to the previously saved current directory
    os.chdir(current_directory)

    return img_list

def get_laplacian_kernel():
    """ returns a laplacian kernel """
    return np.array([[1/12, 1/6, 1/12], 
                     [1/6, -1, 1/6], 
                     [1/12, 1/6, 1/12]])



