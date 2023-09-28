import sys
from src.compress import compress_image, resize_image

def main(args):

    """
    Esta función es para hacer pruebas de la biblioteca
    ImgCompressCRPython
    """

    image_path = "test.jpg"
    compress_img_path = "test-compressed.jpg"
    resize_img_path = "test-resized.jpg"

    compress_image(image_path, compress_img_path, 50, False)

    resize_image(image_path, resize_img_path, 500, 300, True)

if __name__ == "__main__":    
    main(sys.argv)