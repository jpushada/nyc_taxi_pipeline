#NYC Taxi Data configuration
SOURCE_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/"

#GCS Configuration
GCS_BUCKET_NAME = "nyc_raw_zone"
GOOGLE_APP_CREDENTIALS = ""C:/Users/ajay/nyc/nyc-data-pipeline-cebff4db0fce.json""

#Azure Blob Storage Configuration
AZURE_STORAGE_ACCOUNT = "nycstorageacc"
AZURE_CONTAINER_NAME = "nyc-raw-data"
AZURE_SAS_TOKEN = "sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-11-27T22:07:31Z&st=2024-10-24T14:07:31Z&spr=https&sig=IGrwFhWGfZ0Sk3BYDt%2FHwL281U%2Fmp60znaQ7LDYBCVU%3D"


CHUNK_SIZE = 1024*1024
