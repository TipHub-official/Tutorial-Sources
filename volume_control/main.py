import cv2
import mediapipe as mp
import subprocess

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set threshold distance for volume up and down gestures
VOLUME_THRESHOLD = 0.5

# Define AppleScript commands for volume control
VOLUME_UP_COMMAND = 'osascript -e "set volume output volume (output volume of (get volume settings) + 5)"'
VOLUME_DOWN_COMMAND = 'osascript -e "set volume output volume (output volume of (get volume settings) - 5)"'

# Start capturing webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Read and flip the image horizontally
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Process the image with Mediapipe hands to detect hand landmarks
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

            # Calculate Euclidean distance between index finger tip and thumb tip landmarks
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            distance = ((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)**0.5

            # Control system volume based on hand gesture
            if distance > VOLUME_THRESHOLD:
                subprocess.call(VOLUME_UP_COMMAND, shell=True)
                print(distance, VOLUME_THRESHOLD)
            if distance < VOLUME_THRESHOLD:
                subprocess.call(VOLUME_DOWN_COMMAND, shell=True)
                print(distance, VOLUME_THRESHOLD)

    # Display the image with hand landmarks
    cv2.imshow('Hand Gestures Volume Control', frame)

    # Exit program when 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
