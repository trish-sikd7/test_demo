import cv2
import os

#path= 'D:\program/final/image/'
#dir = os.path.dirname(path)
#if not os.path.exists(dir):
#	os.makedirs(dir)

face_id = input('enter name ')
# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
    
	if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("ImagesAttendance/" + str(face_id) + ".jpg",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()