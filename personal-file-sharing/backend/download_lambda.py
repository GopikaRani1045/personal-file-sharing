import json
import boto3
import base64

s3 = boto3.client('s3')
BUCKET = "upanddownloadfiles3"  # <-- replace with your real S3 bucket name

def lambda_handler(event, context):
    try:
        # Safely get the fileName from queryStringParameters
        file_name = event.get("queryStringParameters", {}).get("fileName")
        if not file_name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'fileName' query parameter"})
            }

        # Get file from S3
        obj = s3.get_object(Bucket=BUCKET, Key=file_name)
        file_content = obj["Body"].read()

        # Encode to Base64
        encoded_content = base64.b64encode(file_content).decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "fileName": file_name,
                "fileContent": encoded_content
            })
        }

    except s3.exceptions.NoSuchKey:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"File '{file_name}' not found in S3"})
        }
    except s3.exceptions.NoSuchBucket:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"S3 bucket '{BUCKET}' does not exist"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
