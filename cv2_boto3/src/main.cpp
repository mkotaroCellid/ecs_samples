#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>

#include <hiredis.h>
#include <string>
#include <unistd.h>
#include <iostream>
#include <fstream>

using namespace cv;

int main(int argc, const char* argv[]) {
    
    if (argc != 3) {
        std::cerr << " usage: " << argv[0] << " [input_path] [output_path]" << std::endl;
        return -1;
    }

    cv::VideoCapture vcap;
    cv::Mat image;
    int width, height;
    double fps;

    if(!vcap.open(argv[1])) {
       std::cout << "Error opening video stream or file:"<< argv[1] << std::endl;
       return -1;
    }
    std::cout<<"Get Video Stream\n"<<std::endl;

    //output video info
    width = (int)vcap.get(cv::CAP_PROP_FRAME_WIDTH);
    height = (int)vcap.get(cv::CAP_PROP_FRAME_HEIGHT);
    fps = vcap.get(cv::CAP_PROP_FPS);

    std::ofstream ofs(argv[2]);
    if(!ofs){
        std::cout<<"Cannot open file" << std::endl;
        return -1;
    }
    ofs<<width<<" "<<height<<" "<<fps<<std::endl;
    ofs.close();

}
