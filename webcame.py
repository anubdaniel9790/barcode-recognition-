import cv2 as cv 
from pyzbar import pyzbar

def codeDetector(image, data):
    for barcode in data:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv.putText(image, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)
        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    # show the output image
    cv.imshow("Image", image)
cap = cv.VideoCapture(2)
while True:
    ret, frame = cap.read()
    data = pyzbar.decode(frame)
    if data:
        codeDetector(frame, data)
    cv.imshow("img", frame)
    key =cv.waitKey(1)
    if key ==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
# image = cv.imread("barcode-meaning-this-template-stock-260nw-793867024.jpg")
# codeDetector(image, data)
cv.waitKey(0)