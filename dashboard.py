import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Football Big Data Analytics", layout="wide")
st.title("⚽ Football Player Performance Analytics (Hadoop + Hive)")

players_df = pd.read_csv("output/powerbi_player_stats.csv")
teams_df = pd.read_csv("output/powerbi_team_stats.csv")

# Clean column prefixes if exported by Hive CLI
players_df.columns = [c.split(".")[-1] for c in players_df.columns]
teams_df.columns = [c.split(".")[-1] for c in teams_df.columns]

# Sidebar Filters
st.sidebar.header("Filters")
selected_teams = st.sidebar.multiselect(
    "Select Team(s)",
    options=sorted(players_df["team"].unique()),
    default=sorted(players_df["team"].unique()),
)
selected_pos = st.sidebar.multiselect(
    "Select Position(s)",
    options=sorted(players_df["position"].unique()),
    default=sorted(players_df["position"].unique()),
)

filtered = players_df[
    (players_df["team"].isin(selected_teams))
    & (players_df["position"].isin(selected_pos))
]

# KPI Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Goals", int(filtered["goals"].sum()))
c2.metric("Total Assists", int(filtered["assists"].sum()))
c3.metric("Avg Pass Accuracy", f"{filtered['pass_accuracy'].mean():.2f}%")
top_player = (
    filtered.sort_values("performance_score", ascending=False).iloc[0]["player_name"]
    if not filtered.empty
    else "N/A"
)
c4.metric("Top Rated Player", top_player)

# Top 10 Players & Team Comparison
col1, col2 = st.columns(2)
with col1:
    top10 = filtered.sort_values("performance_score", ascending=False).head(10)
    fig1 = px.bar(
        top10,
        x="performance_score",
        y="player_name",
        color="position",
        orientation="h",
        title="Top 10 Players by Performance Score",
    )
    fig1.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(
        teams_df,
        x="team",
        y=["total_goals", "total_assists"],
        barmode="group",
        title="Team Goals vs. Assists",
    )
    st.plotly_chart(fig2, use_container_width=True)

# Head-to-Head Player Comparison
st.subheader("Head-to-Head Player Comparison")
p_col1, p_col2 = st.columns(2)
p1 = p_col1.selectbox("Player A", players_df["player_name"].unique(), index=0)
p2 = p_col2.selectbox("Player B", players_df["player_name"].unique(), index=1)
comp_df = players_df[players_df["player_name"].isin([p1, p2])][
    [
        "player_name",
        "team",
        "position",
        "goals",
        "assists",
        "pass_accuracy",
        "shot_accuracy",
        "tackles",
        "performance_score",
    ]
]
st.dataframe(comp_df, use_container_width=True)

# Full Rankings Table
st.subheader("Overall Player Rankings")
st.dataframe(
    filtered.sort_values("performance_score", ascending=False),
    use_container_width=True,
)
