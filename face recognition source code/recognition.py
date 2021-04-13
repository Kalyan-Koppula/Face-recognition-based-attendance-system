# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:09:16 2021

@author: kalya
"""

import face_recognition,cv2,os,pickle
import numpy as np
import spreadsheet 

known_face_encodings=[]
known_face_names=[]
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

photo_folder = 'C:/Desktop/facerecognition project/known face photos/'
facial_encodings_folder='C:/Desktop/facerecognition project/known face encodings/'

def load_facial_encodings_and_names_from_memory():
	for filename in os.listdir(facial_encodings_folder):
		known_face_names.append(filename[:-4])
		with open (facial_encodings_folder+filename, 'rb') as fp:
			known_face_encodings.append(pickle.load(fp)[0])
            
            
def run_recognition():


     video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)


     face_locations = []
     face_encodings = []
     face_names = []
     process_this_frame = True

     while True:
    # Grab a single frame of video
         ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
         rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
         if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
             face_locations = face_recognition.face_locations(rgb_small_frame)
             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

             face_names = []
             for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                 name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
                 face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                 best_match_index = np.argmin(face_distances)
                 if matches[best_match_index]:
                     name = known_face_names[best_match_index]

                 face_names.append(name)

         process_this_frame = not process_this_frame


    # Display the results
         for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
             top *= 4
             right *= 4
             bottom *= 4
             left *= 4

        # Draw a box around the face
             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
             cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
             font = cv2.FONT_HERSHEY_DUPLEX
             cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
         cv2.imshow('Video', frame)
         flag=-1
         if(len(face_names)!=0):
         	count=0
         	for person in face_names:
         		if(person=='Unknown'):
         			count+=1
         	if(count==len(face_names)):
         		flag=1
         	else:
         		flag=0


    # Hit 'q' on the keyboard to quit!

    
         if cv2.waitKey(1) & 0xFF==ord('q') or flag==0:
         	spreadsheet.write_to_sheet(face_names[0])
         	break
        
            

# Release handle to the webcam
     video_capture.release()
     cv2.destroyAllWindows()
