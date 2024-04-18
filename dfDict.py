# import dataframe_image as dfi
from natsort import index_natsorted
import numpy as np
import dataframe_image as dfi


# Create a dictionary for each wetland

def wetland_dict(wetlands_list,year):
    dataframe_dict ={}
    for wetland_name in wetlands_list:
        wetland_df = year[year["wetland_name"] == wetland_name].copy()
        wetland_df.drop(columns=["wetland_name"], inplace=True)
        wetland_df = wetland_df.sort_values(
            by="ES Percentage (%)", 
                                            key=lambda x: np.argsort(index_natsorted(wetland_df["ES Percentage (%)"])),
                                            ascending=False
                                            )
        wetland_df["ES Value (USD)"] = wetland_df["ES Value (USD)"].astype(str).apply(lambda x: "No Data" if x == "0.0" else x)
        wetland_df["ES Percentage (%)"] = wetland_df["ES Percentage (%)"].astype(str).apply(lambda x: "____" if x == "0.0" else x)
        dataframe_dict[wetland_name] = wetland_df

    for wetland_name, wetland_df in dataframe_dict.items():
        dfi.export(wetland_df, f'photos/2022_eco/{wetland_name}.png')

    return dataframe_dict
