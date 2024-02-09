from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import config
connection_string = config.blobString
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = 'crime'
container_client = blob_service_client.get_container_client(container_name)

import os

# Local directory to save files
local_path = 'C:\Users\Misha\Desktop\GitHub\ML_pipeline\data'

for blob in container_client.list_blobs():
    print("Downloading blob:", blob.name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
    
    # Create a local file path
    download_file_path = os.path.join(local_path, blob.name.replace('/', os.path.sep))
    
    # Create directory structure if it does not exist
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
    
    # Download blob to a local file
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

