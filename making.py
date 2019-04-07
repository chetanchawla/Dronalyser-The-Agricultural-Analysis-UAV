import cv2
import numpy as np
norm=cv2.imread('/home/pi/Desktop/nonir.jpg')
#print(norm.shape)
#print(norm[:,:,2].shape)
red=norm[:,:,2]
#print(red.shape)
#print(red)
ir=cv2.imread('/home/pi/Desktop/ir.jpg')
infra=ir[:,:,2]
#print(infra.shape)
#print(infra)
ndvi=np.zeros(red.shape)
ndvicol=np.zeros(norm.shape)
for i in range(0,720):
    for j in range(0,1280):
        a=int(infra[i][j])-int(red[i][j])
        b=int(infra[i][j])+int(red[i][j])
        ndvi[i][j]=a/b
        if ndvi[i][j]>0:
            ndvicol[i][j][1] = ndvi[i][j]
        elif ndvi[i][j]<0:
            #print('in')
            ndvicol[i][j][2]=-ndvi[i][j]
            print(ndvi[i][j])
            #print('less it is')
        
        
#print(ndvicol)
#print(ndvicol.shape)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',ndvicol)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

b:91
ndvi: 1.307692289352417
235
112
a:123
b:91
ndvi: 1.3516483306884766
234
112
a:122
b:90
ndvi: 1.355555534362793
233
111
a:122
b:88
nd
"""
