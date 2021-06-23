import boto3
import sys
import configparser  
import os

def main(args):

    config = configparser.ConfigParser()
    config.read('config.ini')

    client = boto3.client('ecs')

    S3BUCKET = config["DEFAULT"]["S3Bucket"]
    CLUSTER_NAME = config["DEFAULT"]["Cluster"]
    TASK_DEF = config["DEFAULT"]["TaskDef"]
    CONTAINER_NAME = config["DEFAULT"]["ContainerName"]
    SUBNET = config["DEFAULT"]["subnet"]
    SECURITY_GROUP = config["DEFAULT"]["sg"]

    response = client.run_task(
        cluster = CLUSTER_NAME,
        launchType="FARGATE",
        taskDefinition=TASK_DEF,
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets":[SUBNET],
                "securityGroups":[SECURITY_GROUP],
                "assignPublicIp":"DISABLED",
            }
        },
        overrides={
            "containerOverrides":[
                {
                    "name":CONTAINER_NAME,
                    "command":["sh","/script/run_test.sh",S3BUCKET,args[1],args[2]],
                }
            ]
        }
    )
    taskArn = response['tasks'][0]['taskArn']
    print(taskArn)


if __name__== "__main__":

    args = sys.argv
    if len(args) < 3:
        print("USAGE: python run_task.py (input_video) (output_text)")
        sys.exit()

    main(args)