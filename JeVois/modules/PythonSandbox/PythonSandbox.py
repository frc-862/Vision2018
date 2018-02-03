import libjevois as jevois
import cv2
import numpy as np
import math
from enum import Enum

class PythonSandbox:
    """
    An OpenCV pipeline generated by GRIP.
    """
    ## Constructor
    def __init__(self):
        jevois.LINFO("PythonTest Constructor")
        # Instantiate a JeVois Timer to measure our processing framerate:
        self.timer = jevois.Timer("sandbox", 100, jevois.LOG_INFO)
        """initializes all values to presets or None if need to be set
        """
        
        self.__resize_image_width = 352.0
        self.__resize_image_height = 288.0
        self.__resize_image_interpolation = cv2.INTER_CUBIC

        self.resize_image_output = None

        self.__blur_input = self.resize_image_output
        self.__blur_type = BlurType.Gaussian_Blur
        self.__blur_radius = 1.8018018018018018

        self.blur_output = None

        self.__hsl_threshold_input = self.blur_output
        
        #Original values
        self.__hsl_threshold_hue = [28.8135593220339, 35.586877323768235]
        self.__hsl_threshold_saturation = [129.1728019883664, 255.0]
        self.__hsl_threshold_luminance = [30, 255]

        self.hsl_threshold_output = None

        self.__cv_dilate_src = self.hsl_threshold_output
        self.__cv_dilate_kernel = None
        self.__cv_dilate_anchor = (-1, -1)
        self.__cv_dilate_iterations = 2.0
        self.__cv_dilate_bordertype = cv2.BORDER_CONSTANT
        self.__cv_dilate_bordervalue = (-1)

        self.cv_dilate_output = None

        self.__cv_erode_src = self.cv_dilate_output
        self.__cv_erode_kernel = None
        self.__cv_erode_anchor = (-1, -1)
        self.__cv_erode_iterations = 6.0
        self.__cv_erode_bordertype = cv2.BORDER_CONSTANT
        self.__cv_erode_bordervalue = (-1)

        self.cv_erode_output = None

        self.__find_contours_input = self.cv_erode_output
        self.__find_contours_external_only = False

        self.find_contours_output = None

        self.__filter_contours_contours = self.find_contours_output
        self.__filter_contours_min_area = 500.0
        self.__filter_contours_min_perimeter = 0.0
        self.__filter_contours_min_width = 0.0
        self.__filter_contours_max_width = 1.0E16
        self.__filter_contours_min_height = 0.0
        self.__filter_contours_max_height = 1.0E21
        self.__filter_contours_solidity = [55.5187429004165, 100]
        self.__filter_contours_max_vertices = 1000000.0
        self.__filter_contours_min_vertices = 0.0
        self.__filter_contours_min_ratio = 0.0
        self.__filter_contours_max_ratio = 1000.0
        
        #Attempt to load above values from file
        try:
            fInit = open("vals.txt", "r")
            if(fInit.mode == "r"):
                valsInit = fInit.read().split('[')[1].split(',')
                self.__hsl_threshold_hue[0] = float(valsInit[0])
                self.__hsl_threshold_hue[1] = float(valsInit[1])
                self.__hsl_threshold_saturation[0] = float(valsInit[2])
                self.__hsl_threshold_saturation[1] = float(valsInit[3])
                self.__hsl_threshold_luminance[0] = float(valsInit[4])
                self.__hsl_threshold_luminance[1] = float(valsInit[5])
                self.__filter_contours_min_area = float(valsInit[6])
                #jevois.sendSerial('setcam absexp' + valsInit[7])
            fInit.close()
        except:
            jevois.LINFO("Error loading parameters from file")

        self.filter_contours_output = None

        self.__convex_hulls_contours = self.filter_contours_output

        self.convex_hulls_output = None
        self.convex_hulls_filled = None
        self.frame = 0
        self.sendFrames = True

        self.__mask_input = self.resize_image_output
        self.__mask_mask = self.hsl_threshold_output

        self.mask_output = None
        jevois.LINFO("END CONSTRUCTOR")
    ## Process function with USB output
    def process(self, inframe, outframe = None):
        """
        Runs the pipeline and sets all outputs to new values.
        """
        self.bgr_input = inframe.getCvBGR()
        
        # Step Resize_Image0:
        #self.__resize_image_input = inframe.getCvRGB()
        # Start measuring image processing time (NOTE: does not account for input conversion time):
        self.timer.start()
        
        
        # Step Blur0:
        self.__blur_input = self.bgr_input
        (self.blur_output) = self.__blur(self.__blur_input, self.__blur_type, self.__blur_radius)

        # Step HSL_Threshold0:
        self.__hsl_threshold_input = self.blur_output
        (self.hsl_threshold_output) = self.__hsl_threshold(self.__hsl_threshold_input, self.__hsl_threshold_hue, self.__hsl_threshold_saturation, self.__hsl_threshold_luminance)

        # Step CV_dilate0:
        self.__cv_dilate_src = self.hsl_threshold_output
        (self.cv_dilate_output) = self.__cv_dilate(self.__cv_dilate_src, self.__cv_dilate_kernel, self.__cv_dilate_anchor, self.__cv_dilate_iterations, self.__cv_dilate_bordertype, self.__cv_dilate_bordervalue)

        # Step CV_erode0:
        self.__cv_erode_src = self.cv_dilate_output
        (self.cv_erode_output) = self.__cv_erode(self.__cv_erode_src, self.__cv_erode_kernel, self.__cv_erode_anchor, self.__cv_erode_iterations, self.__cv_erode_bordertype, self.__cv_erode_bordervalue)

        # Step Find_Contours0:
        self.__find_contours_input = self.cv_erode_output
        (self.find_contours_output) = self.__find_contours(self.__find_contours_input, self.__find_contours_external_only)

        # Step Filter_Contours0:
        self.__filter_contours_contours = self.find_contours_output
        (self.filter_contours_output) = self.__filter_contours(self.__filter_contours_contours, self.__filter_contours_min_area, self.__filter_contours_min_perimeter, self.__filter_contours_min_width, self.__filter_contours_max_width, self.__filter_contours_min_height, self.__filter_contours_max_height, self.__filter_contours_solidity, self.__filter_contours_max_vertices, self.__filter_contours_min_vertices, self.__filter_contours_min_ratio, self.__filter_contours_max_ratio)

        # Step Convex_Hulls0:
        self.__convex_hulls_contours = self.filter_contours_output
        (self.convex_hulls_output) = self.__convex_hulls(self.__convex_hulls_contours)
        
        fps = self.timer.stop()
        numobjects = 0
        for true in self.convex_hulls_output:
            numobjects += 1
        serialMessage = ('Frame:' + str(self.frame) + str(self.frame) + ', Process Time:' + str(fps) + ', Objects:' + str(numobjects) + '=')
        if outframe is not None:
            outimg = self.bgr_input
            
            printedData = False
            textHeight = 22
            i = 0
            for contour in self.convex_hulls_output:
                printedData = True
                x,y,w,h = cv2.boundingRect(contour)
                cv2.circle(outimg, (x + int(w / 2), y + int(h / 2)), 3, (255, 0, 0), 5)
                cv2.rectangle(outimg, (x, y), (x + w, y + h), (0, 255, 0), 3) 
                serialMessage = serialMessage + ('\nObject:' + str(i) + '[x:' + (str(x + int(w / 2)) + ',y:' + str(y + int(h / 2)) + ',w:' + str(w) + ',h:' + str(h) + ']'))
                cv2.putText(outimg, ('x: ' + str(x + int(w / 2)) + ', y: ' + str(y + int(h / 2)) + ', w: ' + str(w) + ', h: ' + str(h)), (3, 288 - textHeight), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                textHeight = textHeight + 15
                i += 1
            if self.sendFrames:
                jevois.sendSerial(serialMessage)
            cv2.drawContours(outimg, self.convex_hulls_output, -1, (0,0,255), 3)
            cv2.putText(outimg, "Glitch CubeVision", (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                        
            # Write frames/s info from our timer into the edge map (NOTE: does not account for output conversion time):
            
            #height, width, channels = self.outimg.shape # if self.outimg is grayscale, change to: height, width = self.outimg.shape
            
            
            cv2.putText(outimg, fps, (3, 288 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

            # Convert our BGR output image to video output format and send to host over USB. If your output image is not
            # BGR, you can use sendCvGRAY(), sendCvRGB(), or sendCvRGBA() as appropriate:
            
            outframe.sendCvBGR(outimg)
        
        else:
            i = 0
            for contour in self.convex_hulls_output:
                x,y,w,h = cv2.boundingRect(contour)
                serialMessage = serialMessage + ('\nObject:' + str(i) + '[x:' + str(x + int(w / 2)) + ',y:' + str(y + int(h / 2)) + ',w:' + str(w) + ',h:' + str(h) + ']')
                i += 1
            if self.sendFrames:
                jevois.sendSerial(serialMessage)
        self.frame += 1

    @staticmethod
    def __blur(src, type, radius):
        """Softens an image using one of several filters.
        Args:
            src: The source mat (numpy.ndarray).
            type: The blurType to perform represented as an int.
            radius: The radius for the blur as a float.
        Returns:
            A numpy.ndarray that has been blurred.
        """
        if(type is BlurType.Box_Blur):
            ksize = int(2 * round(radius) + 1)
            return cv2.blur(src, (ksize, ksize))
        elif(type is BlurType.Gaussian_Blur):
            ksize = int(6 * round(radius) + 1)
            return cv2.GaussianBlur(src, (ksize, ksize), round(radius))
        elif(type is BlurType.Median_Filter):
            ksize = int(2 * round(radius) + 1)
            return cv2.medianBlur(src, ksize)
        else:
            return cv2.bilateralFilter(src, -1, round(radius), round(radius))

    @staticmethod
    def __hsl_threshold(input, hue, sat, lum):
        """Segment an image based on hue, saturation, and luminance ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max luminance.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HLS)
        return cv2.inRange(out, (hue[0], lum[0], sat[0]),  (hue[1], lum[1], sat[1]))

    @staticmethod
    def __cv_dilate(src, kernel, anchor, iterations, border_type, border_value):
        """Expands area of higher value in an image.
        Args:
           src: A numpy.ndarray.
           kernel: The kernel for dilation. A numpy.ndarray.
           iterations: the number of times to dilate.
           border_type: Opencv enum that represents a border type.
           border_value: value to be used for a constant border.
        Returns:
            A numpy.ndarray after dilation.
        """
        return cv2.dilate(src, kernel, anchor, iterations = (int) (iterations +0.5),
                            borderType = border_type, borderValue = border_value)

    @staticmethod
    def __cv_erode(src, kernel, anchor, iterations, border_type, border_value):
        """Expands area of lower value in an image.
        Args:
           src: A numpy.ndarray.
           kernel: The kernel for erosion. A numpy.ndarray.
           iterations: the number of times to erode.
           border_type: Opencv enum that represents a border type.
           border_value: value to be used for a constant border.
        Returns:
            A numpy.ndarray after erosion.
        """
        return cv2.erode(src, kernel, anchor, iterations = (int) (iterations +0.5),
                            borderType = border_type, borderValue = border_value)

    @staticmethod
    def __find_contours(input, external_only):
        """Sets the values of pixels in a binary image to their distance to the nearest black pixel.
        Args:
            input: A numpy.ndarray.
            external_only: A boolean. If true only external contours are found.
        Return:
            A list of numpy.ndarray where each one represents a contour.
        """
        if(external_only):
            mode = cv2.RETR_EXTERNAL
        else:
            mode = cv2.RETR_LIST
        method = cv2.CHAIN_APPROX_SIMPLE
        im2, contours, hierarchy =cv2.findContours(input, mode=mode, method=method)
        return contours

    @staticmethod
    def __filter_contours(input_contours, min_area, min_perimeter, min_width, max_width,
                        min_height, max_height, solidity, max_vertex_count, min_vertex_count,
                        min_ratio, max_ratio):
        """Filters out contours that do not meet certain criteria.
        Args:
            input_contours: Contours as a list of numpy.ndarray.
            min_area: The minimum area of a contour that will be kept.
            min_perimeter: The minimum perimeter of a contour that will be kept.
            min_width: Minimum width of a contour.
            max_width: MaxWidth maximum width.
            min_height: Minimum height.
            max_height: Maximimum height.
            solidity: The minimum and maximum solidity of a contour.
            min_vertex_count: Minimum vertex Count of the contours.
            max_vertex_count: Maximum vertex Count.
            min_ratio: Minimum ratio of width to height.
            max_ratio: Maximum ratio of width to height.
        Returns:
            Contours as a list of numpy.ndarray.
        """
        output = []
        for contour in input_contours:
            x,y,w,h = cv2.boundingRect(contour)
            if (w < min_width or w > max_width):
                continue
            if (h < min_height or h > max_height):
                continue
            area = cv2.contourArea(contour)
            if (area < min_area):
                continue
            if (cv2.arcLength(contour, True) < min_perimeter):
                continue
            hull = cv2.convexHull(contour)
            solid = 100 * area / cv2.contourArea(hull)
            if (solid < solidity[0] or solid > solidity[1]):
                continue
            if (len(contour) < min_vertex_count or len(contour) > max_vertex_count):
                continue
            ratio = (float)(w) / h
            if (ratio < min_ratio or ratio > max_ratio):
                continue
            output.append(contour)
        return output

    @staticmethod
    def __convex_hulls(input_contours):
        """Computes the convex hulls of contours.
        Args:
            input_contours: A list of numpy.ndarray that each represent a contour.
        Returns:
            A list of numpy.ndarray that each represent a contour.
        """
        output = []
        for contour in input_contours:
            output.append(cv2.convexHull(contour))
        return output
        
    # ###################################################################################################
    ## Parse a serial command forwarded to us by the JeVois Engine, return a string
    def parseSerial(self, input):
        jevois.LINFO('parseserial received command [{}]'.format(input))
        command = input.split(' ', 1)[0]
        if command == 'hello':
            return 'Hi!'
        if command == 'getVals':
            return self.getVals()
        if command == 'setHMin':
            return self.setHMin(input)
        if command == 'setHMax':
            return self.setHMax(input)
        if command == 'setSMin':
            return self.setSMin(input)
        if command == 'setSMax':
            return self.setSMax(input)
        if command == 'setLMin':
            return self.setLMin(input)
        if command == 'setLMax':
            return self.setLMax(input)
        if command == 'setMinArea':
            return self.setMinArea(input)
        if command == 'saveParams':
            return self.saveParams(input)
        if command == 'stopSendFrames':
            return self.stopPrintFrames()
        if command == 'sendFrames':
            return self.printFrames()
        return 'ERR: Unknown command'
    #http://jevois.org/qa/index.php?qa=527&qa_1=updating-parameters-in-a-python-module-via-serial
    # ###################################################################################################
    ## Return a string that describes the custom commands we support, for the JeVois help message
    def supportedCommands(self):
        # use \n seperator if your module supports several commands
        return ('hello - print hello using python' + 
        '\ngetVals - return HSL and camera parameters' + 
        '\nsetHMin - set minimum hue' + 
        '\nsetHMax - set maximum hue' + 
        '\nsetSMin - set minimum saturation' + 
        '\nsetSMax - set maximum saturation' + 
        '\nsetLMin - set minimum luminance' + 
        '\nsetLMax - set maximum luminance' + 
        '\nsetMinArea - set minimum area' + 
        '\nsaveParams - save current parameters to file' + 
        '\nsendFrames - resume outputting frames to serial')
    
    def getVals(self):
        return ('Hue. . . . . ' + str(self.__hsl_threshold_hue[0]) + ' - ' + str(self.__hsl_threshold_hue[1]) + 
        '\nSaturation . ' + str(self.__hsl_threshold_saturation[0]) + ' - ' + str(self.__hsl_threshold_saturation[1]) + 
        '\nLuminance. . ' + str(self.__hsl_threshold_luminance[0]) + ' - ' + str(self.__hsl_threshold_luminance[1]) + 
        '\nMin Area . . ' + str(self.__filter_contours_min_area) + 
        '\n[' + str(self.__hsl_threshold_hue[0]) + ',' + str(self.__hsl_threshold_hue[1]) + 
        ',' + str(self.__hsl_threshold_saturation[0]) + ',' + str(self.__hsl_threshold_saturation[1]) + 
        ',' + str(self.__hsl_threshold_luminance[0]) + ',' + str(self.__hsl_threshold_luminance[1]) + 
        ',' + str(self.__filter_contours_min_area) + ', ')
    
    def stopPrintFrames(self):
        self.sendFrames = False
        return 'Not sending frames'
    
    def printFrames(self):
        self.sendFrames = True
        return 'Sending frames'
    
    def setHMin(self, command):
        arg = ''
        arg = command.split(' ')[1]
        if float(arg) < 0:
            return 'ERR: Value too low. Must be at least 0.'
        if float(arg) > self.__hsl_threshold_hue[1]:
            return 'ERR: Value too high. Must be below ' + str(self.__hsl_threshold_hue[1])
        self.__hsl_threshold_hue[0] = float(arg)
        return 'Hue min set to ' + arg
    def setHMax(self, command):
        arg = ''
        arg = command.split(' ')[1]
        if float(arg) > 255:
            return 'ERR: Value too high. Must be below 255'
        if float(arg) < self.__hsl_threshold_hue[0]:
            return 'ERR: Value too low. Must be greater than ' + str(self.__hsl_threshold_hue[0])
        self.__hsl_threshold_hue[1] = float(arg)
        return 'Hue max set to ' + arg
    def setSMin(self, command):
        arg = ''
        arg = command.split(' ')[1]
        if float(arg) < 0:
            return 'ERR: Value too low. Must be at least 0.'
        if float(arg) > self.__hsl_threshold_saturation[1]:
            return 'ERR: Value too high. Must be below ' + str(self.__hsl_threshold_saturation[1])
        self.__hsl_threshold_saturation[0] = float(arg)
        return 'Saturation min set to ' + arg
    def setSMax(self, command):
        arg = ''
        arg = command.split(' ')[1]
        if float(arg) > 255:
            return 'ERR: Value too high. Must be below 255'
        if float(arg) < self.__hsl_threshold_saturation[0]:
            return 'ERR: Value too low. Must be greater than ' + str(self.__hsl_threshold_saturation[0])
        self.__hsl_threshold_saturation[1] = float(arg)
        return 'Saturation max set to ' + arg
    def setLMin(self, command):
        arg = ''
        arg = command.split(' ')[1]
        if float(arg) < 0:
            return 'ERR: Value too low. Must be at least 0.'
        if float(arg) > self.__hsl_threshold_luminance[1]:
            return 'ERR: Value too high. Must be below ' + str(self.__hsl_threshold_luminance[1])
        self.__hsl_threshold_luminance[0] = float(arg)
        return 'Value min set to ' + arg
    def setLMax(self, command):
        arg = ''
        arg = command.split(' ')[1]
        if float(arg) > 255:
            return 'ERR: Value too high. Must be below 255'
        if float(arg) < self.__hsl_threshold_luminance[0]:
            return 'ERR: Value too low. Must be greater than ' + str(self.__hsl_threshold_luminance[0])
        self.__hsl_threshold_luminance[1] = float(arg)
        return 'Value max set to ' + arg
    def setMinArea(self, command):
        arg = ''
        arg = command.split(' ')[1]
        self.__filter_contours_min_area = float(arg)
        return 'Min area set to ' + arg
    def saveParams(self, command):
        exp = ''
        exp = command.split(' ')[1]
        f = open("vals.txt", "w+")
        f.write("h: " + str(self.__hsl_threshold_hue[0]) + "-" + str(self.__hsl_threshold_hue[1]) + "\r\n")
        f.write("s: " + str(self.__hsl_threshold_saturation[0]) + "-" + str(self.__hsl_threshold_saturation[1]) + "\r\n")
        f.write("l: " + str(self.__hsl_threshold_luminance[0]) + "-" + str(self.__hsl_threshold_luminance[1]) + "\r\n")
        f.write("[" + str(self.__hsl_threshold_hue[0]) + "," + str(self.__hsl_threshold_hue[1]) + 
        "," + str(self.__hsl_threshold_saturation[0]) + "," + str(self.__hsl_threshold_saturation[1]) + 
        "," + str(self.__hsl_threshold_luminance[0]) + "," + str(self.__hsl_threshold_luminance[1]) + 
        "," + str(self.__filter_contours_min_area) + "," + exp + ",\r\n")
        f.close()
        return 'Saved parameters'


BlurType = Enum('BlurType', 'Box_Blur Gaussian_Blur Median_Filter Bilateral_Filter')