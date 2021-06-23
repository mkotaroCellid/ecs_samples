
datetime=`date "+%Y%m%d-%H-%M-%s"`
input_name="/tmp/${datetime}_in.mp4"
output_name="/tmp/${datetime}_out.txt"


python3 /script/python/pull_data_from_s3.py $1 $2 $input_name


/source/cv2-s3-sample $input_name $output_name 

python3 /script/python/push_data_to_s3.py $output_name $1 $3

rm $input_name $output_name
