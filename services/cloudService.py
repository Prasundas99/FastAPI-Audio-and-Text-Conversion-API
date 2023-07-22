from cloudinary import config, uploader

def fileUploadService(file):
    config(cloud_name="dwnurvsv4", api_key="426177162755758", api_secret="vqOVz0gTC2lvTefhwAI2-ETMt-k")
    
    upload_result = None
    if file:
        upload_result = uploader.upload(file, resource_type = "auto")
        print(upload_result)
        return upload_result['url']
    else:
        return "File upload failed."
    