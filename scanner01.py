import cv2
import numpy as np

from IPython.display import display, Image

def myfunc(i):
    pass # do nothing

def gamma (x,v):
    c = 1
    x01 = x/255
    y01 = c * (x01**v)
    y = y01*255
    return y

def bgrcolor (x,b,g,r):
    f = np.zeros(x.shape)
    f[:,:,0] = gamma(x[:,:,0],b/10)
    f[:,:,1] = gamma(x[:,:,1],g/10)
    f[:,:,2] = gamma(x[:,:,2],r/10)
    return f

def display_cv_image(image, t, format='.png'):
    decoded_bytes = cv2.imencode(format, image)[1].tobytes()
    display(Image(data=decoded_bytes))
    cv2.imwrite("scanner_"+str(t)+".png",image)

cv2.namedWindow('scanner') # create win with win name

switch3 = '0 : rgbOFF \n1 : rgbON'
cv2.createTrackbar(switch3,'scanner',0,1,myfunc)

cv2.createTrackbar('B','scanner',0,255,myfunc)
cv2.createTrackbar('G','scanner',0,255,myfunc)
cv2.createTrackbar('R','scanner',0,255,myfunc)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)



# OpenCVに用意されている顔認識するためのxmlファイルのパス
cascade_path = "haarcascade_frontalface_alt.xmlまでのパス"

# カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)
    
# 顔に表示される枠の色を指定（白色）
color = (255,255,255)



while(True):

    ret, frame = cap.read()
    if not ret: continue
        
    s3 = cv2.getTrackbarPos(switch3,'scanner')
    b = cv2.getTrackbarPos('B','scanner')
    g = cv2.getTrackbarPos('G','scanner')
    r = cv2.getTrackbarPos('R','scanner')

    # グレイスケール化
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 二値化
    ret1,th1 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    
    # 輪郭抽出
    image, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 面積の大きいもののみ選別
    areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10000:
            epsilon = 0.1*cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,epsilon,True)
            areas.append(approx)

    cv2.drawContours(frame,areas,-1,(0,255,0),3)
    
    
    

    ## do something by using v
    facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10,10))
    
    if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness=2)

    if(s3 == 1):
        framecolor=bgrcolor(frame,b,g,r)
        cv2.imshow('scanner', framecolor)  # show in the win
    else:
        cv2.imshow('scanner', frame)

    k = cv2.waitKey(1)
    if k == ord('s'):
        dst = []

        pts1 = np.float32(areas[0])
        pts2 = np.float32([[600,300],[600,0],[0,0],[0,300]])

        M = cv2.getPerspectiveTransform(pts1,pts2)
        if(s3 == 1):
            dst = cv2.warpPerspective(framecolor,M,(600,300))
        else:
            dst = cv2.warpPerspective(frame,M,(600,300))

        display_cv_image(dst,"card")
        
    if k == ord('f'):
        i = 1;
        for rect in facerect:
            #顔だけ切り出して保存
            x = rect[0]
            y = rect[1]
            width = rect[2]
            height = rect[3]
            if(s3 == 1):
                dst = framecolor[y:y+height, x:x+width]
            else:
                dst = frame[y:y+height, x:x+width]
            display_cv_image(dst,i)
            i += 1
        
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()