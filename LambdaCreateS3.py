import json, boto3, os, time

AWS_DEFAULT_REGION = "eu-central-1"
# Region where lambda is  running
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

bucketname ="serega231bucket231456666" + str(time.time())

def lambda_handler(event, context):
    myS3 = boto3.resource('s3')
    try:
        results= myS3.create_bucket(Bucket=bucketname, CreateBucketConfiguration= {'LocationConstraint': AWS_DEFAULT_REGION})
        return("<h1><font color=green>S3 Bucket Created Susseccfully:</font</h1><br><br>" + str(results))
    except:
        #print("Error is hapen")
        print("<h1><font color=red>Error !</font></h1><br><br>" )
