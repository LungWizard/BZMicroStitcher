import os
from pathlib import Path
from datetime import datetime
import PIL.Image
import numpy as np
from ome_types import (to_xml)
from ome_types.model.simple_types import UnitsLength, UnitsTime
from ome_types.model import (OME, Image, Pixels, Instrument, InstrumentRef,
                             Microscope, Objective, Channel, TiffData, Plane)
from GCI_Data import KeyenceMetadata
from UserInput import UserInput
import tifffile

''' This line is needed because large images will return an error of a suspected 
"decompression bomb DOS attack" '''

PIL.Image.MAX_IMAGE_PIXELS = 10000000000

GCI = KeyenceMetadata.GCI
ImgPath = UserInput.img
Img = PIL.Image.open(ImgPath)
Objective_Mag = KeyenceMetadata.Lens_XML['Magnification']
Binning_Settings = str(KeyenceMetadata.Channel3_CameraSettings_XML['Binnin'])


'''Converting the image to a numpy array, then defining the image size in 
X and Y in addition to defining the number of channels in the image'''
ImgArray = np.array(Img)
#Number of pixels in the Y direction
Image_Y = int(ImgArray.shape[0])
#Number of pixels in the X direction
Image_X = int(ImgArray.shape[1])
#Number of channels in the image (eg. RGB has 3, 1 for each color)
Image_C = int(ImgArray.shape[2])
    
'''The date and time the GCI file was created in UTC. This will become 
the aquisition date/time'''
ImageTimestamp = os.path.getmtime(GCI)
ImageTimeUTC = datetime.utcfromtimestamp(ImageTimestamp)
    
#Return the original TIFF name so we can name the OME-TIFF
ImgName = Path(ImgPath).stem

#Create a blank OME-XML
ome = OME()

Keyence_Microscope = Microscope(
    manufacturer = 'Keyence Corportation',
    model = 'BZ-X800',
    type = 'Inverted')

#Objective Information
Objective_4X = Objective(
    manufacturer = 'Keyence Corporation', #This will not change
    model = '4X PlanFluor',
    nominal_magnification = 4,
    working_distance = 16.5,
    working_distance_unit = 'mm',
    lens_na = 0.13,
    immersion = 'Air')

Objective_10X = Objective(
    manufacturer = 'Keyence Corporation', #This will not change
    model = '10X PlanFluor',
    nominal_magnification = 10,
    working_distance = 14.5,
    working_distance_unit = 'mm',
    lens_na = 0.45,
    immersion = 'Air')

Objective_20X = Objective(
    manufacturer = 'Keyence Corporation', #This will not change
    model = '20X PlanApo',
    nominal_magnification = 20,
    working_distance = 0.6,
    working_distance_unit = 'mm',
    lens_na = 0.75,
    immersion = 'Air')

Objective_40X = Objective(
    manufacturer = 'Keyence Corporation', #This will not change
    model = '40X PlanApo',
    nominal_magnification = 40,
    working_distance = 0.95,
    working_distance_unit = 'mm',
    lens_na = 0.75,
    immersion = 'Air')

Objective_100X = Objective(
    manufacturer = 'Keyence Corporation', #This will not change
    model = '100X PlanApo',
    nominal_magnification = 100,
    working_distance = 0.13,
    working_distance_unit = 'mm',
    lens_na = 1.45,
    immersion = 'Oil')

Objective_X = Objective()

#Setting correct objective in OME-XML and defining image pixel size
def SelectObjective(Objective_Mag, Objective_4X , Objective_10X, Objective_20X,
                    Objective_40X, Objective_100X, Objective_X):   
    if Objective_Mag == 400:
        ImgObjective = Objective_4X
        PixelSizeX = 1.8907
        PixelSizeY = 1.8907
    elif Objective_Mag == 1000:
        ImgObjective = Objective_10X
        PixelSizeX = 0.7562
        PixelSizeY = 0.7562            
    elif Objective_Mag == 2000:
        ImgObjective = Objective_20X
        PixelSizeX = 0.3784
        PixelSizeY = 0.3784
    elif Objective_Mag == 4000:
        ImgObjective = Objective_40X
        PixelSizeX = 0.1891
        PixelSizeY = 0.1891
    elif Objective_Mag == 10000:
        ImgObjective = Objective_100X
        PixelSizeX = 0.0756
        PixelSizeY = 0.0756
    else:
        ImgObjective = Objective_X
        PixelSizeX = 1
        PixelSizeY = 1
        print("Unable to find the objective used, setting a blank objective and a pixel size of 1 in both the X and Y directions.")
    return ImgObjective, PixelSizeX, PixelSizeY

#Setting the correct binning to adjust the X and Y pixel size
def Binning(Binning_Settings):
    if Binning_Settings == "Off":
        BinSize = 1
    elif Binning_Settings == "TwoByTwo":
        BinSize = 4
    elif Binning_Settings == "ThreeByThree":
        BinSize = 9
    elif Binning_Settings == "FourByFour":
        BinSize = 16
    elif Binning_Settings == "EightByEight":
        BinSize = 64
    elif Binning_Settings == "TwelveByTwelve":
        BinSize = 144
    else:
        BinSize = 1
        print("Unable to determine if binning was used, assuming none.")
    return BinSize

def ColorModeCH4(FilterCube3):
    if FilterCube3 == "Brightfield":
        ColorDef = 'rgb'
    else:
        ColorDef = "minisblack"
    return ColorDef

BinSize = Binning(Binning_Settings)
ImgObjective, PixelSizeX, PixelSizeY = SelectObjective(int(Objective_Mag), Objective_4X,
                                                    Objective_10X, Objective_20X,
                                                    Objective_40X, Objective_100X,
                                                    Objective_X)

Instrument_Config = Instrument(
    microscope = Keyence_Microscope,
    objectives = [ImgObjective])

Channel_Config = Channel(
    illumination_type = 'Transmitted',
    contrast_method = 'Brightfield',
    samples_per_pixel = Image_C)

Plane_Config = Plane(
    the_c = 1,
    the_t = 1,
    the_z = 1,
    delta_t = 0,
    exposure_time = KeyenceMetadata.Ch3_Exposure,
    exposure_time_unit = UnitsTime.SECOND)

Tiff_Config = TiffData(first_c = 1, 
                       first_t = 1, 
                       first_z = 1, 
                       ifd = 0, 
                       plane_count = 1)

Image_Data = Image(
    name = ImgName,
    acquisition_date = ImageTimeUTC,
    pixels = Pixels(
        dimension_order = 'XYCZT',
        size_c = Image_C,
        size_t = 1,
        size_x = Image_X,
        size_y = Image_Y,
        size_z = 1,
        type = 'uint8', #8-bit RGB images for brightfield, 8/14-bit monochrome
        channels = [Channel_Config],
        physical_size_x = PixelSizeX * BinSize,
        physical_size_x_unit = UnitsLength.MICROMETER,
        physical_size_y = PixelSizeY * BinSize,
        physical_size_y_unit = UnitsLength.MICROMETER,
        planes = [Plane_Config],
        tiff_data_blocks = [Tiff_Config]))

ome.instruments.append(Instrument_Config)
ome.images.append(Image_Data)
ome.images[0].instrument_ref = InstrumentRef(Instrument_Config.id)
Final_OMEXML = to_xml(ome)

save_path_file = "OME_XML.xml"
with open(save_path_file, "w") as f:
    f.write(Final_OMEXML)

tifffile.imwrite(ImgName + '.ome.tif', ImgArray,  photometric = 'rgb', 
                 description = Final_OMEXML, metadata = None) 



    