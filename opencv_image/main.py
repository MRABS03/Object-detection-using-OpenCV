import cv2, time

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
while True:
    check, frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    gray_img_blur = cv2.GaussianBlur(gray_img, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_img_blur

    delta_frame = cv2.absdiff(first_frame, gray_img_blur)
    threshold_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    dil = cv2.dilate(threshold_frame, None, iterations=10)
    cv2.imshow("My video", dil)
    contours, check = cv2.findContours(dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 15000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("My_vid",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
