def tiff_to_png(tiff_folder, png_folder):
    from PIL import Image
    import os

    tiff_files = [f for f in os.listdir(tiff_folder) if f.endswith('.tiff')]
    if len(tiff_files) > 0:
        print(f"{len(tiff_files)} TIFF images found in directory {tiff_folder}")

        for img_filename in tiff_files:
            img_tiff = Image.open(os.path.join(tiff_folder, img_filename))
            img_output_filename = img_filename
            img_output_filename = img_output_filename.replace('.tiff', '') + '.png'
            img_tiff.save(os.path.join(png_folder, img_output_filename), format='PNG')


def get_SR_image(models_folder, model_filename, model_selected, scale_factor, png_files, input_folder, output_folder):
    import os
    import cv2
    from cv2 import dnn_superres
    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read the desired model
    sr.readModel(os.path.join(models_folder, model_filename))

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel(model_selected, scale_factor)

    for img_filename in png_files:
        # Read the image
        img_LR = cv2.imread(os.path.join(input_folder, img_filename))

        # Upscale the image
        img_HR = sr.upsample(img_LR)

        # Save the image
        cv2.imwrite(os.path.join(output_folder, img_filename), img_HR)