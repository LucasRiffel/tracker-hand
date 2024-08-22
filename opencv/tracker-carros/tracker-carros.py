import cv2
from cap_from_youtube import cap_from_youtube

youtube_url = "https://www.youtube.com/watch?v=wqctLW0Hb_0"
cap = cap_from_youtube(youtube_url, 'best')

object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mask = object_detector.apply(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 200:
            cv2.drawContours(frame, [cnt], -1,(0, 255, 0),  2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask" , mask)

    key = cv2.waitKey(30)
    if key == 27:  
        break

cap.release()
cv2.destroyAllWindows()
