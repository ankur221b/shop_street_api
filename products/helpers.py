import base64
import cloudinary
import os

BASE_DIR = ""


def convertBase64ImagetoUrl(data):
    base64ImagetoUrl = data["Image"]
    title = data["Title"]
    productID = data["ProductID"]
    fileName = f"{title}_{productID}"
    img_data = None
    imageurl = None
    with open(fileName, "wb") as fh:
        fh.write(base64.decodebytes(img_data))
    filePath = ""
    imageurl = cloudinary.uploader.upload(filePath)
    return imageurl
