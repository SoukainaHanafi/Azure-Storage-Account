# from dotenv import load_dotenv
# from os.path import join, dirname
# print("hello Sou ")
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    print(connect_str)
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = str('photos')
    container_client = blob_service_client.create_container('photos')
    
    print(container_client)
    local_path = "./data"
    # os.mkdir(local_path)
    local_file_name='photos.txt'
    upload_file_path = os.path.join(local_path, local_file_name)
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    with open(upload_file_path, "rb") as data1:
        blob_client.upload_blob(data1)
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)
    # Quick start code goes here
   
except Exception as ex:
    print('Exception:')
    print(ex)
