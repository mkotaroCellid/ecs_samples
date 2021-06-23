cmake_minimum_required(VERSION 2.8)
project(cv2-s3-sample)
set (CMAKE_CXX_STANDARD 11)

#[[
    find_package(AWSSDK REQUIRED COMPONENTS s3) 
]]

find_package(PkgConfig)
pkg_check_modules(OPENCV REQUIRED opencv4)
pkg_check_modules(HIREDIS REQUIRED hiredis)

set(INCLUDE_DIR
    ${OPENCV_INCLUDE_DIRS}
    ${HIREDIS_INCLUDE_DIRS}
)
include_directories("${INCLUDE_DIR}")


add_executable(cv2-s3-sample main.cpp)


set(LIBRARIES ${OPENCV_LIBRARIES} ${HIREDS_LIBRARIES})

target_link_libraries(cv2-s3-sample ${LIBRARIES})
#[[
    target_link_libraries(cv2-s3-sample ${AWSSDK_LINK_LIBRARIES})
]]
