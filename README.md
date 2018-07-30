# rtmp-server-setup
setup stuff for the rtmp server

We are using third party software (nginx and the rtmp module available) for the rtmp server.

NGINX
Source: https://nginx.org/en/download.html

NGINX-RTMP-module
Source: https://github.com/arut/nginx-rtmp-module
License: https://github.com/arut/nginx-rtmp-module/blob/master/LICENSE

To stream to server use:
rtmp://ec2-54-197-1-1.compute-1.amazonaws.com:1935/live/<your stream key>

to get stream from server:
http://ec2-54-197-1-1.compute-1.amazonaws.com/live/<my-stream-key>/index.m3u8
http://ec2-54-197-1-1.compute-1.amazonaws.com/dash/<my-stream-key>/index.mpd
