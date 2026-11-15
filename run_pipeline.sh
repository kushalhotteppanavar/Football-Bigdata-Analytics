#!/bin/bash
set -e

chmod +x mapreduce/mapper.py mapreduce/reducer.py

echo "[1/4] Generating football match dataset..."
python3 scripts/generate_data.py

echo "[2/4] Uploading raw dataset to HDFS..."
hdfs dfs -mkdir -p /football/raw
hdfs dfs -put -f data/football_match_logs.csv /football/raw/

echo "[3/4] Running Hadoop MapReduce aggregation..."
hdfs dfs -rm -r -f /football/processed
STREAMING_JAR=$(find $HADOOP_HOME/share/hadoop/tools/lib/ -name "hadoop-streaming-*.jar" | head -n 1)
hadoop jar "$STREAMING_JAR" \
  -files mapreduce/mapper.py,mapreduce/reducer.py \
  -mapper mapper.py \
  -reducer reducer.py \
  -input /football/raw/football_match_logs.csv \
  -output /football/processed

echo "[4/4] Running Hive queries and exporting Power BI CSVs..."
mkdir -p output
hive -f hive/analytics.hql
hive -e "SET hive.cli.print.header=true; SELECT * FROM football_analytics.player_season_stats;" | tr '\t' ',' > output/powerbi_player_stats.csv
hive -e "SET hive.cli.print.header=true; SELECT team, SUM(goals) AS total_goals, SUM(assists) AS total_assists, ROUND(AVG(pass_accuracy), 2) AS avg_pass_accuracy, SUM(tackles) AS total_tackles, ROUND(AVG(performance_score), 2) AS team_avg_rating FROM football_analytics.player_season_stats GROUP BY team ORDER BY team_avg_rating DESC;" | tr '\t' ',' > output/powerbi_team_stats.csv

echo "Pipeline complete! Power BI files ready in ./output/"
