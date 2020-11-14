# Hadoop_ecosystem
Perform some analysis on data extracted from reddit


## How to run
1. Source `utils.sh` . `source utils.sh`
2. Start HDFS and yarn, you can use `start-yarn` and `start-hdfs` from `utils.sh`, tested on Hadoop 2.9.2
3. Get nltk depenedanet libraries by running `nltk-deps`
4. Put the input file in the input folder and move files to HDFS by running `move-files`
5. Start the MapReduce job by running `rmapred`
