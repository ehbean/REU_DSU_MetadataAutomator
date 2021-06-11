import os
import csv
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import exifread
import piexif
from GPSPhoto import gpsphoto

filePath = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Media/"
reportHome = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/"
metaFolder = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Reports/"
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
    global exifDict
    exifDict = {}
    
    try:
        for tag, value in image.getexif().items():
            if tag in TAGS:
                exifDict[TAGS[tag]] = value
    except:
        exifDict[TAGS[tag]] = "-"

    if "ImageDescription" in exifDict:
        global exifImgDes
        exifImgDes = exifDict["ImageDescription"]
    else:
        exifImgDes = "-"
    if "Make" in exifDict:
        global exifMake
        exifMake = exifDict["Make"]
    else:
        exifMake = "-"
    if "Model" in exifDict:
        global exifModel
        exifModel = exifDict["Model"]
    else:
        exifModel = "-"
    if "DateTime" in exifDict:
        global exifDateTime
        exifDateTime = exifDict["DateTime"]
    else:
        exifDateTime = "-"
    if "Software" in exifDict:
        global exifSoftware
        exifSoftware = exifDict["Software"]
    else:
        exifSoftware = "-"

    return exifDict

# Uses GPSPhoto module to target image's Longitutde, Latitude, and Altitude.
# If infomation is missing, or not stored as metadata, it returns as "-"
def FindGPS(targetImage):
    global gpsData
    gpsData = gpsphoto.getGPSData(targetImage)
    try:
        if "Latitude" in gpsData:
            global gpsLat
            gpsLat = gpsData["Latitude"]
        else:
            gpsLat = "-"
        if "Longitude" in gpsData:
            global gpsLong
            gpsLong = gpsData["Longitude"]
        else:
            gpsLong = "-"
        if "Altitude" in gpsData:
            global gpsAlt
            gpsAlt = gpsData["Altitude"]
        else:
            gpsAlt = "-"
        #print(gpsLat, gpsLong, gpsAlt)
        #print(gpsData)

    except:
        print("No GPS Exif Found")
    return gpsData

def Merge():
    global totalDict
    totalDict = {}
    totalDict.update(gpsData)
    totalDict.update(exifDict)
    print(totalDict)
    return totalDict

def GenDir():
    foldersFound = os.listdir(reportHome)

    if "Reports" not in foldersFound:
        os.mkdir(metaFolder)
    else:
        pass

def WriteReport(targetImage, runCheck):
    now = datetime.now()
    formatNow = now.strftime("%d-%m-%Y_%H-%M")
    reportName = "ExifReport" + formatNow + ".csv"
    reportPath = metaFolder+reportName

    headers = ["TargetFile", "ImageDescription", "Make", "Model", "DateTime", "Software", "Latitude", "Longitude", "Altitude", 'XResolution', 'YResolution', 'XPKeywords', 'YCbCrPositioning', 'GPSInfo', 'XPComment', 'ResolutionUnit', 'Orientation', 'ExifOffset', 'ImageLength', 'ImageWidth']

    with open(reportPath, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        if runCheck == 0:
           runCheck = runCheck + 1
           writer.writeheader()
        else:
            pass
        writer.writerow(totalDict)

def GatherImageExif():
    FilterImages()
    GenDir()
    global runCheck
    runCheck = 0

    for i in range(len(imageList)):
        targetImage = str(filePath) + imageList[i]
        print(targetImage)
        FindGPS(targetImage)
        FindExif(targetImage)
        Merge()
        WriteReport(targetImage, runCheck)
        runCheck = runCheck + 1


GatherImageExif()