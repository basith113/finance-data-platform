import os
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = os.getenv("AWS_REGION")
BUCKET = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

local_folder = "data_generator/output"

for file in os.listdir(local_folder):
    if file.endswith(".csv"):

        local_path = f"{local_folder}/{file}"
        s3_path = f"raw/{file}"

        s3.upload_file(local_path, BUCKET, s3_path)

        print(f"Uploaded {file} to S3")