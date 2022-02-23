import cv2
import serial

tracker = cv2.TrackerKCF_create()
video = cv2.VideoCapture(0)

while True:
    k,frame = video.read()
    cv2.imshow("Tracking",frame)
    k = cv2.waitKey(30) & 0xff 
    if k == 27: # Esc (escape) key
        break
bbox = cv2.selectROI(frame, False)

ok = tracker.init(frame, bbox)
cv2.destroyWindow("ROI selector")

while True:
    ok, frame = video.read()
    ok, bbox = tracker.update(frame)
    # bbox[0] = top left corner x - coordinate
    # bbox[1] = top left corner y - coordinate
    # bbox[2] = bottom right corner x - coordinate
    # bbox[3] = bottom right corner y - coordinate
    if ok:
        p1 = (int(bbox[0]),int(bbox[1])) 
        p2 = (int(bbox[0] + bbox[2]), (bbox[1] + bbox[3]))
        centroid = (int(bbox[0]) + int(bbox[2]/2), int(bbox[1]) + int(bbox[3]/2))
        cv2.rectangle(frame, p1, p2, (255,255,255),2,2)
        cv2.circle(frame,centroid,3,(0,0,255),2)

    print(int((centroid[0]-320)/10)+90," ",int((320-centroid[1])/10)+90)
    cv2.imshow("Tracking",frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break
    
