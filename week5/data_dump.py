import pandas as pd
import numpy as np
import os
from os.path import join as joinpath
from timeit import default_timer as timer

# define directory, should be within the homework folder for the "digital tools for finance" course
DATADIR = joinpath(os.environ.get("HOMEWORK_PATH"), "week5")

# create 1e6x5 df with random numbers between 0 and 1000 and set the fifth column equal to the fourth column
df = pd.DataFrame(np.random.randint(0,100,size = (1000000,5)), columns = ["first", "second", "third", "fourth", "fourth2"], dtype = np.float32)
df["fourth2"]=df["fourth"]

# write df to parquet file and show how long it took to write the file
tic = timer()
df.to_parquet(joinpath(DATADIR, 'data_dump.parquet'))
toc = timer()
print("time to write df to parquet file", round(toc - tic, 5), "seconds")

# write df to hdf file and show how long it took to write the file
tic = timer() 
df.to_hdf(joinpath(DATADIR, 'data_dump.hdf'), key = "rand_df")
toc = timer()
print("time to write df to hdf file", round(toc - tic, 5), "seconds")

# write df to feather file and show how long it took to write the file
tic = timer()
df.to_feather(joinpath(DATADIR, 'data_dump.feather'))
toc = timer()
print("time to write df to feather file", round(toc - tic, 5), "seconds")
