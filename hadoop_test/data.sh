cd /usr/local/Cellar/hadoop/3.3.2 && \
sbin/stop-all.sh &&\
bin/hdfs namenode -format |\
sbin/start-dfs.sh |\
sbin/start-yarn.sh |\
bin/hdfs dfs -mkdir /user |\
bin/hdfs dfs -mkdir /user/hongphucvo &&\
bin/hdfs dfs -put  /Users/hongphucvo/Desktop/DE/col 