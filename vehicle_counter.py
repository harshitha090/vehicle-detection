from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

vehicle_classes = ["car","motorcycle","bus","truck"]

 True:

    ret, frame = cap.read()

    results = model(frame);;;;;;

    car_count = 0
    bike_count = 0
    bus_count = 0
    truck_count = 0

    for r in results:
        boxes = r.boxes
        for box in boxes:

            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "car":
                car_count += 1
            elif label == "motorcycle":
                bike_count += 1
            elif label == "bus":
                bus_count += 1
            elif label == "truck":
                truck_count += 1

    annotated = results[0].plot()

    cv2.putText(annotated, f"Cars: {car_count}", (20,40), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(annotated, f"Bikes: {bike_count}", (20,80), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(annotated, f"Buses: {bus_count}", (20,120), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(annotated, f"Trucks: {truck_count}", (20,160), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Vehicle Counter", annotated)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
