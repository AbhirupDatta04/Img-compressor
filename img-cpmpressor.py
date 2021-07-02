import PIL   #Importing Pillow library which can be used for image processing 
from PIL import Image
from tkinter.filedialog import *

fp=askopenfilename()         #Asks our filepath to be used
Image= PIL.Image.open(fp)        
h,w=Image.size
image=Image.resize((h,w),PIL.Image.ANTIALIAS)
savingpath=asksaveasfilename()
image.save(savingpath+"Compressed.jpeg")
 