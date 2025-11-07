import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env (if available)
load_dotenv()

# Create DynamoDB connection
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
    region_name="ap-south-1"  # 👈 Must be inside quotes!
)

# Reference your DynamoDB table
users_table = dynamodb.Table('User')

