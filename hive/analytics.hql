CREATE DATABASE IF NOT EXISTS football_analytics;
USE football_analytics;

DROP TABLE IF EXISTS player_season_stats;

CREATE EXTERNAL TABLE player_season_stats (
    player_name STRING,
    team STRING,
    position STRING,
    matches_played INT,
    minutes_played INT,
    goals INT,
    assists INT,
    passes_completed INT,
    passes_attempted INT,
    pass_accuracy DOUBLE,
    tackles INT,
    shots INT,
    shots_on_target INT,
    shot_accuracy DOUBLE,
    performance_score DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/football/processed';

-- 1. Verify Data Load
SELECT * FROM player_season_stats LIMIT 10;

-- 2. Top 10 Players Overall by Performance Score
SELECT 
    RANK() OVER (ORDER BY performance_score DESC) AS player_rank,
    player_name, team, position, goals, assists, pass_accuracy, tackles, performance_score
FROM player_season_stats
LIMIT 10;

-- 3. Team Performance Aggregation
SELECT 
    team,
    SUM(goals) AS total_goals,
    SUM(assists) AS total_assists,
    ROUND(AVG(pass_accuracy), 2) AS avg_pass_accuracy,
    SUM(tackles) AS total_tackles,
    ROUND(AVG(performance_score), 2) AS team_avg_rating
FROM player_season_stats
GROUP BY team
ORDER BY team_avg_rating DESC;

-- 4. Top Goal Contributors (Goals + Assists) by Position
SELECT 
    position, player_name, team, goals, assists, (goals + assists) AS goal_contributions
FROM player_season_stats
ORDER BY goal_contributions DESC;
