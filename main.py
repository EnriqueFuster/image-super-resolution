# https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066

import os
import cv2
from cv2 import dnn_superres
from functions import tiff_to_png, get_SR_image


input_folder = './input/'
output_folder = './output/'
models_folder = './models/'
png_files = None

model_filename = "EDSR_x3.pb"
model_selected = "edsr" # "edsr", "fsrcnn", "lapsrn", "espcn"
scale_factor = 3

# tiff_to_png(tiff_folder = input_folder, png_folder = input_folder)

if png_files is None:
    png_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

get_SR_image(models_folder, model_filename, model_selected, scale_factor, png_files, input_folder, output_folder)







