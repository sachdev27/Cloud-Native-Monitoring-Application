import boto3

client = boto3.client('ecr', region_name='ap-south-1')


repo = 'DevOps-Test-Repo'

respone = client.create_repository(repositoryName="devops-test-repo")

repository_uri = respone['repository']['repositoryUri']

print(repository_uri)