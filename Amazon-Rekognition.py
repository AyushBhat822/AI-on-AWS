import cv2
cap = cv2.VideoCapture(0)
myphoto = "ayush.jpg"
ret , photo = cap.read()
cv2.imwrite(myphoto , photo)
cap.release()

bucket = "aionaws11"

import boto3

s3 = boto3.resource('s3')

s3.Bucket(bucket).upload_file(myphoto , "file.jpg")

region = 'ap-south-1'
rek = boto3.client('rekognition' , region )

upimage = "file.jpg"

response = rek.detect_labels(
 Image={
          
          'S3Object': {
              'Bucket': bucket,
              'Name': upimage,
            
          }
     
         },
         MaxLabels=10,
         MinConfidence=90
)

for i in range(4):
    print (response['Labels'][i]['Name'])
