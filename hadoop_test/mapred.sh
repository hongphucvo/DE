bin/hdfs dfs -rm -r -f st1 && 
mapred streaming  \
-input col \
-output st1   \
-mapper m1.py \
-reducer r1.py \
-file /Users/hongphucvo/Desktop/hadoop_test/m1.py \
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
-file /Users/hongphucvo/Desktop/hadoop_test/reduce_tf.py|\

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