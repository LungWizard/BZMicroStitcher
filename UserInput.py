import openpyxl
from ProcessData import Create_OMETIFF
#USER INPUT
class UserInput():
    MainDirectory = 'C:'
    SlideID = []
    GroupID = []
    XYID = []
    GCI_List = []
    ImgPath_List = []
  #  GCI = []
  #  ImgPath = []
    WSI_List = openpyxl.load_workbook("OME-TIFF.xlsx").worksheets[0]
    #WSI_Worksheet = SlideList.worksheets[0]
    Num_Slides = WSI_List.max_row

    X = 1

    while X < Num_Slides:
        X += 1
        SlideID_Val = WSI_List.cell(row = X, column = 1).value
        SlideID.append(SlideID_Val)
        GroupID_Val = WSI_List.cell(row = X, column = 2).value
        GroupID.append(GroupID_Val)
        XYID_Val = WSI_List.cell(row = X, column = 3).value
        XYID.append(XYID_Val)
        
    for X in range (0, Num_Slides):
        GCI_List.append(MainDirectory + '/' + str(GroupID[X-1]) + '/' +
                        XYID[X-1] + '/' + '*.gci')
        ImgPath_List.append(MainDirectory + '/' + str(GroupID[X-1]) + '/' +
                            XYID[X-1] + '/' + str(SlideID[X-1]) + '.tif')
    
    for X in range (0, Num_Slides):
        Create_OMETIFF(GCI_List[X-1], ImgPath_List[X-1])