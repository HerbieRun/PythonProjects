from PIL import Image
import copy, os

# Note : for cropping pictures #
# Any questions, contact: tingl1@andrew.cmu.edu #


# im is a PIL image
def imageToPixel2dList(im):
    width, height = im.size
    pixelList = list(im.getdata())

    pixel2dList = [[0 for _ in range(width)] for _ in range(height)]

    for row in range(0, height):
        for col in range(0, width):
            i = row * width + col
            pixel2dList[row][col] = pixelList[i]
    return pixel2dList

def flatten2dList(lst):
    return [item for sublist in lst for item in sublist]

def horizontalCrop(pixel2dList, width, croppedWidth):

    cropW_2d = []
    
    # Decide starting position in cropping by user-input #
    auto_choice = input("automatic cropping in width? (starting from left edge) \n y for yes, n for no \n")
    if auto_choice == 'y':
        start_col = 0
    elif auto_choice == 'n':
        start_col = int(input("which pixel in column would you like to start?\n"))
    else:
        print('invalid input, please answer in y or n \n')

   # In case user calculates the run starting column #
    while start_col < 0 or start_col > width - croppedWidth:
        print("wrong input, you must put in a value between 0 and",width-croppedWidth,"\n")
        start_col = int(input("which pixel in column would you like to start?\n"))
                  
    for i in range(len(pixel2dList)):
        cropW_2d.append([pixel2dList[i][col] for col in range(start_col,start_col + croppedWidth)])

    return cropW_2d

def verticalCrop(pixel2dList, height, croppedHeight):
   
    cropH_2d = []
   
    # Decide starting position in cropping by user-input #
    auto_choice = input("automatic cropping in height? (starting from top edge) \n y for yes, n for no \n")
    if auto_choice == 'y':
        start_row = 0 
    elif auto_choice == 'n':
        start_row = int(input("which pixel in row would you like to start?\n"))

    # In case user calculates the run starting row #
    while start_row < 0 or start_row > height - croppedHeight:
        print("wrong input, you must put in a value between 0 and",height-croppedHeight,"\n")
        start_row = int(input("which pixel in row would you like to start?\n"))

    for i in range(start_row, start_row + croppedHeight):
        cropH_2d.append(pixel2dList[i])

    return cropH_2d

def convertToSquare(pixel2dList, width, height):

    # Ask for user input of width and height #
    croppedWidth = int(input("what's the desired pixel size of the output square image?\n"))
    croppedHeight = croppedWidth

    while (croppedWidth not in range(width+1)) or (croppedHeight not in range(height+1)):
        print('invalid input on width or height, please re-input\n')
        croppedWidth = int(input("what's the desired pixel size of the output square image?\n"))
        croppedHeight = croppedWidth
      
    # do the width crop, saved in a new 2dlist called cropW_2d #
    cropW_2d = horizontalCrop(pixel2dList, width, croppedWidth)

    # do the height crop, saved in result_2d #
    # note that input is changed to output of the width crop function # 
    result_2d = verticalCrop(cropW_2d, height, croppedHeight)

    return result_2d

# im is a PIL image
def cropImageToSquare(im):
    width, height = im.size

    # print image's width and height for user reference of input later #
    print('This image has an original width of',width,'and height of',height)
    
    pixel2dList = imageToPixel2dList(im)

    squareImage2dList = convertToSquare(pixel2dList, width, height)
    
    size = len(squareImage2dList)
    
    pixelList = flatten2dList(squareImage2dList)
    newIm = Image.new(im.mode, (size, size))
    
    newIm.putdata(pixelList)
    
    return newIm

def cropImageFromPath(path, croppedPath):
    im = Image.open(path)
    if im.format == "JPEG":
        print("cropping", path,'\n\n')
        # crop image if it is a jpg
        newIm = cropImageToSquare(im)
        newIm.save(croppedPath, "JPEG")
    else:
        print("not jpeg")
        im.save(croppedPath, im.format)

def testCrop(basePath, resultBasePath):
    # Call cropImageFromPath on all the files in the folder 
    # designated by basePath.

    # The following process file one by one, .ds_store excluded #
    image_list = os.listdir(basePath)
    for image in image_list:
        if (image != '.DS_Store'):
            cropImageFromPath(basePath + image,resultBasePath + image)
            print(image,'is done cropping, procesing the next one\n\n\n')
    print('all images in', basePath, 'all done\n')
    return

