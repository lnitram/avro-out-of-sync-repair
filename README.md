avro-out-of-sync-repair
=======================

Just a quick workaround to fix out-of-sync problems in avro files

I had a broken avro file that caused an exception while running a map and reduce-job on hadoop. 
The errormessage in the log was like this:

```
org.apache.avro.AvroRuntimeException: java.io.IOException: Invalid sync!
	at org.apache.avro.file.DataFileStream.hasNext(DataFileStream.java:210)
	at org.apache.avro.mapred.AvroRecordReader.next(AvroRecordReader.java:67)
	at org.apache.avro.mapred.AvroRecordReader.next(AvroRecordReader.java:34)
	at org.apache.hadoop.mapred.MapTask$TrackedRecordReader.moveToNext(MapTask.java:215)
	at org.apache.hadoop.mapred.MapTask$TrackedRecordReader.next(MapTask.java:200)
	at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:48)
	at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:417)
	at org.apache.hadoop.mapred.MapTask.run(MapTask.java:332)
	at org.apache.hadoop.mapred.Child$4.run(Child.java:268)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.security.auth.Subject.doAs(Subject.java:396)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1408)
	at org.apache.hadoop.mapred.Child.main(Child.java:262)
Caused by: java.io.IOException: Invalid sync!
	at org
```

In my case this little python script helped to repair the file. Maybe it's useful for somebody else...

Path and filenames are hardcoded in the python file and have to be changed.

To run this python-script avro support has to be installed:

```easy_install avro```
