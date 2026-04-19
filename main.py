import cv2
from ultralytics import YOLO
import angles
from pushup import PushUps
from situp import SitUps
import argparse

UP_ANGLE = 145
DOWN_ANGLE = 90


model = YOLO("yolo26m-pose.pt")
cap = cv2.VideoCapture(0)

parser = argparse.ArgumentParser()

parser.add_argument("-m","--mode", type=str, default="pushup")

args = parser.parse_args()
print(f"Running {args.mode}")
if args.mode == "situp" or args.mode == "situps":
    exercise = SitUps()
else:
    exercise = PushUps()

sets = 0
reps = 0

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    results = model(frame, verbose=False, show=False)

    # --- THE FIX IS HERE ---
    # We use a copy of the raw video frame instead of YOLO's plot() function
    annotated_frame = frame.copy()

    if len(results[0].keypoints.xy) > 0:
        
        if exercise.compute(results[0], annotated_frame):
            reps+=1
        
    # Show the final window

    cv2.putText(annotated_frame, f"Reps: {reps}", (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.putText(annotated_frame, f"Sets: {sets}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    cv2.imshow("Dual Arm Pushup Counter", annotated_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        # exercise.resetAll()
        sets=0
        reps=0

    elif key == ord(' '):
        exercise.nextSet()
        sets+=1
        reps = 0

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)