# ==========================================================================================================
#                                            IMPORTED LIBRARIES
# ==========================================================================================================
from tkinter import filedialog
from tkinter import *
import cv2
from Spectral import Tresholder
from PerspectiveCV import CVRuler
# ==========================================================================================================
imagesel = Tk()
orgimg = filedialog.askopenfilename()
imagesel.destroy()

root = Tk()
cvimage = cv2.imread(orgimg)
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

#Screen Initializer. Creates screen.
def screeninit(master,x, y):
    master.title("[SPECTER] - Image Renderer")
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
                  bg="DeepSkyBlue3",
                  fg="white",
                  relief=GROOVE
                  )

    BDisp = Label(master,
                  textvariable=BlueTreshold,
                  height=1,
                  width=20,
                  bg="GREEN",
                  fg="white",
                  relief=GROOVE
                  )


    RGBTreshDisp.place(x=x, y=y)
    RDisp.place(x=x+20,y=y+10)
    GDisp.place(x=x+20, y=y+30)
    BDisp.place(x=x+20, y=y+50)

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

def Measure(master, x, y):
    measure = Button(master = master, text = "Measure", command = execute, width = 10, height = 2, bg = "Purple", fg = "White")
    measure.place(x = x, y = y)

def execute():
    global cvimage
    cvimage_edited = Tresholder.invertbgimg(cvimage_edit, True)
    cvimage_edited = Tresholder.removebinoise(cvimage_edited)
    CVRuler.computelength(cvimage_edited)

screeninit(root,x=1400,y=700)
Measure(root, 0, 600)
RGBTreshScale(root,x=0, y=0)
RGBDisplay(root,0,300)
Image_Spawn(root,600,0)



root.mainloop()