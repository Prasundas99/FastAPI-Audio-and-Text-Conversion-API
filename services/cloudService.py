from cloudinary import config, uploader
from config.globals import CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, CLOUDINARY_CLOUD_NAME

def fileUploadService(file):
    config(cloud_name=CLOUDINARY_CLOUD_NAME, api_key=CLOUDINARY_API_KEY, api_secret=CLOUDINARY_API_SECRET)
    
    upload_result = None
    if file:
        upload_result = uploader.upload(file, resource_type = "auto")
        print(upload_result)
        return upload_result['url']
    else:
        return "File upload failed."
    