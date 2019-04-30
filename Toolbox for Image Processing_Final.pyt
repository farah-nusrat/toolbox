# File Creator: Farah Nusrat
# Course No: NRS 568
# Student ID: 100602863
# Final Project: Creating "Toolbox" for executing three different process using separate tools
# License Used: MIT License

# Purpose of the toolbox:

# There are separate tools inside this toolbox. The tools are for
# performing Normalized Difference Water Index (NDWI), Extracting values from NDWI to point
# shapefile and stored it, Clipping with desired area of interest from the NDWI layers. For
# calculating the NDWI, Band 3 (B3) and Band 5 (B5) of Landsat images are considered.
# NDWI = (B3 - B5) / (B3 + B5)
# The values vary from -1 to 1. It is mainly done for identifying water.
# The next one is for Extracting raster value using point data. This is helpful
# while you want to extract value from any raster/interpolated layer for desired
# locations.
# The next one is Clip for sub-setting the NDWI layer for desired area of interest.


# Description of the MIT License:

# MIT License
#
# Copyright (c) 2019 farah-nusrat
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import arcpy
from arcpy import env
import os
arcpy.CheckOutExtension("Spatial")


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox for Image Processing"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [NDWI, Extract, Clip]


class NDWI(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "NDWI Creation Tool"
        self.description = "This tool is for calculating NDWI from Landsat 8 images using Band 3 and Band 5."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_directory = arcpy.Parameter(name="input_directory",
                                     displayName="Input Directory",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_directory)
        output = arcpy.Parameter(name="output",
                                 displayName="Output Directory",
                                 datatype="DEFolder",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.env.workspace = parameters[0].valueAsText
        arcpy.env.overwriteOutput = True
        outputDirectory = parameters[1].valueAsText

        outputDirectory = r"J:\NDWI\Data_NDWI\Output"

        if not os.path.exists(outputDirectory):
            os.mkdir(outputDirectory)
        yearsMonths = ["201903", "201901"]
        # Input: Landsat 8 images folder: only use Band 3 and band 5 for
        # calculating NDWI in TIFF format
        # Output: NDWI layer in TIFF format
        for month in yearsMonths:
            arcpy.env.workspace = r"J:\NDWI\Data_NDWI" + "/" + month
            listRasters = arcpy.ListRasters("*", "TIF")
            arcpy.AddMessage(listRasters)

            listRasters_B3 = [x for x in listRasters if "_B3.TIF" in x]
            # arcpy.AddMessage(listRasters_B3)
            listRasters_B5 = [x for x in listRasters if "_B5.TIF" in x]
            if len(listRasters_B5) == 1:
                for i in listRasters_B5:
                    B5 = str(i)
            if len(listRasters_B3) == 1:
                for i in listRasters_B3:
                    B3 = str(i)
            input_string = '(Float("' + B3 + '") - Float("' + B5 + '")) / (Float("' + B3 + '") + Float("' + B5 + '"))'
            arcpy.AddMessage(input_string)

            arcpy.gp.RasterCalculator_sa(input_string, outputDirectory + "/" + str(month) + ".TIF")

            # IF this line do not work, please use the following line.
            #arcpy.gp.RasterCalculator_sa(input_string, outputDirectory + "/" + "a" + str(month) + ".TIF")
            arcpy.AddMessage("Completed: NDWI layers created successfully!!!")

        return
class Extract(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Extracting Tool"
        self.description = "This tool is for extracting NDWI value using point shapefile."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        input_point = arcpy.Parameter(name="input_point",
                                        displayName="Input Point",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_point)
        input_raster = arcpy.Parameter(name="input_raster1",
                                     displayName="Input Directory",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_raster)

        output = arcpy.Parameter(name="output",
                                 displayName="Output Directory",
                                 datatype="DEFolder",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input_point = parameters[0].valueAsText
        arcpy.env.workspace = parameters[1].valueAsText
        outputDirectory = parameters[2].valueAsText

        # # Setting Working Directory and output Directory:

        # User need to change the workspace and output directory. Please select the workspace
        # where you extracted and saved the data.
        arcpy.env.workspace = r"J:\NDWI\Data_Extract"
        arcpy.env.overwriteOutput = True
        outputDirectory = r"J:\NDWI\Data_Extract\output"
        if not os.path.exists(outputDirectory):
            os.mkdir(outputDirectory)

        # Define local variables

        hospitals = "hospitals.shp"
        input_raster = arcpy.ListRasters("*", "TIF")
        arcpy.AddMessage(input_raster)

        # Define projection of input data

        desc = arcpy.Describe(hospitals)
        arcpy.AddMessage(desc.spatialReference.name)

        # Identifying Property and Type of input data

        arcpy.AddMessage(type(hospitals))
        arcpy.AddMessage(property(hospitals))

        # Process: Extract Raster Values to Points

        # Description: A process to extract values from the NDWI layer and stored in a new
        # column of a new shapefile.
        # input = locations of hospital in the study area and NDWI layers for
        # January and March 2019

        # output = shapefile of hospitals' locations in the study area including
        # extracted raster value from NDWI layer. It will add a new column
        # named "RASTERVALU" of the new shapefile by taking values from NDWI layer

        # interpolate_values = "NONE" (No interpolation is applied; the value
        # of the cell center is used only.)

        # add_attributes = "VALUE_ONLY" (Only the value of the input raster is
        # added to the point attributes.)

        # -9999 defines no value.

        for i in input_raster:
            output = "new_" + i
            # checking if the shapefile exists, proceed to extract.
            if arcpy.Exists(hospitals):
                arcpy.AddMessage("Shapefile exists, Proceed to Extract!!!")
            arcpy.gp.ExtractValuesToPoints_sa(hospitals, i, outputDirectory + "/" + output, "NONE", "VALUE_ONLY")
        arcpy.AddMessage("Completed: NDWI values are extracted in new shapefiles!!")

        return

class Clip(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clipping Tool"
        self.description = "This tool is for clipping area of interest from the NDWI layers."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_raster = arcpy.Parameter(name="input_raster",
                                     displayName="Input Directory",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_raster)
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_polygon)
        output = arcpy.Parameter(name="output",
                                 displayName="Output Directory",
                                 datatype="DEFolder",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.env.workspace = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        outputDirectory = parameters[2].valueAsText

        # # Setting Working Directory and output Directory:

        arcpy.env.workspace = r"J:\NDWI\Data_Clip"
        arcpy.env.overwriteOutput = True
        outputDirectory = r"J:\NDWI\Data_Clip\output"

        if not os.path.exists(outputDirectory):
            os.mkdir(outputDirectory)

        # Local variables and parameter description:

        input_raster = arcpy.ListRasters("*", "TIF")
        arcpy.AddMessage(input_raster)
        input_polygon = "dhaka_boundary.shp"

        # output_extent = "218505.675552713 2610223.34303103 254094.983428607 2645940.67"
        # Y Maximum = 2645940.67000000
        # Y Minimum = 2610223.34303103
        # X Maximum = 254094.983428607
        # X Minimum = 218505.675552713

        # NoData_Value = "-3.402823e+038" = The value for pixels to be considered as NoData.

        # clipping_geometry = "ClippingGeometry" (Uses the geometry of the specified feature
        # class to clip the data. The pixel depth of the output may be increased; therefore,
        # you need to make sure that the output format can support the proper pixel depth.)

        # maintain_clipping_extent = NO_MAINTAIN_EXTENT (Maintains the cell alignment
        # as the input raster and adjusts the output extent accordingly.)

        # Checking if the shapefile is available before staring of the process
        if arcpy.Exists(input_polygon):
            arcpy.AddMessage("Shapefile Exists, Proceed to the Clip!")

        # Describe a feature class Type
        desc = arcpy.Describe(input_polygon)
        arcpy.AddMessage(desc.shapeType)
        # input: NDWI layers and shapefile of Area Of Interest (AOI)
        # output: Two clipped TIFF file for January and March for AOI

        # Process: Clip
        for i in input_raster:
            if desc.shapeType == "Polygon":
                arcpy.Clip_management(i, "218505.675552713 2610223.34303103 254094.983428607 2645940.67",
                                      outputDirectory + "/" + "clip_" + str(i), input_polygon,
                                      "-3.402823e+038", "ClippingGeometry", "NO_MAINTAIN_EXTENT")
        arcpy.AddMessage("Clipping Completed!")

        return