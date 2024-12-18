# import win32com.client
# from cvzone.HandTrackingModule import HandDetector
# import cv2
# import numpy as np
# import time  # Import time to manage gesture timing
#
# # Initialize PowerPoint application and get the active presentation
#
# def run_ppt(stop_event):
#     Application = win32com.client.Dispatch("PowerPoint.Application")
#     Presentation = Application.ActivePresentation  # Get the currently active presentation
#     print("Currently open presentation:", Presentation.Name)
#
#     # Start slideshow
#     Presentation.SlideShowSettings.Run()
#
#     # Parameters
#     width, height = 900, 720
#     gestureThreshold = 300
#     delay = 1  # Delay in seconds between gestures (e.g., 1 second between gestures)
#
#     # Camera Setup
#     cap = cv2.VideoCapture(0)
#     cap.set(3, width)
#     cap.set(4, height)
#
#     # Hand Detector
#     detectorHand = HandDetector(detectionCon=0.8, maxHands=1)
#
#     # Variables
#     buttonPressed = False
#     lastGestureTime = 0  # Track when the last gesture occurred
#     imgNumber = 0
#     while not stop_event.is_set():
#         # Get image frame
#         success, img = cap.read()
#
#         # Find the hand and its landmarks
#         hands, img = detectorHand.findHands(img)  # with draw
#
#         # Check for hand presence and whether enough time has passed since the last gesture
#         if hands and time.time() - lastGestureTime > delay:  # Check if enough time has passed
#             hand = hands[0]
#             cx, cy = hand["center"]
#             lmList = hand["lmList"]  # List of 21 Landmark points
#             fingers = detectorHand.fingersUp(hand)  # List of which fingers are up
#
#             if cy <= gestureThreshold:  # If hand is at the height of the face
#                 # Gesture 1: Thumbs up (next slide)
#                 if fingers == [0, 0, 0, 0, 1]:
#                     print("Next slide")
#                     Presentation.SlideShowWindow.View.Next()
#                     imgNumber += 1
#                     lastGestureTime = time.time()  # Update the time of the last gesture
#                     buttonPressed = True  # Disable further gestures until time passes
#
#                 # Gesture 2: Whole hand pointing up (previous slide)
#                 elif fingers == [1, 0, 0, 0, 0]:
#                     print("Previous slide")
#                     Presentation.SlideShowWindow.View.Previous()
#                     imgNumber -= 1
#                     lastGestureTime = time.time()  # Update the time of the last gesture
#                     buttonPressed = True  # Disable further gestures until time passes
#
#         if buttonPressed:
#             # Reset button press to allow gesture detection again after some time
#             buttonPressed = False
#
#         # Display the frame
#         cv2.imshow("Hand Gesture Control", img)
#
#         # Press 'q' to quit the application
#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             break
#
#     # Release the webcam and close the window
#     cap.release()
#     cv2.destroyAllWindows()
#
#

import pyautogui
import time
import cv2
from cvzone.HandTrackingModule import HandDetector

# Function to simulate pressing the right arrow key (next slide)
def next_slide():
    pyautogui.press('right')  # Simulate pressing the right arrow key to go to the next slide
    print("Next slide")

# Function to simulate pressing the left arrow key (previous slide)
def previous_slide():
    pyautogui.press('left')  # Simulate pressing the left arrow key to go to the previous slide
    print("Previous slide")

# Function to run the hand gesture control
def run_ppt(stop_event):
    # Parameters
    width, height = 900, 720
    gestureThreshold = 300
    delay = 1  # Delay in seconds between gestures (e.g., 1 second between gestures)

    # Camera Setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Hand Detector
    detectorHand = HandDetector(detectionCon=0.8, maxHands=1)

    # Variables
    buttonPressed = False
    lastGestureTime = 0  # Track when the last gesture occurred

    while not stop_event.is_set():
        # Get image frame
        success, img = cap.read()

        # Find the hand and its landmarks
        hands, img = detectorHand.findHands(img)  # with draw

        # Check for hand presence and whether enough time has passed since the last gesture
        if hands and time.time() - lastGestureTime > delay:  # Check if enough time has passed
            hand = hands[0]
            cx, cy = hand["center"]
            fingers = detectorHand.fingersUp(hand)  # List of which fingers are up

            if cy <= gestureThreshold:  # If hand is at the height of the face
                # Gesture 1: Thumbs up (next slide)
                if fingers == [0, 0, 0, 0, 1]:
                    next_slide()  # Move to the next slide
                    lastGestureTime = time.time()  # Update the time of the last gesture
                    buttonPressed = True  # Disable further gestures until time passes

                # Gesture 2: Whole hand pointing up (previous slide)
                elif fingers == [1, 0, 0, 0, 0]:
                    previous_slide()  # Move to the previous slide
                    lastGestureTime = time.time()  # Update the time of the last gesture
                    buttonPressed = True  # Disable further gestures until time passes

        if buttonPressed:
            # Reset button press to allow gesture detection again after some time
            buttonPressed = False

        # Display the frame
        cv2.imshow("Hand Gesture Control", img)

        # Press 'q' to quit the application
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run the PowerPoint control script

