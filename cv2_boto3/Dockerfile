FROM --platform=linux/x86-64 ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN echo "Asia/Tokyo" > /etc/timezone

RUN apt update -y && apt upgrade -y && apt install -y build-essential cmake 


#install openCV + redis
RUN apt install -y libopencv-dev libhiredis-dev

#install python3 + boto3
RUN apt install -y python3-pip && pip3 install boto3

# # install AWS SDK C++ (this will take long time and require storage size)
# # if you do not use C++ SDK, comment out these lines
# RUN apt install -y git libcurl4-openssl-dev libssl-dev zlib1g-dev
# WORKDIR /opt
# RUN git clone --recurse-submodules https://github.com/aws/aws-sdk-cpp && mkdir /opt/aws-sdk-cpp-build
# WORKDIR /opt/aws-sdk-cpp-build
# RUN cmake -DBUILD_ONLY="s3" ../aws-sdk-cpp && make && make install 


RUN mkdir /work && mkdir /source && mkdir /script && mkdir /work/build
COPY ./script/ /script
COPY ./src/ /work

#build main tools
WORKDIR /work/build
RUN cmake .. && make 
RUN mv /work/build/cv2-s3-sample /source


#Make sure to add CMD command
WORKDIR /
CMD ["echo","test"]
