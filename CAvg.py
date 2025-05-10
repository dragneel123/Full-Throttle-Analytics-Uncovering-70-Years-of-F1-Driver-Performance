# Calculate average finishing position per driver per season
avg_finish = merged_df.groupby(['driverId', 'year'])['positionOrder'].mean().reset_index()
avg_finish.rename(columns={'positionOrder': 'avg_finish_position'}, inplace=True)
-+