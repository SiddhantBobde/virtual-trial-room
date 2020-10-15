import os
import cv2


def convert(original, GT,saveto):
    img = cv2.imread(r"E:\\EDI\\virtual-trial-room\\Shirt_MRCNN\\samples\\EDI\\dataset\\GT\\" + GT, cv2.IMREAD_COLOR)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, gta = cv2.threshold(img2, 250, 255, cv2.THRESH_BINARY)

    x_end, y_end = 0, 0
    x, y = 0, 0
    flag = 0
    for i in range(len(gta)):
        for j in range(len(gta[0])):
            if (gta[i][j] != 255):
                x = i
                y = j
                flag = 1
                break
        if (flag):
            break
    flag = 0
    for i in range(len(gta) - 1, 0, -1):
        for j in range(len(gta[0]) - 1, 0, -1):
            print(gta[i][j])
            if (gta[i][j] != 255):
                x_end = i
                y_end = j
                flag = 1
                break
        if (flag):
            break

    cv2.imwrite("Modified_GT\\modify_GT"+original, img[x:x_end - 1, y:y_end - 1])

    gt = cv2.imread(r'Modified_GT\\modify_GT'+original, cv2.IMREAD_COLOR)
    original1 = cv2.imread(r"E:\\EDI\\virtual-trial-room\\Shirt_MRCNN\\samples\\EDI\\dataset\\val\\"+original, cv2.IMREAD_COLOR)

    gta = cv2.cvtColor(gt, cv2.COLOR_RGB2GRAY)
    original1 = cv2.cvtColor(original1, cv2.COLOR_BGR2BGRA)
    # thresh=cv2.THRESH_MASK()
    gta = cv2.resize(gta, (600, 600))
    original1 = cv2.resize(original1, (600, 600))
    ret, gta = cv2.threshold(gta, 120, 255, cv2.THRESH_BINARY)

    # #print(gta)
    for i in range(len(gta)):
        for j in range(len(gta[0])):
            if (gta[i][j] != 0):
                original1[i][j][3] = 0

    # cv2.imshow('Binary Threshold', gta)

    cv2.imwrite(saveto+"\\"+"trans_"+original[:4]+".png", original1)


OriginList = [i for i in os.listdir("E:\\EDI\\virtual-trial-room\\Shirt_MRCNN\\samples\\EDI\\dataset\\val") if (i.endswith(".jpg")) and i not in ["HS_13.jpg","HS_Thirteight.jpg","FS_forty.jpg","FS28.jpg"]]
GTList = [i for i in os.listdir("E:\\EDI\\virtual-trial-room\\Shirt_MRCNN\\samples\\EDI\\dataset\\GT") if i.endswith(".jpg") and i not in ["FS28.jpg"]]

OriginList.sort()
GTList.sort()
#
print(OriginList)
print(GTList)
# GT = "FS15.jpg"
saveto = "Transperent_images"
# origin = "original.jpg"
# convert(origin,GT,saveto)

for i in range(len(OriginList)):
    convert(OriginList[i],GTList[i],saveto)
