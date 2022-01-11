import cv2
import numpy as np
def determineObject(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 125, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)                                    
    cv2.drawContours(image=imgray, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3, lineType=cv2.LINE_AA)
    list = []
    for cnt in contours:
        list.append(cv2.contourArea(cnt))
    list.sort(reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        if  cv2.contourArea(cnt)==list[1] :
            cv2.rectangle(img, (x,y), (x+w,y+h), (223,0,41), 2)
            crop_img = img[y:y+h, x:x+w]
    return crop_img
def saveResult(img):
    img = cv2.resize(img, (620,480), interpolation = cv2.INTER_AREA)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 120, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)                                 
    cv2.drawContours(image=imgray, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3, lineType=cv2.LINE_AA)
    list = []
    for cnt in contours:
        list.append(cv2.contourArea(cnt))
    list.sort(reverse=True)
    i=0
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        if  cv2.contourArea(cnt)<=list[2] and cv2.contourArea(cnt) >3000:
            cv2.rectangle(img, (x,y), (x+w,y+h), (223,0,41), 3)
            crop_img = img[y:y+h, x:x+w]
            i+=1
            cv2.imwrite("Resource/Result/number" + str(i)+".jpg",crop_img)
    cv2.imwrite("Resource/Result/LicensePlates.jpg",img)
    return 
img = cv2.imread('Resource/photo1.jpg')
saveResult(determineObject(img))

