import os #https://docs.python.org/3/library/os.html

filePath = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Media/"
imageList = []
videoList = []

# Reads all the files inside a directory for .jpg files, stores them in a list, and returns the list.
def FilterImages():
    imageList.clear()
    for x in os.listdir(filePath):
        if (x.endswith(".jpg") or x.endswith(".JPG")):
            imageList.append(x)
    #print(imageList)
    return imageList

# Reads all the files inside a directory for .mp4 files, stores them in a list, and returns the list.
def FilterVideos():
    videoList.clear()
    for x in os.listdir(filePath):
           if (x.endswith(".mp4") or x.endswith(".MP4")):
               videoList.append(x)
    #print(videoList)
    return videoList

FilterImages()
FilterVideos()