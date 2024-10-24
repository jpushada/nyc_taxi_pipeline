#NYC Taxi Data configuration
SOURCE_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/"

#GCS Configuration
GCS_BUCKET_NAME = "nyc_raw_zone"
GOOGLE_APP_CREDENTIALS = "D:/Dijendra/MyProjects/gcp_config/nyc-taxi-pipeline-439606-7787e5221af1.json"

#Azure Blob Storage Configuration
AZURE_STORAGE_ACCOUNT = "nycstorageac"
AZURE_CONTAINER_NAME = "nyc-raw-data"
AZURE_SAS_TOKEN = "sp=rwdl&st=2024-10-24T06:33:43Z&se=2024-12-24T15:33:43Z&spr=https&sv=2022-11-02&sr=c&sig=NfiHNvRlb1ysK8FXa1xXvgbDOLrR7eiIb2D55sS4Hhc%3D"


CHUNK_SIZE = 1024*1024