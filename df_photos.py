from pathlib import Path
import pandas as pd
from dfDict import wetland_dict
import dataframe_image as dfi
from PIL import Image
from PIL import ImageDraw

df = pd.read_json("data/ecosystem_service_data_copy.json")

# Extract data for each year
df_2018 = df[["wetland_name","ecosystem_service","value_2018","percentage_2018"]]
df_2022 = df[["wetland_name","ecosystem_service","value_2022","percentage_2022"]]


df_list = [df_2018, df_2022]

# Rename column names to appear as in the dashboard
for dataframe in df_list:
    dataframe.columns = ["wetland_name", "Ecosystem Service", "ES Value (USD)", "ES Percentage (%)"]

# Create a list of all unique wetlands in the dataframe
wetlands_names_list = df["wetland_name"].unique().tolist()


# wetland_dict(wetlands_names_list, df_2018)
# wetland_dict(wetlands_names_list, df_2022)

for each in wetlands_names_list:
    img = Image.open(f'photos/2018_eco/{each}.png')
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Add Text to an image
    I1.text((38, 10), "\u00A9 Colwed", fill=(255, 255, 255, 128))

    # Display edited image
    # img.show()

    # Save the edited image
    img.save(f"photos/copyright/2018_copy/{each}.png")

