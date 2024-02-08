import cv2

img = cv2.imread('solar-system.jpg')
cv2.imshow('output',img)
print(img)

cv2.putText(img,"Sun",(20,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Mercury",(50,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Venus",(80,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Earth",(110,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Mars",(140,320),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Jupiter",(180,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Saturn",(210,380),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Uranus",(240,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))
cv2.putText(img,"Neptune",(270,300),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 0.5,color= (255,255,255))


cv2.imwrite('solar_systemwithname.jpg',img)

cv2.waitKey(0)