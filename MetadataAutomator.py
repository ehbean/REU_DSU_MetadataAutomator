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
def FindExif():
    image = Image.open(imagePath)
    exifData = image.getexif()
    exifDict = {}
    
    try:
        for tag, value in image.getexif().items():
            if tag in TAGS:
                exifDict[TAGS[tag]] = value
    except:
        exifDict[TAGS[tag]] = "-"
        pass

    exifImgDes = exifDict["ImageDescription"]
    exifMake = exifDict["Make"]
    exifModel = exifDict["Model"]
    exifDateTime = exifDict["DateTime"]
    exifSoftware = exifDict["Software"]
    return exifImgDes, exifMake, exifMake, exifDateTime, exifSoftware
    #print(exifImgDes + "\n" + exifMake + "\n" + exifModel + "\n" + exifDateTime + "\n" + exifSoftware)

# Uses GPSPhoto module to target image's Longitutde, Latitude, and Altitude.
def FindGPS():
    gpsData = gpsphoto.getGPSData(imagePath)
    gpsLat = gpsData["Latitude"]
    gpsLong = gpsData["Longitude"]
    gpsAlt = gpsData["Altitude"]
    #print(gpsLat, gpsLong, gpsAlt)
    return gpsLat, gpsLong, gpsAlt
