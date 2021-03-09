"""
Joshua Sample
Intro to Multimedia Computing Project 2
Dr. Sun
"""

# imports needed, numpy for creating image array and Pillow for image processing
# use command pip install numpy and pip install Pillow if needed
import numpy
from PIL import Image


# filtering method
# takes the image as an array and the filter size (i.e. 3x3)
def median_filter(data, filterSize):
    # set up data fields
    temp = []
    # creates a 2D array filled with 0s based off of the length of the image data
    finalArray = numpy.zeros((len(data), len(data[0])))
    index = filterSize // 2  # index stores the floor of the filter size divided by 2

    # start iterating through the length of the image array
    for i in range(len(data)):
        # iterate through the length of data[0]
        for j in range(len(data[0])):
            # iterate through window size
            for z in range(filterSize):
                # start replacing noise pixels with median neighboring pixels
                if i + z - index < 0 or i + z - index > len(data) - 1:
                    for c in range(filterSize):
                        temp.append(0)
                else:
                    if j + z - index < 0 or j + index > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filterSize):
                            temp.append(data[i + z - index][j + k - index])
            # sort the temporary array in ascending order
            temp.sort()
            # store sorted pixels in final array
            finalArray[i][j] = temp[len(temp) // 2]
            # reset the temporary array
            temp = []
    # once algorithm is finished, return new noise reduced array
    return finalArray


# driver for program
def main():
    # open Lena image
    img = Image.open("Lena_noise.jpg")
    # use numpy to take the image data and put it in an array
    arr = numpy.asarray(img)
    # run the image through the filter, store returned array
    # pass in the image as an array, 3 as the filtering size (3x3)
    removed_noise = median_filter(arr, 3)
    # use Pillow fromarray method to take the array created
    # and transform it back to an image
    img = Image.fromarray(removed_noise)
    # display image
    img.show()


# run main
if __name__ == '__main__':
    main()
