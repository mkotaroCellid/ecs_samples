import sys
import boto3


def main(args):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(args[2])
    bucket.upload_file(args[1],args[3])

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 4:
        print("Usage:python3 push_data_to_s3.py (save_path) (s3_bucket) (s3_data_path)")
        sys.exit()
    
    main(args)