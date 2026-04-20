# ml2-final-rep-counter

Install the required packages

```
pip install cv2 ultralytics 
```

Run main.py

```
python main.py --mode pushups
```
or
```
python main.py --mode situps
```

# Model (YOLO pose)
17 keypoints:
1. Nose
2. Left Eye
3. Right Eye
4. Left Ear
5. Right Ear
6. Left Shoulder
7. Right Shoulder
8. Left Elbow
9. Right Elbow
10. Left Wrist
11. Right Wrist
12. Left Hip
13. Right Hip
14. Left Knee
15. Right Knee
16. Left Ankle
17. Right Ankle

### Rep Logic
Calculate angles between two keypoints to measure amount of bend.

angle between vector(b->c) and vector(b->a) = atan(c - b) - atan(a - b) 
