# ==========================================================================================================
#                                            IMPORTED LIBRARIES
# ==========================================================================================================
from tkinter import filedialog
from tkinter import *
import cv2
from Spectral import Tresholder
from PerspectiveCV import CVRuler
from ExcelOp import sheet
import os
# ==========================================================================================================

imagesel = Tk()
orgimg = filedialog.askopenfilename()
imagesel.destroy()

root = Tk()

cvimage = cv2.imread(orgimg)
cvimage = Tresholder.removecolnoise(cvimage)
cvimage = Tresholder.removecolnoise(cvimage)
tkimage = Tresholder.CV2TkConvert(root,cvimage)

Rmin = IntVar()
Rmax = IntVar()
Bmin = IntVar()
Bmax = IntVar()
Gmin = IntVar()
Gmax = IntVar()

RedTreshold = StringVar()
GreenTreshold = StringVar()
BlueTreshold = StringVar()

Folder_Directory = StringVar()
File_Directory = StringVar()

#============================================================================================================

#Screen Initializer. Creates screen.
def screeninit(master,x, y):
    master.title("[Gluefinder]")
    master.resizable(FALSE, FALSE)
    master.geometry(str(x) + "x" + str(y))
    # root.attributes("-fullscreen", 1)
    master.configure(bg='honeydew2')

    # Center the window
    screenWidth = master.winfo_screenwidth()
    screenHeight = master.winfo_screenheight()

    # For left-alling
    left = (screenWidth / 2) - (x / 2)

    # For right-allign
    top = (screenHeight / 2) - (y / 2)

    # For top and bottom
    master.geometry('%dx%d+%d+%d' % (x, y, left, top))

#Main Image generator.
def Image_Spawn(master,x,y):
    global panel
    panel = Label(master=master, image=tkimage)
    panel.place(x=x, y=y)

#WIP TO BE DECIDED
def Logo_Spawn(master, x, y):
    global logo
    cvimage = cv2.imread('Logo.jpg')
    photo = Tresholder.CV2TkConvert(root, cvimage)
    logo = Label(master=master, image=photo)
    logo.place(x=x, y=y)

#RGB Treshold editor and changer.
def RGBTreshScale(master,x,y):
    global Rmin
    global Rmax
    global Bmin
    global Bmax
    global Gmin
    global Gmax

    global RedMin
    global RedMax
    global BlueMin
    global BlueMax
    global GreenMin
    global GreenMax

    canvas = Canvas(master, width=220, height=300, background='GREY')

    RedMin = Scale(master,
                     orient=HORIZONTAL,
                     length=200,
                     from_=0, to=255,
                     showvalue=0,
                     label="Min R Treshhold",
                     activebackground="firebrick",
                     troughcolor="MAROON",
                     bg="grey30",
                     fg="white",
                     highlightbackground="BLACK",
                     sliderlength=10,
                     command=updateval,
                     )

    RedMax = Scale(master,
                   orient=HORIZONTAL,
                   length=200,
                   from_=255, to=0,
                   showvalue=0,
                   label="Max R Treshhold",
                   activebackground="firebrick",
                   troughcolor="MAROON",
                   bg="grey30",
                   fg="white",
                   highlightbackground="BLACK",
                   sliderlength=10,
                   command=updateval,
                   )

    BlueMin = Scale(master,
                   orient=HORIZONTAL,
                   length=200,
                   from_=0, to=255,
                   showvalue=0,
                   label="Min B Treshhold",
                   activebackground="firebrick",
                   troughcolor="SKYBLUE3",
                   bg="grey30",
                   fg="white",
                   highlightbackground="BLACK",
                   sliderlength=10,
                   command=updateval,
                   )

    BlueMax = Scale(master,
                   orient=HORIZONTAL,
                   length=200,
                   from_=255, to=0,
                   showvalue=0,
                   label="Max B Treshhold",
                   activebackground="firebrick",
                   troughcolor="SKYBLUE3",
                   bg="grey30",
                   fg="white",
                   highlightbackground="BLACK",
                   sliderlength=10,
                   command=updateval,
                   )

    GreenMin = Scale(master,
                   orient=HORIZONTAL,
                   length=200,
                   from_=0, to=255,
                   showvalue=0,
                   label="Min G Treshhold",
                   activebackground="firebrick",
                   troughcolor="GREEN",
                   bg="grey30",
                   fg="white",
                   highlightbackground="BLACK",
                   sliderlength=10,
                   command=updateval,
                   )

    GreenMax = Scale(master,
                   orient=HORIZONTAL,
                   length=200,
                   from_=255, to=0,
                   showvalue=0,
                   label="Max G Treshhold",
                   activebackground="firebrick",
                   troughcolor="GREEN",
                   bg="grey30",
                   fg="white",
                   highlightbackground="BLACK",
                   sliderlength=10,
                   command=updateval,
                   )

    RedMin.place(x=x+10, y=y+5)#10 ,5
    RedMax.place(x=x+10, y=y + 55)#10, 55
    BlueMin.place(x=x+10, y=y + 105)#10, 105
    BlueMax.place(x=x+10, y=y + 155)#10, 155
    GreenMin.place(x=x+10, y=y + 205)#10, 205
    GreenMax.place(x=x+10, y=y + 255)#10, 255
    canvas.place(x=x, y=y)#0,0

    BlueMin.set(88)
    GreenMin.set(0)
    BlueMax.set(145)
    GreenMax.set(int(-(((53 - 255) * 255) / 255) + 0))

def RGBDisplay(master,x,y):
    global RedTreshold
    global GreenTreshold
    global BlueTreshold

    RGBTreshDisp = Canvas(width=220, height=80, bg="GRAY")
    RDisp = Label(master,
                  textvariable=RedTreshold,
                  height=1,
                  width=20,
                  bg="MAROON",
                  fg="white",
                  relief=GROOVE
                  )

    GDisp = Label(master,
                  textvariable=GreenTreshold,
                  height=1,
                  width=20,
                  bg="Green",
                  fg="white",
                  relief=GROOVE
                  )

    BDisp = Label(master,
                  textvariable=BlueTreshold,
                  height=1,
                  width=20,
                  bg="DeepSkyBlue3",
                  fg="white",
                  relief=GROOVE
                  )


    RGBTreshDisp.place(x=x, y=y)
    RDisp.place(x=x+20,y=y+10)
    GDisp.place(x=x+20, y=y+30)
    BDisp.place(x=x+20, y=y+50)

def DirDisplay(master,x,y):
    global Folder_Directory

    Folder_Dir =  Label(master,
                  textvariable=Folder_Directory,
                  height=1,
                  width=60,
                  bg="white",
                  fg="black",
                  relief=GROOVE
                  )

    Folder_Dir.place(x=x,y=y)

def FileDisplay(master,x,y):
    global File_Directory

    File_Dir =  Label(master,
                  textvariable=File_Directory,
                  height=1,
                  width=60,
                  bg="white",
                  fg="black",
                  relief=GROOVE
                  )

    File_Dir.place(x=x,y=y)

#============================================================================================================

#Screen upadating function.
def updateval(event):
    global cvimage
    global cvimage_edit

    Rmin = RedMin.get()
    Bmin = BlueMin.get()
    Gmin = GreenMin.get()

    Rmax = int(-(((RedMax.get() - 255) * 255) / 255) + 0)
    Gmax = int(-(((GreenMax.get() - 255) * 255) / 255) + 0)
    Bmax = int(-(((BlueMax.get() - 255) * 255) / 255) + 0)

    '''print("=================",
          "\nRTresh: ", Rmin, "-", Rmax,
          "\nGTresh", Gmin, "-", Gmax,
          "\nBTresh", Bmin, "-", Bmax)'''

    cvimage_edit = Tresholder.RGBTreshold(cvimage, Rmin, Rmax, Gmin, Gmax, Bmin, Bmax)
    tkimage = Tresholder.CV2TkConvert(root,cvimage_edit)
    panel.config(image = tkimage)
    panel.image = tkimage

    #print(cvimage)

    RedTreshold.set(str(Rmin) + " - " + str(Rmax))
    GreenTreshold.set(str(Gmin) + " - " + str(Gmax))
    BlueTreshold.set(str(Bmin) + " - " + str(Bmax))

#Spawn Measure button
def Measure_Spawn(master, x, y):
    measure = Button(master = master,
                     text = "Manual Measure",
                     command = executemeasure,
                     width = 20, height = 1,
                     bg = "Purple",
                     fg = "White")

    measure.place(x = x, y = y)

    autorun = Button(master=master,
                     text="Auto Run",
                     command=execute_automeasure,
                     width=20, height=1,
                     bg="Purple",
                     fg="White")

    autorun.place(x=x, y=y + 30)

#============================================================================================================

#Spawn Image Folder Select Button
def ImgFolderSelect_Spawn(master, x, y):
    folder = Button(master=master,
                    text="Select Folder",
                    command=executefolder,
                    width=10,
                    height=1,
                    bg="Purple",
                    fg="White")

    folder.place(x=x, y=y)

#Spawn Excel File Select Button
def ExcelFileSelect_Spawn(master, x, y):
    folder = Button(master=master,
                    text="Select xlxs File",
                    command=executefile,
                    width=10,
                    height=1,
                    bg="Purple",
                    fg="White")

    folder.place(x=x, y=y)

#============================================================================================================

#Execute measurement of masked image
def executemeasure():
    global cvimage
    cvimage_edited = Tresholder.invertbgimg(cvimage_edit, True)
    cvimage_edited = Tresholder.removebinoise(cvimage_edited, 5)
    cvimage_edited = Tresholder.removespecks(cvimage_edited)
    length, width = CVRuler.computelength(window = True, cvimage = cvimage_edited)
    print(length, ", ", width)

def execute_automeasure():
    if Folder_Directory.get() == '':
        executefolder()

    if File_Directory.get() == '':
        executefile()

    folder_file_count = 1

    global path

    lengthlist = []
    widthlist = []
    pathlist = []

    sheet.addon_template_image(
                      filepath=File_Directory.get(),
                      imgpath=Folder_Directory.get(),
                      data_table_size=4,
                      image_table_size=5,
                      image_start_col=2,
                      start_image=10.0)

    for file in os.listdir(Folder_Directory.get()):
        if file.endswith(".PNG") or file.endswith(".png") or file.endswith(".JPG"):
            path = os.path.join(Folder_Directory.get(), file)

            auto_cvimage = cv2.imread(path)
            auto_cvimage = Tresholder.removecolnoise(auto_cvimage)
            auto_cvimage = Tresholder.removecolnoise(auto_cvimage)

            auto_cvimage_edited = Tresholder.RGBTreshold(auto_cvimage,
                                                  RedMin.get(),
                                                  int(-(((RedMax.get() - 255) * 255) / 255) + 0),
                                                  GreenMin.get(),
                                                  int(-(((GreenMax.get() - 255) * 255) / 255) + 0),
                                                  BlueMin.get(),
                                                  int(-(((BlueMax.get() - 255) * 255) / 255) + 0))

            RedTreshold.set(str(Rmin) + " - " + str(Rmax))
            GreenTreshold.set(str(Gmin) + " - " + str(Gmax))
            BlueTreshold.set(str(Bmin) + " - " + str(Bmax))

            auto_cvimage_edited = Tresholder.invertbgimg(auto_cvimage_edited, True)
            auto_cvimage_edited = Tresholder.removebinoise(auto_cvimage_edited, 5)
            auto_cvimage_edited = Tresholder.removespecks(auto_cvimage_edited)
            length, width = auto_cvimage_edited, width = CVRuler.computelength(window = False, cvimage = auto_cvimage_edited)

            print("Length,Width : " + str(length) + ", " + str(width) + " : " + file + " : " + path)
            lengthlist.append(length)
            widthlist.append(width)
            pathlist.append(path)
            folder_file_count += 1

    sheet.data_addon(path=File_Directory.get(),
                      data_table_size=4,
                      start_image=10.0,
                     length_data=lengthlist,
                     width_data=widthlist,
                     path_data = pathlist,
                     data_count = folder_file_count)

#Selects Folder Area
def executefile():
    fileselect = Tk()
    fileselect.withdraw()
    filepath = filedialog.askopenfilename(title="Select Excel File",
                                          filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
    File_Directory.set(filepath)

#Selects Folder Area
def executefolder():
    folderselect = Tk()
    folderselect.withdraw()
    folderpath = filedialog.askdirectory()
    Folder_Directory.set(folderpath)


#Code Starts here:
#====================================================
screeninit(root,x=1400,y=700)
ImgFolderSelect_Spawn(root, x = 1318, y = 645)
ExcelFileSelect_Spawn(root, x = 1318, y = 590)
Measure_Spawn(root, x = 0, y = 400)
RGBTreshScale(root,x=0, y=0)
RGBDisplay(root, x = 0, y = 300)
DirDisplay(root, 974, 675)
FileDisplay(root, 974, 620)
Image_Spawn(root,250,0)

root.mainloop()