import sys
import boto3
import os

def main(args):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(args[1])
    bucket.download_file(args[2],args[3])

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 4:
        print("Usage:python3 pull_data_from_s3.py (s3_bucket) (s3_data_path) (save_path)")
        sys.exit()
    
    main(args)