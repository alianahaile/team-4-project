import boto3
import src.app as run_etl
import csv


def start(event, context):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')
    data_as_list = data.splitlines()
    
    with open("/tmp/temp.csv", 'w') as etl_file:
        etl_writer = csv.writer(etl_file)
        
        for line in data_as_list:
            etl_writer.writerow(line)
        
        run_etl.etl("/tmp/temp.csv")
        
        return 'finito'
    




    # s = boto3.resource('s3')
    # our_buck = s.Bucket(bucket)
    # bucket_contents = []
    # for file in our_buck.objects.all():
    #     bucket_contents.append(file.key)
    # return bucket_contents