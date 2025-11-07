import boto3
import os
from dotenv import load_dotenv
from botocore.config import Config

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REGION = os.getenv("REGION")

boto_config = Config(signature_version="v4")

dynamodb = boto3.resource(
    "dynamodb",
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    config=boto_config
)

try:
    users_table = dynamodb.Table("User")
    print("✅ Connected successfully to DynamoDB table:", users_table.name)
except Exception as e:
    print("❌ Error connecting to DynamoDB:", e)
