import cv2

cap = cv2.VideoCapture(r"C:\Users\lucas\Videos\4K Road traffic video for object detection and tracking - free download now!.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()

    roi = frame[ 0 : 360, 0 : 640]

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 100:
            cv2.drawContours(roi, [cnt], -1,(0, 255, 0),  2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask" , mask)

    key = cv2.waitKey(30)
    if key == 27:  
        break

cap.release()
cv2.destroyAllWindows()
