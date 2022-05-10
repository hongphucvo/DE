http://localhost:9870/explorer.html

open /tmp xoa het hadoop

cd /usr/local/Cellar/hadoop/3.3.2 && sbin/stop-all.sh


bin/hdfs namenode -format && sbin/start-dfs.sh && sbin/start-yarn.sh

# Data from scratch
bin/hdfs dfs -mkdir /user && 
bin/hdfs dfs -mkdir /user/hongphucvo && 
bin/hdfs dfs -put  /Users/hongphucvo/Desktop/DE/col 

# updated data
python /Users/hongphucvo/Desktop/DE/data.py &&\
bin/hdfs dfs -rm -r -f col &&\
bin/hdfs dfs -put  /Users/hongphucvo/Desktop/DE/col


# cat /Users/hongphucvo/Desktop/DE/collection/1.txt | python /Users/hongphucvo/Desktop/DE/map_1.py
# cat /Users/hongphucvo/Desktop/DE/col/3.txt | python /Users/hongphucvo/Desktop/hadoop_test/reduce_1.py
# cat /Users/hongphucvo/Desktop/col/3.txt| python /Users/hongphucvo/Desktop/hadoop_test/map_doc.py
# cat /Users/hongphucvo/Desktop/col/dictionary_map_1 | python /Users/hongphucvo/Desktop/hadoop_test/reduce_doc.py
# cat /Users/hongphucvo/Desktop/col/dictionary_map_1 | python /Users/hongphucvo/Downloads/reduce_doc.py
# cat /Users/hongphucvo/Desktop/dictionary_map_1  | python /Users/hongphucvo/Desktop/hadoop_test/map_word.py
# cat /Users/hongphucvo/Desktop/temp  | python /Users/hongphucvo/Desktop/hadoop_test/reduce_query.py

# mapreduce-1 | mapreduce-2 | mapreduce-3 | ...



# A-Z


cd /usr/local/Cellar/hadoop/3.3.2 &&\
bin/hdfs namenode -format && sbin/start-dfs.sh && sbin/start-yarn.sh &&\
bin/hdfs dfs -mkdir /user && \
bin/hdfs dfs -mkdir /user/hongphucvo && \
bin/hdfs dfs -put  /Users/hongphucvo/Desktop/DE/col &&\


bin/hdfs dfs -rm -r -f st1 && 
mapred streaming  \
-input col \
-output st1   \
-mapper m1.py \
-file /Users/hongphucvo/Desktop/hadoop_test/m1.py \
-reducer r1.py \
-file /Users/hongphucvo/Desktop/hadoop_test/r1.py|\


bin/hdfs dfs -rm -r -f st2 && 
mapred streaming  \
-input st1 \
-output st2   \
-mapper m2.py \
-file /Users/hongphucvo/Desktop/hadoop_test/m2.py \
-reducer r2.py \
-file /Users/hongphucvo/Desktop/hadoop_test/r2.py |\


bin/hdfs dfs -rm -r -f st3 && 
mapred streaming  \
-input st2 \
-output st3   \
-mapper map_tf.py \
-file /Users/hongphucvo/Desktop/hadoop_test/map_tf.py \
-reducer reduce_tf.py \
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_tf.py  |\


bin/hdfs dfs -rm -r -f st4 && 
mapred streaming  \
-input st3 \
-output st4   \
-mapper map_sum_tf.py \
-file /Users/hongphucvo/Desktop/hadoop_test/map_sum_tf.py \
-reducer reduce_sum_tf.py \
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_sum_tf.py|\


bin/hdfs dfs -rm -r -f st5 && 
mapred streaming  \
-input st4 \
-output st5   \
-mapper map_group_tf.py \
-file /Users/hongphucvo/Desktop/hadoop_test/map_group_tf.py \
-reducer reduce_group_tf.py \
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_group_tf.py|\

bin/hdfs dfs -rm -r -f result && \
mapred streaming \
-input st5 \
-output result  \
-mapper map_word.py \
-file /Users/hongphucvo/Desktop/hadoop_test/map_word.py \
-reducer reduce_word.py \
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_word.py 





#query
cd /usr/local/Cellar/hadoop/3.3.2 &&\
bin/hdfs dfs -rm -r -f query.txt &&\
bin/hdfs dfs -put /Users/hongphucvo/Desktop/DE/query.txt  |\

bin/hdfs dfs -rm -r -f st6 && 
mapred streaming  \
-input query.txt st5 \
-output st6 \
-mapper map_query.py \
-file /Users/hongphucvo/Desktop/hadoop_test/map_query.py \
-reducer reduce_query.py \
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_query.py   |\


bin/hdfs dfs -rm -r -f search && 
mapred streaming  \
-input st6 \
-output search   \
-mapper map_search.py \
-file /Users/hongphucvo/Desktop/hadoop_test/map_search.py \
-reducer reduce_search.py \
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_search.py 