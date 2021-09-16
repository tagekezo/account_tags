import boto3
import csv
client = boto3.client('organizations',aws_access_key_id='your_access_key_id',aws_secret_access_key='your_secret_access_key')

def get_next_token(response):
    next_token = ''
    try:
        next_token = response['NextToken']
    except:
        next_token = ''
    return next_token

account_ids = []
response = client.list_accounts(
    MaxResults=20
)
account_ids = [account['Id'] for account in response['Accounts']]

next_token = get_next_token(response)
while next_token:
    response = client.list_accounts(
        MaxResults=20,
        NextToken=next_token
    )
    next_token = get_next_token(response)
    account_ids += [account['Id'] for account in response['Accounts']]


def parse_tags(response,account_id):
    return [{'id':account_id,'key':tag['Key'],'value':tag['Value']} for tag in response['Tags']]

account_tags_list = []
for account_id in account_ids:
    response = client.list_tags_for_resource(
        ResourceId=account_id
    )
    account_tags_list += parse_tags(response,account_id)
    next_token = get_next_token(response)
    while next_token:
        response = client.list_tags_for_resource(
            ResourceId=account_id,
            NextToken=next_token
        )
        next_token = get_next_token(response)
        account_tags_list += parse_tags(response,account_id)


csv_columns = ['id','key','value']
with open('account_tags.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in account_tags_list:
        writer.writerow(data)

print('complete')