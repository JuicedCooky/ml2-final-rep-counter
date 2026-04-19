import angles
import cv2

class SitUps:
    def __init__(self, up_angle=145, down_angle=90, body_straight_angle=160):
        self.up_angle = up_angle
        self.down_angle = down_angle

        self.reps = 0
        self.sets = 0
        self.stage = None

        self.body_straight_angle = body_straight_angle
        # self.all_up = False

    def compute(self, points, annotated_frame):
        result = False
        kpts = points.keypoints.xy[0].cpu().numpy()

        r_sh, r_hip, r_knee = kpts[6], kpts[12], kpts[14]

        body_angle = angles.getAngles(r_sh,r_hip,r_knee)

        if body_angle > 110:
            self.stage = 'down'
        elif body_angle < 55:
            if self.stage == 'down':
                self.stage = 'up'
                # self.reps+=1
                result = True


        # left_color = (255, 0, 0)   # Blue
        right_color = (0, 0, 255)  # Red
        body_color = (0, 255, 0)

        cv2.line(annotated_frame, (int(r_sh[0]), int(r_sh[1])), (int(r_hip[0]), int(r_hip[1])), right_color, 3)
        cv2.line(annotated_frame, (int(r_hip[0]), int(r_hip[1])), (int(r_sh[0]), int(r_sh[1])), right_color, 3)

        # Draw circles on the actual joints (radius=5, thickness=-1 for filled circle)
        # for pt in [l_sh, l_el, l_wr]:
        #     cv2.circle(annotated_frame, (int(pt[0]), int(pt[1])), 5, (0, 255, 255), -1) # Yellow dots
        # for pt in [r_sh, r_el, r_wr]:
        #     cv2.circle(annotated_frame, (int(pt[0]), int(pt[1])), 5, (0, 255, 255), -1)
        for pt in [r_sh, r_hip, r_knee]:
            cv2.circle(annotated_frame, (int(pt[0]), int(pt[1])), 5, (0, 255, 255), -1)


        # cv2.putText(annotated_frame, f"L Reps: {left_reps}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, left_color, 2)
        # cv2.putText(annotated_frame, f"L Angle: {int(left_angle)}", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, left_color, 2)

        # cv2.putText(annotated_frame, f"R Angle: {int(right_angle)}", (400, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, right_color, 2)
        
        cv2.putText(annotated_frame, f"Body Angle: {int(body_angle)}", (30, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, body_color, 2)
            
        return result
    
    def nextSet(self):
        self.sets += 1
        self.reps = 0

    def resetAll(self):
        self.sets=0
        self.reps=0
    # def draw(self, annotated_frame):
        # Draw lines connecting the joints (thickness=3)
        

