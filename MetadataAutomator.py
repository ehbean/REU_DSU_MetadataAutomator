import os
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import exifread
import piexif
from GPSPhoto import gpsphoto

filePath = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Media/"
imagePath = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Media/DJI_0002.JPG"
testImage = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Media/WIN_20210604_08_51_43_Pro.JPG"
imageList = []
videoList = []

# Reads all the files inside a directory for .jpg files, stores them in a list, and returns the list.
def FilterImages():
    #imageList.clear()
    for x in os.listdir(filePath):
        if (x.endswith(".jpg") or x.endswith(".JPG")):
            imageList.append(x)
    return imageList

# Reads all the files inside a directory for .mp4 files, stores them in a list, and returns the list.
def FilterVideos():
    videoList.clear()
    for x in os.listdir(filePath):
           if (x.endswith(".mp4") or x.endswith(".MP4")):
               videoList.append(x)
    return videoList

# Reads all avaiable exif data from target image, that Pillow is able to extract.
# If infomation is missing, or not stored as metadata, it returns as "-"
def FindExif(targetImage):
    image = Image.open(targetImage)
    exifData = image.getexif()
    exifDict = {}
    
    try:
        for tag, value in image.getexif().items():
            if tag in TAGS:
                exifDict[TAGS[tag]] = value
    except:
        exifDict[TAGS[tag]] = "-"

    if "ImageDescription" in exifDict:
        exifImgDes = exifDict["ImageDescription"]
    else:
        exifImgDes = "-"
    if "Make" in exifDict:
        exifMake = exifDict["Make"]
    else:
        exifMake = "-"
    if "Model" in exifDict:
        exifModel = exifDict["Model"]
    else:
        exifModel = "-"
    if "DateTime" in exifDict:
        exifDateTime = exifDict["DateTime"]
    else:
        exifDateTime = "-"
    if "Software" in exifDict:
        exifSoftware = exifDict["Software"]
    else:
        exifSoftware = "-"

    #print(exifImgDes + "\n" + exifMake + "\n" + exifModel + "\n" + exifDateTime + "\n" + exifSoftware)
    return exifImgDes, exifMake, exifMake, exifDateTime, exifSoftware


# Uses GPSPhoto module to target image's Longitutde, Latitude, and Altitude.
# If infomation is missing, or not stored as metadata, it returns as "-"
def FindGPS(targetImage):
    gpsData = gpsphoto.getGPSData(targetImage)
    try:
        if "Latitude" in gpsData:
            gpsLat = gpsData["Latitude"]
        else:
            gpsLat = "-"
        if "Longitude" in gpsData:
            gpsLong = gpsData["Longitude"]
        else:
            gpsLong = "-"
        if "Altitude" in gpsData:
            gpsAlt = gpsData["Altitude"]
        else:
            gpsAlt = "-"
        #print(gpsLat, gpsLong, gpsAlt)
        return gpsLat, gpsLong, gpsAlt
    except:
        print("No GPS Exif Found")

def GatherImageExif():
    FilterImages()

    for i in range(len(imageList)):
        targetImage = str(filePath) + imageList[i]
        print(targetImage)
        FindGPS(targetImage)
        FindExif(targetImage)


GatherImageExif()