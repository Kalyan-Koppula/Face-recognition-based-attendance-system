# Face-recognition-based-attendance-system
Python implementation of simple face recognition based attendance system using face_recognition library.

A real time face recognition of students and employees for their attendance. The attendance record is stored on a google sheet over the cloud and updates regarding the attendance is directly sent to the user via gmail. An android app is also provided for the end user.

**How to execute this project**

Check the detailed step by step guide available at https://www.youtube.com/watch?v=cPm6saam3aY

**Basic project flow**

local db of face and their encodings ------>  face recognition--------> mark attendance in gsheets----->email alerts----->android app

**Methodology of the system:**
•	Capture a video and check each frame for person.
•	If any person is detected , detect the face and crop the frame around his face.
•	Generate facial features of that face and match these with the local database.
•	If the facial features are matched get the name of the person from the local database.
•	Get the date and name of the person detected and update the attendance in the google sheet.  
•	Get the email id of the person from the google sheet and send a mail regarding the attendance status.


**Methodology for face recognition:**

•	Capture a video and process each other frame.
•	Resize the image to 1/4th of the original frame.
•	Convert the image from BGR to RGB.
•	generate a 128 byte array of data for each face detected.
•	Compare this array with the existing arrays in the local database.
•	Calculate Euclidian distance from each face in the local database and get the index of minimum distance.
•	Get the name of the best match index.

