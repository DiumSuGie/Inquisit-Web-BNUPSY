from PIL import Image 
from numpy import *
from matplotlib import pylab
import os

work_dir = "C:/Desktop/pictures/"
im = array(Image.open(work_dir+'pic.jpg').convert('L')) 

for i in range(0,10,100):
    image = (i/255)*im
    pic1 = Image.fromarray(uint8(image)) .resize((300,300))
pic1.save(work_dir + "grey" + str(i) + ".jpg") 


picturename = os.listdir(work_dir+"pictures\\") 
print("<item pic>")

j = 0
for i in range(0, len(picturename)):
    j = i+1
    print('    '+'/'+str(j)+' = ' + '"' +'pictures/'+ picturename[i] + '"')
print("</item>")
print("\n")
