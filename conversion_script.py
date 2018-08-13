import os, sys

# Path video recordings, will have to be changed
print("starting file conversion")
mainPath = "/home/ubuntu/video_recordings"
flvFolder = os.path.join(mainPath, "flv_folder")
mp4Folder = os.path.join(mainPath, "mp4_folder")

flvExtension = ".flv"
mp4Extension = ".mp4"
allMp4 = "*" + mp4Extension
separator = "-"

print("checking path: " + mainPath)
processed = False
for root, dirs, files in os.walk(mainPath, topdown=True):

    if processed:
        break

    print(files)
    for fileInPath in files:
        print("evaluating file: " + fileInPath)
        filename = os.path.splitext(fileInPath)[0].lower()
        ext = os.path.splitext(fileInPath)[-1].lower()

        print("filename: '" + filename + "'\next: '" + ext + "'")
        if ext == flvExtension:
            print ("converting " + fileInPath + " to mp4")

            #split the string
            filenameComponents = filename.split(separator)
            if len(filenameComponents) < 3:
                print("filename is not the correct format: " + fileInPath + "\n")
                continue

            course = filenameComponents[0]
            lecTitle = separator.join(filenameComponents[1:-1])
            newFilename = course + separator + lecTitle + mp4Extension

            newFilePath = os.path.join(mainPath, newFilename)
            print("new filename: " + newFilename + "\nnew file path: " + newFilePath)

            #have to differentiate files from the same lecture
            if os.path.exists(newFilePath):
                part = 2;
                newFilename = course + separator + lecTitle + separator + "part" + str(part) + mp4Extension
                newFilePath = os.path.join(mainPath, newFilename)
                print("new filename: " + newFilename + "\nnew file path: " + newFilePath)

                while os.path.exists(newFilePath):
                    part = part + 1
                    newFilename = course + separator + lecTitle + separator + "part" + str(part) + mp4Extension
                    newFilePath = os.path.join(mainPath, newFilename)
                    print("new filename: " + newFilename + "\nnew file path: " + newFilePath)

            # convert file to mp4
            flvFilePath = os.path.join(mainPath, fileInPath)
            conversionCommand = "ffmpeg -i " + flvFilePath + " -codec copy " + newFilePath
            print (conversionCommand)
            os.system(conversionCommand)

            # organize files... needs more organization but will use this for now
            moveFlv = "mv " + flvFilePath + " " + flvFolder
            os.system(moveFlv)
            print("moved " + flvFilePath + " to " + flvFolder)
            print("-------------------------------------------------------------\n\n\n\n\n")

    moveMp4 = "mv " + os.path.join(mainPath, allMp4) + " " + mp4Folder
    print(moveMp4)
    os.system(moveMp4)
    processed = True

print("finished file conversion")
