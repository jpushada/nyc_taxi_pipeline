import os
import requests
from bs4 import BeautifulSoup
from google.cloud import storage
from azure.storage.blob import BlobServiceClient
from config import (
    SOURCE_DATA_URL, GCS_BUCKET_NAME, GOOGLE_APP_CREDENTIALS,
    AZURE_STORAGE_ACCOUNT, AZURE_CONTAINER_NAME, AZURE_SAS_TOKEN, CHUNK_SIZE
)

def get_file_list():
    """Scrape the source URL to get a list of available files."""
    print(f"Scraping {SOURCE_DATA_URL} for available files...")
    response = requests.get(SOURCE_DATA_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    files = [link.get('href') for link in soup.find_all('a') if link.get('href').endswith('.parquet')]
    print(f"Found {len(files)} files: {files}")
    return files

def upload_to_gcs(file_url):
    """Stream the file from URL to Google Cloud Storage."""
    print(f"Uploading {file_url} to GCS...")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APP_CREDENTIALS

    storage_client = storage.Client()
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob_name = file_url.split('/')[-1]
    blob = bucket.blob(blob_name)

    with requests.get(file_url, stream=True) as response:
        response.raise_for_status()
        blob.upload_from_file(response.raw)

    print(f"Uploaded {blob_name} to GCS: gs://{GCS_BUCKET_NAME}/{blob_name}")

def upload_to_azure(file_url):
    """Stream the file from URL to Azure Blob Storage."""
    print(f"Uploading {file_url} to Azure Blob Storage...")
    blob_service_client = BlobServiceClient(
        account_url=f"https://{AZURE_STORAGE_ACCOUNT}.blob.core.windows.net",
        credential=AZURE_SAS_TOKEN
    )
    blob_name = file_url.split('/')[-1]
    blob_client = blob_service_client.get_blob_client(
        container=AZURE_CONTAINER_NAME, blob=blob_name
    )

    with requests.get(file_url, stream=True) as response:
        response.raise_for_status()
        blob_client.upload_blob(response.raw, overwrite=True)

    print(f"Uploaded {blob_name} to Azure Blob Storage.")

if __name__ == "__main__":
    try:
        files = get_file_list()
        for file_name in files:
            file_url = f"{DATA_BASE_URL}{file_name}"
            upload_to_gcs(file_url)
            upload_to_azure(file_url)
    except Exception as e:
        print(f"An error occurred: {e}")
