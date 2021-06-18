import boto3

def main():
    print('Start!!!')

    # create a new session with the given profile
    # this is one way of creating a session
    session = boto3.Session(profile_name='devuser-mycloudstack')

    # get the s3 client
    s3_client = session.client('s3')
    #s3_resource = session.resource('s3')

    # Retrieve the list of existing buckets
    response = s3_client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
    
    '''
    bucket_name = 'acloudbucket-12345-accesslogs'
    key = 'boto3/s3.py'

    file_name = "s3.py"
    # Upload File
    print('Start - File Upload')
    s3_client.upload_file(file_name, bucket_name, key)
    print('End - File Upload')

    # Download File  
    # print('Start - File Download')  
    s3_client.download_file(bucket_name, key, 'xyz.py')
    print('End - File Download')
    '''

    print('End!!!')

main()