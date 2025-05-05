import matplotlib.pyplot as plt
import seaborn as sns

# Plotting average finishing position over seasons for a driver
driver_id = 1  # Example driverId
driver_data = avg_finish[avg_finish['driverId'] == driver_id]

plt.figure(figsize=(10, 6))
sns.lineplot(data=driver_data, x='year', y='avg_finish_position')
plt.title('Average Finishing Position Over Seasons')
plt.xlabel('Year')
plt.ylabel('Average Finishing Position')
plt.gca().invert_yaxis()  # Lower positions are better
plt.show()

