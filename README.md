# synchronization
lidar camera synchronization

Note-Currently implemented and tested using a recorded rosbag file,with lidar and camera both running at 10Hz for 10 minutes and also tested with live feed from the sensors.

Method in brief-
   
   Initially the sensors are freely running,with the lidar and camera topics being published.The sync event is then published(after 1-2 secs wrt the bag file start time),with the timestamp as the message.The timestamp is the system time.Once the cam_gen.py and lidar_gen.py scripts detect this sync event,the offset is computed as the difference between the sensors' header timestamp and the timestamp published on the sync event as shown in the image below.
   ![alt text](https://github.com/poornimajd/newdemo/blob/main/IMG_20210129_140354_HDR.jpg)
This offset is then added to the sensors' timestamp to get the corrected timestamp and the data from the two sensors is stored in a folder with the names as the corrected timestamp.
   
Observation-
  
   Some data is discarded because the corrected timestamps of the lidar camera pair,is not same or has a difference of close to 100ms.
  
   The offset computed is not constant for the entire data,(has a 100ms variation),and hence the offset is computed everytime.
  
   The data stored from the above method is comprised of lidar and image frames having the exact same timestamp.
  
  
