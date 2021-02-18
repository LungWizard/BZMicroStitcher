import zipfile
import xml.dom.minidom
from UserInput import UserInput

class KeyenceMetadata():
    GCI = UserInput.GCI
    GCI_Zip  = zipfile.ZipFile(GCI, "r")
    def parseProperties(GCI_Zip, zipinfo):
        with GCI_Zip.open(zipinfo) as GCI_info:
            dom = xml.dom.minidom.parse(GCI_info)
            return {node.tagName : node.firstChild.data 
                    if node.firstChild is not None 
                    else None for node in dom.firstChild.childNodes}
    
    Toplevel_XML = parseProperties(GCI_Zip, "GroupFileProperty/properties.xml")
    ImageJoint_XML = parseProperties(GCI_Zip, "GroupFileProperty/ImageJoint/properties.xml")
    Image_XML = parseProperties(GCI_Zip, "GroupFileProperty/Image/properties.xml")

    #Objective Information
    Lens_XML = parseProperties(GCI_Zip, "GroupFileProperty/Lens/properties.xml")

    #Channel 0 Information
    Channel0_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel0/properties.xml")
    Channel0_CameraSettings_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel0/Shooting/Parameter/properties.xml")
    Channel0_Exposure_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel0/Shooting/Parameter/ExposureTime/properties.xml")
    Channel0_ImageCorrection_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel0/ImageCorrection/properties.xml")
    Channel0_LUT_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel0/ImageCorrection/LookupTable/properties.xml")
    Channel0_Balance_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel0/ImageCorrection/WhiteBalance/properties.xml")
    
    #Channel 1 Information
    Channel1_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel1/properties.xml")
    Channel1_CameraSettings_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel1/Shooting/Parameter/properties.xml")
    Channel1_Exposure_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel1/Shooting/Parameter/ExposureTime/properties.xml")
    Channel1_ImageCorrection_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel1/ImageCorrection/properties.xml")
    Channel1_LUT_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel1/ImageCorrection/LookupTable/properties.xml")
    Channel1_Balance_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel1/ImageCorrection/WhiteBalance/properties.xml")
    
    #Channel 2 Information
    Channel2_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel2/properties.xml")
    Channel2_CameraSettings_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel2/Shooting/Parameter/properties.xml")
    Channel2_Exposure_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel2/Shooting/Parameter/ExposureTime/properties.xml")
    Channel2_ImageCorrection_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel2/ImageCorrection/properties.xml")
    Channel2_LUT_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel2/ImageCorrection/LookupTable/properties.xml")
    Channel2_Balance_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel2/ImageCorrection/WhiteBalance/properties.xml")
    
    #Channel 3 Information
    Channel3_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel3/properties.xml")
    Channel3_CameraSettings_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel3/Shooting/Parameter/properties.xml")
    Channel3_Exposure_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel3/Shooting/Parameter/ExposureTime/properties.xml")
    Channel3_ImageCorrection_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel3/ImageCorrection/properties.xml")
    Channel3_LUT_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel3/ImageCorrection/LookupTable/properties.xml")
    Channel3_Balance_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel3/ImageCorrection/WhiteBalance/properties.xml")
    
    #Channel 4 Information
    Channel4_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel4/properties.xml")
    Channel4_CameraSettings_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel4/Shooting/Parameter/properties.xml")
    Channel4_Exposure_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel4/Shooting/Parameter/ExposureTime/properties.xml")
    Channel4_ImageCorrection_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel4/ImageCorrection/properties.xml")
    Channel4_LUT_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel4/ImageCorrection/LookupTable/properties.xml")
    Channel4_Balance_XML = parseProperties(GCI_Zip, "GroupFileProperty/Channel4/ImageCorrection/WhiteBalance/properties.xml")
    
    
    #Number of tiles in the X and Y direction
    x_num = ImageJoint_XML['Column']
    y_num = ImageJoint_XML['Row']
    
    #Objective Information
    Objective_Mag = Lens_XML['Magnification']
    
    #Channel 1
    Channel0_Status = Channel0_XML['IsShot'] # True = ON, False = OFF
    Ch0_Exposure = int(Channel0_Exposure_XML['Numerator'])/int(Channel0_Exposure_XML['Denominator'])
    FilterCube0 = Channel0_XML['Comment']
    
    #Channel 2
    Channel1_Status = Channel1_XML['IsShot'] # True = ON, False = OFF
    Ch1_Exposure = int(Channel1_Exposure_XML['Numerator'])/int(Channel1_Exposure_XML['Denominator'])
    FilterCube1 = Channel1_XML['Comment']
    
    #Channel 3
    Channel2_Status = Channel2_XML['IsShot'] # True = ON, False = OFF
    Ch2_Exposure = int(Channel2_Exposure_XML['Numerator'])/int(Channel2_Exposure_XML['Denominator'])
    FilterCube2 = Channel2_XML['Comment']
    
    #Channel 4
    Channel3_Status = Channel3_XML['IsShot'] # True = ON, False = OFF
    Ch3_Exposure = int(Channel3_Exposure_XML['Numerator'])/int(Channel3_Exposure_XML['Denominator'])
    FilterCube3 = Channel3_XML['Comment']
    
    '''Channel 5 is reserved for the RGB composite that the microscope generates and is not
    relevant for our use'''