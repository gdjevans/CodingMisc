import boto3
import click
import sys
import os
import pdb
import time
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError

load_dotenv()
client = boto3.client('ec2')

slclient = WebClient(token=os.environ['SLACK_API_TOKEN'])

def startserver(insttype, instkey, dryrun):
    try:
        resources = client.run_instances(ImageId='ami-9ccc8aed', MinCount=1, MaxCount=1, InstanceType=insttype, KeyName=instkey, DryRun=dryrun)
        instid2 = client.describe_instances(InstanceIds=[resources['Instances'][0]['InstanceId']])
        
        #This is the old way of doing it...
        while instid2['Reservations'][0]['Instances'][0]['State']['Name'] != 'running':
            print("Not Yet Running")
            instid2 = client.describe_instances(InstanceIds=[resources['Instances'][0]['InstanceId']])
            time.sleep(2)
        
        print(instid2['Reservations'][0]['Instances'][0]['PublicIpAddress'])
        pdb.set_trace()
    except:
        print(sys.exc_info()[1])
        return 1
    return 0

def listinstances():
    resp = client.describe_instances()
    for reservation in resp["Reservations"]:
        for instance in reservation["Instances"]:
            #print(instance)
            print(instance['InstanceId'],instance['InstanceType'], instance['State']['Name'])

def send_message(channel, message):
    try:
        response = slclient.chat_postMessage(channel=channel,text=message)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")

@click.command()
@click.option('-a', '--action', required=True)
@click.option('-t', '--type', 'insttype')
@click.option('-k', '--key', 'instkey')
@click.option('--dryrun/--no-dryrun', default=False)
def maincode(action,insttype,instkey, dryrun):
    if action == 'start':
        if insttype == None or instkey == None:
            print("No instance type or key provided, please run --help")
            return 1
        if startserver(insttype,instkey,dryrun) == 0:
            send_message('#general', "Server Start Success!")
        else:
            send_message('#general', "ERROR: Server Start Failed!")
    elif action == 'list':
        listinstances()
    else:
        print("We don't know what you want!")

maincode()