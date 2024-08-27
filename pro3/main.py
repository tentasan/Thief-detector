import cv2
import winsound
from email.message import EmailMessage
import ssl
import smtplib


email_sender ="nithishprabha07@gmail.com"
email_password="iuhl kibe ufqs svaf"
email_receiver="itzsfreaky7@gmail.com"
subject="You going to Succeed"
body="""
        You are on the way

    """
def email():
    em= EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject

    em.set_content(body)
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())        

cam =cv2.VideoCapture(0)


while cam.isOpened():
    ret,frame1 =cam.read()
    ret,frame2 =cam.read()
    diff =cv2.absdiff(frame1,frame2)
    gray =cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur =cv2.GaussianBlur(gray,(5,5),0)
    _,thresh =cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated =cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    for c in contours:
        if cv2.contourArea(c) < 5000 :
            continue
        x,y,w,h =cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0), 2)
        winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
        email()
        
    if cv2.waitKey(10) == ord('N'):
        break
    cv2.imshow('Freaky Cam',frame1)
 
