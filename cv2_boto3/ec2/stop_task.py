import boto3
import sys
import configparser  
import os

def main(args):

    config = configparser.ConfigParser()
    config.read('config.ini')
    client = boto3.client('ecs')

    CLUSTER_NAME = config["DEFAULT"]["Cluster"]

    response = client.stop_task(
        cluster = CLUSTER_NAME,
        task=args[1]
    )


if __name__== "__main__":

    args = sys.argv
    if len(args) < 2:
        print("USAGE: python stop_task.py (taskArn)")
        sys.exit()

    main(args)