# rtmp-server-setup
setup stuff for the rtmp server

We are using third party software (nginx and the rtmp module available) for the rtmp server.

NGINX
Source: https://nginx.org/en/download.html

NGINX-RTMP-module
Source: https://github.com/arut/nginx-rtmp-module
License: https://github.com/arut/nginx-rtmp-module/blob/master/LICENSE

To stream to server use:
rtmp://<ip address>:1935/live/<your stream key>

to get stream from server:
http://<ip address>/live/<my-stream-key>/index.m3u8
http://<ip address>/dash/<my-stream-key>/index.mpd

We are currently using the full_nginx.conf file as the config

The conversion_script.py file contains a script for converting the flv video files to mp4. It requires the third party software ffmpeg to be installed, and for the files to be located in a directory of the user's home directory '/home/<username>/video_recording' with two subdirectories inside '/home/<username>/video_recording/flv_folder' '/home/<username>/video_recording/mp4_folder'. 
  To run the script, use the following command in the comamnd line:
  
  python3 conversion.py
  
  in the directory the file is located in.
  Alternatively, you can use the cron job in cron_conversion.txt to run the script every day at 11pm.
  To create the cron job, use the following command:
  
  crontab /path/to/cron_conversion.txt
  
# Script limitations 
The script heavily relies on the video file names to be standard. The stream key is used for naming the mp4 files that can be accessed post live stream. The current naming/stream key format is as follows:

CourseCode-lec#
For example:
ast101-lec4

If there are error with the network and the stream disconnects, the first part of the stream will be saved in CourseCode-lec#.mp4 and the other parts will be saved as CourseCode-lec#-part#.mp4 starting with part2. The stream key must be updated every time a new lecture is streamed.  If the stream key is not update, the previous mp4 file with the same name will be overwritten. Though the mp4 files of the lecture may be lost, the recorded streams will still be available as flv files.
Locating the correct flv file can pose an issue though as the unique identifier attached to the flv file is the timestamp (ex 1534126765).

Also since the format file name is very important to the file naming and creation, if the flv file does not contain at least two dashes the file will be skipped and an mp4 of it will not be created 
