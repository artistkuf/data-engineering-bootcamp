import json

from google.cloud import storage
from google.oauth2 import service_account


DATA_FOLDER = "data"
BUSINESS_DOMAIN = "greenery"
project_id = "deb-skooldio-project"
location = "asia-southeast1"
bucket_name = "deb-bootcamp-03"
data = "users"
dt = "2020-10-23"
partition = dt.replace("-", "")

# Prepare and Load Credentials to Connect to GCP Services
keyfile_gcs = "deb-uploading-files-to-gcs.json"
service_account_info_gcs = json.load(open(keyfile_gcs))
credentials_gcs = service_account.Credentials.from_service_account_info(
    service_account_info_gcs
)

# Load data from Local to GCS
storage_client = storage.Client(
    project=project_id,
    credentials=credentials_gcs,
)
bucket = storage_client.bucket(bucket_name)

file_path = f"{DATA_FOLDER}/{data}.csv"
destination_blob_name = f"raw/{BUSINESS_DOMAIN}/{data}/{dt}/{data}.csv"

# YOUR CODE HERE TO LOAD DATA TO GCS
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)
