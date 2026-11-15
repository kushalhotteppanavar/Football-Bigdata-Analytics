# Football Player Performance Analytics Using Big Data and Hadoop

## Project Structure
```text
football_bigdata/
├── data/
│   └── football_match_logs.csv       # 50,000-row raw match dataset
├── mapreduce/
│   ├── mapper.py                     # Hadoop Streaming Mapper
│   └── reducer.py                    # Hadoop Streaming Reducer (aggregations + Performance Score)
├── hive/
│   └── analytics.hql                 # Hive DDL & analytical queries
├── scripts/
│   └── generate_data.py              # Synthetic dataset generator
├── output/
│   ├── powerbi_player_stats.csv      # Pre-generated sample output for Power BI
│   └── powerbi_team_stats.csv        # Pre-generated sample team stats for Power BI
└── run_pipeline.sh                   # End-to-end Ubuntu execution script
```

## Quick Start on Ubuntu
1. Extract this archive into your home directory (`~/football_bigdata`).
2. Start Hadoop HDFS & YARN:
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```
3. Run the entire pipeline:
   ```bash
   cd ~/football_bigdata
   chmod +x run_pipeline.sh
   ./run_pipeline.sh
   ```
4. Import `output/powerbi_player_stats.csv` and `output/powerbi_team_stats.csv` into Power BI Desktop.
