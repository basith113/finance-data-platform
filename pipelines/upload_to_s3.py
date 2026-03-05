import os
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = os.getenv("AWS_REGION")
BUCKET = os.getenv("S3_BUCKET_NAME")

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

# Local CSV folder
local_folder = "data_generator/output"

# Upload each CSV file
for file in os.listdir(local_folder):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        local_path = f"{local_folder}/{file}"
        s3_path = f"raw/{table_name}/{file}"

        try:
            s3.upload_file(local_path, BUCKET, s3_path)
            print(f"Uploaded {file} → s3://{BUCKET}/{s3_path}")

        except Exception as e:
            print(f"Failed to upload {file}")
            print(e)

print("Upload process completed.")