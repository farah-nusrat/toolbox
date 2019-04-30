# Toolbox for Image Processing

Number of Tools: 3
Name of Tools: (1) Creating Normalized Difference Water Index (NDWI), (2) Extract, (3) Clip

Toolbox for Image Processing
ArcGIS Python Toolbox version 10.5 containing three tools used for processing Landsat 8 data.

# These tools can be used for: 

*(1) creating NDWI layer when we have Landsat 8 data as equation is used for specially Landsat 8, 
*(2) then extract desired point data from that NDWI layers and 
*(3) the clipped the desired Area of Interest from NDWI layers.

The tools are largely maintained by Farah Nusrat of University of Rhode Island. All tools are released under the MIT License, and no warranty is implied.

# Data:
Three sets of data are provided to run these tools. All data are for Bangladesh and Dhaka. The hospital data are the locations of hospitals in whole Bangladesh. Landsat data are downloaded from USGS Earth Explorer. 
Name of the data folder: 
(1) Data_NDWI 
(2) Data_Extract 
(3) Data_Clip

# Purpose of the toolbox:

There are separate tools inside this toolbox. The tools are for
performing Normalized Difference Water Index (NDWI), Extracting values from NDWI to point
shapefile and stored it, Clipping with desired area of interest from the NDWI layers. For
calculating the NDWI, Band 3 (B3) and Band 5 (B5) of Landsat images are considered.
NDWI = (B3 - B5) / (B3 + B5)
The values vary from -1 to 1. It is mainly done for identifying water.
The next one is for Extracting raster value using point data. This is helpful
while you want to extract value from any raster/interpolated layer for desired 
locations. 
The next one is Clip for subsetting the NDWI layer for desired area of interest. 

# License: MIT License

Description of the MIT License:
# MIT License
#
# Copyright (c) 2019 farah-nusrat
#
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

