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