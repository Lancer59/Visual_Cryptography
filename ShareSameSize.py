#Importing Libraries
import random
from PIL import Image 
import numpy as np

#Opening the image and displaying it
img = Image.open('image1.png').convert('L')
img.show(title="Original Image")

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

#Modifing the above declared list into 2D based on height
for x in range(height):
    s1.append([])
    s2.append([])
    de.append([])

#Converting image to numpy array
img=np.asarray(img)        

#Encryption
for x in range(height):
    for y in range(width):      
        
        z=random.randrange(0,2)
        #Encryption algorithm
        if(img[x][y]==1):
            s1[x].insert(y,z)
            if(z==1):
                z=0
            s2[x].insert(y,z)
        else:
            s1[x].insert(y,0)
            if(z==1):
                z=0
            s2[x].insert(y,1)

                

#Convertig share1 & share2 into numpy array then into image.
s1=np.asarray(s1)
s2=np.asarray(s2)
s1=Image.fromarray(s1)
s2=Image.fromarray(s2)

#Remove both (1) and (2) code blocks for faster execution of program but remember that the share1 and share2 wont be displayed the correct way.


#(1) Converting the shares from (0,1)image to (0,255)image
#{
width,height=s1.size    
for x in range(width):
    for y in range(height):
        if s1.getpixel((x,y)) == 1:
            s1.putpixel((x,y),255)
        else:
            s1.putpixel((x,y),0) 
        if s2.getpixel((x,y)) == 1:
            s2.putpixel((x,y),255)
        else:
            s2.putpixel((x,y),0) 
#}

#display share1 and share2

s1.show(title="Share 1")
s2.show(title="Share 2")

#(2) Converting the shares from(0,255) to (0,1)image
#{
for x in range(width):
    for y in range(height):
        if s1.getpixel((x,y)) == 255:
            s1.putpixel((x,y),1)
        else:
            s1.putpixel((x,y),0) 
        if s2.getpixel((x,y)) == 255:
            s2.putpixel((x,y),1)
        else:
            s2.putpixel((x,y),0) 
#}


#Initializing width and height of share
width,height=s1.size
#Converting shares from image to normal list
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
de.show(title="Decrypted Image")

print("Enrcyption and Decryption Successful")
