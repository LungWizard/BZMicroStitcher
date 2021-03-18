import openpyxl
from ProcessData import Create_OMETIFF
import pyprog
#USER INPUT
class UserInput():
    MainDirectory = 'D:/WSI/03012021'
    SlideID = []
    GroupID = []
    XYID = []
    GCI_List = []
    ImgPath_List = []
    WSI_List = openpyxl.load_workbook("D:/WSI/03012021/03012021.xlsx").worksheets[0]
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
                        str(XYID[X-1]) + '/' + '*.gci')
        ImgPath_List.append(MainDirectory + '/' + str(GroupID[X-1]) + '/' +
                            str(XYID[X-1]) + '/' + str(SlideID[X-1]) + '.tif') 

    ProgBar = pyprog.ProgressBar(" ", " ", total = Num_Slides, 
                              bar_length = 26, 
                              complete_symbol = "=", 
                              not_complete_symbol = " ", 
                              wrap_bar_prefix = " [", wrap_bar_suffix="] ",
                              progress_explain = "", 
                              progress_loc = pyprog.ProgressBar.PROGRESS_LOC_END)
    
    for X in range (0, Num_Slides):
        try:
            Create_OMETIFF(GCI_List[X-1], ImgPath_List[X-1])
            ProgBar.set_stat(X + 1)
            ProgBar.update()
        except:
            pass