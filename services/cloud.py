import cloudinary

def fileUpload(file):
    CLOUDINARY_URL="cloudinary://426177162755758:vqOVz0gTC2lvTefhwAI2-ETMt-k@dwnurvsv4"
    cloudinary.config(cloud_name="dwnurvsv4", api_key="426177162755758", api_secret="vqOVz0gTC2lvTefhwAI2-ETMt-k")

    upload_result = None
    if file:
        upload_result = cloudinary.uploader.upload(file, resource_type = "auto")
        print(upload_result)
        return upload_result['url']
    else:
        return "File upload failed."
    