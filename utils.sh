export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/home/mmahrous/.local/hadoop-2.9.2
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_HOME}/share/hadoop/tools/lib/*

function start-hdfs { 
    hdfs namenode -format;
    $HDHM/sbin/hadoop-daemon.sh --script hdfs start namenode;
    $HDHM/sbin/hadoop-daemon.sh --script hdfs start datanode;
    hdfs dfs -mkdir /user;
    hdfs dfs -mkdir /user/$USER
}

function start-yarn { 
    $HDHM/sbin/yarn-daemon.sh start nodemanager;
    $HDHM/sbin/yarn-daemon.sh start resourcemanager
}
function move-files { 
    hdfs dfs -put mapper.py /user/$USER/;
    hdfs dfs -put reducer.py /user/$USER/;
    hdfs dfs -put nltk.tgz /user/$USER/;
    hdfs dfs -put nltk_data.tgz /user/$USER/;
    hdfs dfs -put freqs.json /user/$USER/;
    hdfs dfs -put english.txt /user/$USER/;
    hdfs dfs -put input /user/$USER/
}
function remove-files { 
    hdfs dfs -rm -r /user/$USER;
    hdfs dfs -mkdir /user/$USER
}
function mapred { 
    JOB=$1;
    hadoop org.apache.hadoop.streaming.HadoopStreaming \
    -files $JOB/mapper.py,$JOB/reducer.py,$JOB/freqs.json \
    -archives $JOB/nltk.tgz#nltk,$JOB/nltk_data.tgz#nltk_data \
    -input $JOB/input \
    -output $JOB/output \
    -mapper mapper.py \
    -combiner reducer.py \
    -reducer reducer.py
}

function nltk-deps {
    [ -d "nltk" ] && rm -rf nltk
    [ -f "nltk.zip" ] && rm nltk.zip
    [ -f "nltk_data.tgz" ] && rm nltk_data.tgz
    pip3 install --target=nltk nltk --ignore-installed
    cd nltk
    tar -czvf ../nltk.tgz .
    cd ..
    rm -rf nltk
    cd nltk_data
    tar -czvf ../nltk_data.tgz .
    cd ..
}

alias rmapred="mapred hdfs://localhost:9000/user/$USER"
alias rmop="hdfs dfs -rm -r /user/$USER/output"