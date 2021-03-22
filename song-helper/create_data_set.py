# Load Exploratory Data Analysis (EDA) packages
import pandas as pd

# Load our dataset
df_yelp = pd.read_table('song-helper/song-helper/data/yelp_labelled.txt')
df_imdb = pd.read_table('song-helper/song-helper/data/imdb_labelled.txt')
df_amz = pd.read_table('song-helper/song-helper/data/amazon_cells_labelled.txt')

# Concatenate our Datasets
frames = [df_yelp,df_imdb,df_amz]

# Renaming Column Headers
for colname in frames:
    colname.columns = ["Message","Target"]

# Column names
for colname in frames:
    print(colname.columns)

# Assign a Key to Make it Easier
keys = ['Yelp','IMDB','Amazon']

# Merge or Concat our Datasets
df = pd.concat(frames,keys=keys)

# Length and Shape
df.shape

df.head()

df.to_csv('song-helper/song-helper/data/sentimentdataset.csv')

# Data Cleaning
df.columns

# Checking for Missing Values
df.isnull().sum()
