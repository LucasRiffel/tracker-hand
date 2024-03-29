import cv2
import mediapipe as mp
import time
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence = 0.25,
        min_tracking_confidence = 0.2) as hands:
    gesture_detected = False
    while cap.isOpened():
        sucess, image = cap.read()
        if not sucess:
            print("ignoring empty camera frame.")
            continue
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_x, thumb_y = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
                index_x, index_y = int(index_finger_tip.x * image.shape[1]), int(index_finger_tip.y * image.shape[0])

                if thumb_x - 10 < index_x < thumb_x + 10 and thumb_y - 10 < index_y < thumb_y + 0:
                    print("Gesto detectado: Fechar a mão e pressionar o dedo indicador no polegar")
                    time.sleep(1) 
                    cv2.destroyAllWindows()
                    cap.release()
                    exit()

                def calculate_distance(point1, point2):
                    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                thumb_index_distance = calculate_distance(thumb_tip, index_finger_tip)
                index_middle_distance = calculate_distance(index_finger_tip, middle_finger_tip)

                DISTANCE_THRESHOLD = 0.1

                if (thumb_tip.y < ring_finger_tip.y and thumb_tip.y < pinky_tip.y and
                    index_finger_tip.y < ring_finger_tip.y and index_finger_tip.y < pinky_tip.y and
                    middle_finger_tip.y < ring_finger_tip.y and middle_finger_tip.y < pinky_tip.y):
            
                   if (thumb_tip.y < ring_finger_tip.y and thumb_tip.y < pinky_tip.y and
                        index_finger_tip.y < ring_finger_tip.y and index_finger_tip.y < pinky_tip.y and
                        middle_finger_tip.y < ring_finger_tip.y and middle_finger_tip.y < pinky_tip.y and
                        thumb_index_distance > DISTANCE_THRESHOLD and index_middle_distance > DISTANCE_THRESHOLD):
                        print("Gesto detectado: Súarez")
               


        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
