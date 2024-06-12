
import face_recognition
import cv2

img1=face_recognition.load_image_file("Test_image_1.jpeg") 
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=face_recognition.load_image_file("Test_image_3.jpeg") 
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)



faceloc1=face_recognition.face_locations(img1)[0]
encode1=face_recognition.face_encodings(img1)[0]



faceloc2=face_recognition.face_locations(img2)[0]
encode2=face_recognition.face_encodings(img2)[0]


result=face_recognition.compare_faces([encode1],encode2)  
facedis=face_recognition.face_distance([encode1],encode2) 
print(result,facedis)
cv2.putText(img1,f'{result}{round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,250,0),2)

cv2.imshow("image1",img1) 
cv2.imshow("image2",img2)

cv2.waitKey()
cv2.destroyAllWindows()

