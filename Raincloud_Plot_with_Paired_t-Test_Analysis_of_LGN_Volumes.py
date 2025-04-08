import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import ptitprince as pt from scipy.stats 
import ttest_rel

df = pd.DataFrame({"ID": np.arange(len(LGN_lh)), "LH": LGN_lh, "RH": LGN_rh}) df_long = df.melt(id_vars="ID", var_name="Hemisphere", value_name="Volume")

# Plot Raincloud
plt.figure(figsize=(6, 6)) 
ax = pt.RainCloud(x="Hemisphere", y="Volume", data=df_long, 
palette=["#1f77b4", "#ff7f0e"], 
bw=0.2, width_viol=0.5, width_box=0.2, orient="v")
plt.title("Raincloud Plot: LH vs. RH Volume") 
plt.show()

# Perform Paired t-test
t_stat, p_value = ttest_rel(LGN_lh, LGN_rh) 
print(f"Paired t-test: t = {t_stat:.3f}, p = {p_value:.3f}")
