#Importing Libraries
from random import randint
from PIL import Image 
import numpy as np

#Opening the image and displaying it
img = Image.open('image.png').convert('L')
img.show()

#Converting image to binary format
thresh=100    #thresh = Threshold
width,height=img.size    
for x in range(width):
    for y in range(height):
        if img.getpixel((x,y)) < thresh:
            img.putpixel((x,y),0)
        else:
            img.putpixel((x,y),1) 
            #put 255 in place of 1 for binary image
                                 
#s1(Share 1), s2(Share 2), de(Decrypted image) declaration
s1=[]
s2=[]
de=[]

#Initializing the above declared lists
for x in range(height):
    s1.append([])
    s2.append([])
    de.append([])
    for y in range(width):
        s1[x].append(0)
        s2[x].append(0)
        de[x].append(0)

#Converting image to numpy array
img=np.asarray(img)        

#Encryption
for x in range(height):
    for y in range(0,width*2,2):#y = 0,2,4,6,..width-1        
        z = randint(0,1)
        #Bypassing second for loop step value.
        if(y%2!=0 and y!=0):
            y=y-1
            #y=0,1,2,3,4,..width-1

        #Removing ListOutOfIndex error 
        if(y>=width):
            break

        #Encryption algorithm
        if(img[x][y]==1):
            if(z==1):
                s1[x].insert(y,1)
                s1[x].insert(y+1,0)
                s2[x].insert(y,1)
                s2[x].insert(y+1,0)
            else:
                s1[x].insert(y,0)
                s1[x].insert(y+1,1)
                s2[x].insert(y,0)
                s2[x].insert(y+1,1)
        else:
            if(z==1):
                s1[x].insert(y,1)
                s1[x].insert(y+1,0)
                s2[x].insert(y,0)
                s2[x].insert(y+1,1)
            else:
                s1[x].insert(y,0)
                s1[x].insert(y+1,1)
                s2[x].insert(y,1)
                s2[x].insert(y+1,0)

#Displaying share1 & share2
s1=np.asarray(s1)
s2=np.asarray(s2)
s1=Image.fromarray(s1)
s2=Image.fromarray(s2)
s1.show()
s2.show()

#Initializing width and height of share
width,height=s1.size
s1=np.asarray(s1).tolist()
s2=np.asarray(s2).tolist()

#Decryption 
for x in range(height):
    for y in range(width):
        de[x].insert(y,s1[x][y] ^ s2[x][y]) 
        #performing XOR(^) operation on 2 shares to obtain the final image

#Converting decrypted array into image 
de=np.asarray(de)
de=Image.fromarray(de)
width,height=de.size
for x in range(width):
    for y in range(height):
        if de.getpixel((x,y)) == 1 :
            de.putpixel((x,y),0)
        else:
            de.putpixel((x,y),255) 
            #put 1 inplace of 255 to obtain binary image

#Final Output
de.show()





