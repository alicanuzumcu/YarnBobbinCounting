import cv2
import ultralytics
import numpy as np

# YOLOv11 model path
model = ultralytics.YOLO('best.pt')

# Video kaynağını aç
cap = cv2.VideoCapture("original.mp4")  

# İlk frame'i okuyarak video çözünürlüğünü alın
ret, frame = cap.read()
if not ret:
    print("Unsuccessful reading!!!.")
    exit()

# Videonun çözünürlüğünü elde et
height, width = frame.shape[:2]

# Opertions to save frames as mp4 file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4 format
out = cv2.VideoWriter('Output.mp4', fourcc, 30.0, (width, height))  

total = set()

while ret:
    ret, frame = cap.read()
    if not ret: 
        print("Frame does not exist.")
        break

    results = model.track(frame, persist=True, show=False)
    cv2.line(frame, (1600, 0), (1600, 3840), (0, 0, 255), 10)

    print("------------------------------------------------------------------------------")
    print("|                                                                            |")
    print("------------------------------------------------------------------------------")
    
    # Boxes Control
    boxes = results[0].boxes
    if boxes is not None and len(boxes) > 0:
        if boxes.id is not None and boxes.conf is not None:
            for i in range(len(boxes.id)):
                x1, y1, x2, y2 = results[0].boxes.xyxy[i]
                ids = int(boxes.id[i])
                conf = float(boxes.conf[i])

                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                if conf < 0.9:
                    continue

                cx = int(x1 / 2 + x2 / 2)
                cy = int(y1 / 2 + y2 / 2)

                center = (cx, cy)

                if cx >= 1575 and cx <= 1625:
                    total.add(ids)
                    cv2.circle(frame, (cx, cy), 50, (255, 0, 0), -1)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 6)

    # Params for text
    text = "Count: " + str(len(total))
    font = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 8
    thickness = 10

    # Black background
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
    cv2.rectangle(frame, (0, 0 ), (1550,400), (0, 0, 0), -1)
    
    # Put text
    cv2.putText(frame, text, (60, 290), font, font_scale, (255, 255, 255), thickness)

    # Save the frames as mp4 file
    out.write(frame)  

    cv2.imshow("Frame", frame)    
    print(f"Set of total {total}")
    print(f"Current count: {len(total)}")
    print("------------------------------------------------------------------------------")
    print("|                                                                            |")
    print("------------------------------------------------------------------------------")

    # type "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release() 
cv2.destroyAllWindows()
