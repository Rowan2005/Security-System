import cv2
import dropbox
import time
import random

start_time = time.time()
def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    accesstoken = "iD8Xi0tCt4AAAAAAAAAAGjXrE8RBpvuZexCJiFLp21hrsdwxfoQRWxN0chQ6fCyX"
    file = img_name
    file_from = file
    file_to = "/secure/" + (img_name)
    dbx = dropbox.Dropbox(accesstoken)
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 120):
            name = takeSnapshot()
            upload_files(name)

main()