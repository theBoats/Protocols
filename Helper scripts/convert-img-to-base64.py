import base64
import os
import sys


def main():
    '''
    Takes a folder containing images as a command argument (full path) and encodes them in base64. The result is printed to a text file output.txt in the 
    same folder containing the images. Each image begins with the string 'a new image' that can be found with Ctrl+F in the output.

    This script was designed to encode images within markdown documents for circulation offline.
    '''

    def image_to_base64(file_path):
        with open(file_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        return base64_string

    images= os.listdir(sys.argv[1])

    file = open(sys.argv[1]+"/"+"output.txt", "a")

    for image in images:
        file.write("A new image:\n")    
        file.write(image_to_base64(sys.argv[1]+"/"+image))
        file.write("\n")

    file.close()


if __name__ == "__main__":
    main()