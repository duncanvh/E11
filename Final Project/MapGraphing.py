import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
df = pd.read_csv("D:\Data&Documents\Berkeley\Classes\25Spring\Engin11\FinalPre\FinalPresenationData.csv")
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df.Longitude, df.Latitude),
    crs="EPSG:4326"
)
gdf = gdf.to_crs(epsg=3857)
ax = gdf.plot(
    column="reading",
    cmap="viridis", 
    markersize=40,
    edgecolor="k",
    legend=True,
    figsize=(6,6)
)
ctx.add_basemap(
    ax, 
    source=ctx.providers.OpenStreetMap.Mapnik,
    attribution=False
)

ax.set_axis_off()
plt.tight_layout()
plt.show()