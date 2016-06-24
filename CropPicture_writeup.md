[Ting Liu / tingl1]
[Nov.20th, 2015]
15-110 F15 PA9
[Facebook Image Resizing]

*********************************************************************************
1. Interface
---------------------------------------------------------------------------------
- The program takes a image or a series of images in the directory at 'basepath'. The program also takes in a desired cropped width and height value. 
- The program outputs a cropped image (images) with the same value of width and height, a square imag and store them in the directory at 'resultBasePath'.

2. Algorithms
----------------------------------------------------------------------------------
Nested Loops (while or for) would be majorly used in the horizontalCrop and verticalCrop function. For example, horizontalCrop function crops image to an ideal width, so for each row in the 2d list (a single list), the new row in the new_image 2d list is just a subset of the original list, one can simply implement for n<col<len(pixel2dList[row])-n, new_list[row].append(pixel2dList[row][col]). Such nested loops will generate a new_list (a new 2d list represents the new image) with unwanted pixels unselected.

3. Data Structures
----------------------------------------------------------------------------------
2d list will be used in the program. For example a raster image of 512*512 pixel will be representated as [[row0col0,row0col1,...,row0col511],...[row511col0,row511col1,...row11col511]] while the row[i]col[j] value corresponds to the color code of that image, it can be from 0 to 255 for grey scale pictures, 0-255 for 256-color images.

4. Code Structures
----------------------------------------------------------------------------------
- ImagetoPixel2dList(im)
takes an image, convert it into a pixelList, then to a 2d list while each row of pixels are put into a [], then different rows constitute the 2nd layer, the 2d list of pixels are like this [[row0],[row1],...[row(hight-1)]], the value of each pixel depends on the color code.
helper function: None

- faltten2dList(lst)
the opposite, converts a 2d list into a 1d list, which PIL can then convert into an image.
helper function: None

- horizontalCrop(pixel2dList, width,croppedWidth)
crops the sides of the input image to a new width according to the input cropped Width.
helper function: None

- verticalCrop(pixel2dList, height,croppedHeight)
crops the top and bottom of the input image to a new width according to the input cropped Width.
helper function: None

- convertToSquare(pixel2dList, width, height)
delete the unwanted elements in pixel2dlist (trim the top, bottom, left side, right side) and leave with a 2dlist of len(list) = len(list[0]) = desired width/height
helper function: horizontalCrop(pixel2dList, width,croppedWidth), verticalCrop(pixel2dList, height,croppedHeight)

- cropImageToSquare(im)
Takes an image and then crop into a new image using all the functions defined above
helper functions: imageToPixel2dList(im),convertToSquare(pixel2dList, width, height),flatten2dList(squareImage2dList)

- cropImageFromPath(path, croppedPath)
calls cropImageToSquare(im) on all the image located at path.
helper function: cropImageToSquare(im)

  
