import os #https://docs.python.org/3/library/os.html
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
    imageList.clear()
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
    imagePath = r"C:/Users/ehbea/source/repos/REU/MetadataAutomator/Media/DJI_0002.JPG"
    image = Image.open(imagePath)
    exifData = image.getexif()

    for tag_id in exifData:
        tag = TAGS.get(tag_id, tag_id)
        data = exifData.get(tag_id)

        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:16}: {data}")

# Uses GPSPhoto module to target image's Longitutde, Latitude, and Altitude.
def FindGPS():
    gpsData = gpsphoto.getGPSData(imagePath)
    gpsLat = gpsData["Latitude"]
    gpsLong = gpsData["Longitude"]
    gpsAlt = gpsData["Altitude"]
    #print(gpsLat, gpsLong, gpsAlt)
    return gpsLat, gpsLong, gpsAlt

FindExif()
FindGPS()
#Test()

