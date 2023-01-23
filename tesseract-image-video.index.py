import pytesseract
import cv2

# print_pixel_color() is a callback function that is called when the user clicks on the image
def print_pixel_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Pixel color at ({x}, {y}) is {img[y, x]}')

# Initialize the camera
cap = cv2.VideoCapture(1)

# Loop until the user presses the 'q' key
while True:
    ret, img = cap.read()

    if img is None:
        break
    img = img[215:254, 340:400]
    img = cv2.GaussianBlur(img, (5,5), 0)
    # cv2.imshow shows the image in a window
    cv2.imshow('Video', img)
    # cv2.setMouseCallback registers a callback function to be called when a mouse event happens
    cv2.setMouseCallback('Video', print_pixel_color)
    # pytesseract.image_to_string converts the image to a string
    ocr_result = pytesseract.image_to_string(img, config='outputbase digits')
    # print the OCR result if it is a digit
    if ocr_result.isdigit():
        print(f'OCR result is {int(ocr_result)}')
    # wait for 1 millisecond and check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the camera and close all windows
cv2.destroyAllWindows()