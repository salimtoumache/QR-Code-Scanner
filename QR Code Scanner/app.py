from tkinter import *
import cv2
import numpy as np
from PIL import Image,ImageTk
from tkinter import messagebox
app_width = 1083
app_height = 865
win1 = Tk()
width = win1.winfo_screenwidth()
height = win1.winfo_screenheight()
x = (width / 2) - (app_width / 2)
y = (height / 2) - (app_height / 2)
win1.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
win1.title("QR Code Scanner")
win1.resizable(False, False)
filename = PhotoImage(file="bg.png")
background_label = Label(win1, image=filename)
background_label.place(x=0,y=0,relheight=1,relwidth=1)
video_label=Label(win1,bg="#9FEEFF")
video_label.place(x=0,y=235)
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 780)
cap.set(10,90)
while True :
    img=cap.read()[1]
    det = cv2.QRCodeDetector()
    data, pts, st_code = det.detectAndDecode(img)
    if pts is not None:
        if len(data) > 0:
            sc_data='Scanned : '+(str(data))
            messagebox.showinfo(title='info', message=f'\n  | {sc_data} | ')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = ImageTk.PhotoImage(Image.fromarray(img_rgb))
    video_label['image'] = img_rgb
    win1.update()
win1.mainloop()
