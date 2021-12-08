import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

for i in range(0, 11):
    instances = ec2.create_instances(
        ImageId='ami-0ed9277fb7eb570c9',
        InstanceType='m5.large',
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{"Key": "Type", "Value": "Worker"}]}],
    )

    for instance in instances:
        instance.wait_until_running()
    print('Instance ', i, ' running.')