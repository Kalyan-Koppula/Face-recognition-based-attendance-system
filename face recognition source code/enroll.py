# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:04:22 2021

@author: kalya
"""

import face_recognition,cv2,pickle
import spreadsheet

photo_folder = 'C:/Desktop/facerecognition project/known faces photos/'
facial_encodings_folder='C:/Desktop/facerecognition project/known face encodings/'

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def encoding_of_enrolled_person(name,image):
	enroll_encoding=[]

	enroll_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(image))[0])
	f=open(facial_encodings_folder+name+'.txt','w+')
	
	with open(facial_encodings_folder+name+'.txt','wb') as fp:
		pickle.dump(enroll_encoding,fp)
	f.close
    
    

def enroll_via_camera(name):
	while True:
		ret,frame=cap.read()
		cv2.imshow('Enrolling new attendee',frame)
		k=cv2.waitKey(1)
		if k & 0xFF==ord('y'):
			cv2.imwrite(photo_folder+name+'.jpg',frame)
			encoding_of_enrolled_person(name,photo_folder+name+'.jpg')
			cv2.destroyAllWindows()
			break
		if k& 0xFF==ord('q'):
			print('quitting')
			cv2.destroyAllWindows()
			break
	cap.release()
	email=input("Enter email address: ")
	spreadsheet.enroll_person_to_sheet(name,email)