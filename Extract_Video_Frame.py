import cv2
import os



'''

pathIn = path to video
pathOut = where output images will be saved
name = name of file
int_desiredLength=3  (e.g. 3 ==> 000, 4 ==> 0000) 
sec = extract video frame every certain second

'''

if not os.path.exists(pathOut):
    os.makedirs(pathOut)


if os.path.exists(pathIn):

    cap = cv2.VideoCapture(pathIn)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = fps
    fps_2_capture = round(sec * fps)

    vid_frame = 0
    vid_frame_saved = 0

    while (cap.isOpened()):

        ret, frame = cap.read()

        #get current frame
        frameId = round(cap.get(1))



        if not ret == True:
            break

        if frameId % fps_2_capture == 0:

            vid_frame = 'frame' + str(switcher['actual_num_frame'])
            #str_0 conv int to str
            fname = name + '_{str_0:0>{str_1}}.jpg'.format(str_0=vid_frame_saved, str_1=int_desiredLength)

            print('Extracting {} to: {}'.format(vid_frame , fname))
            cv2.imwrite(os.path.join(pathOut, fname), frame)

            vid_frame_saved += 1

        vid_frame += 1

else:
    print('path to video file does not exist')

print('Finished Extracting')

cap.release()
cv2.destroyAllWindows()


