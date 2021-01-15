import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def plot_data(data, mean, xlabel, ylabel, file_name):
   plt.plot(data, "r-")
   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.axhline(y=mean, color="b", linestyle="--")
   plt.savefig(file_name)
   plt.clf()


def read_data(file_name, nrows, column):
   data = pd.read_csv(file_name, nrows=nrows)
   return data[column]

for num_measurements in [25, 100, 500]:

   temperatures = read_data(
       file_name="data/temperatures.csv",
       nrows=num_measurements,
       column="Air temperature (degC)",
   )

   mean = np.mean(temperatures)

   plot_data(
       data=temperatures,
       mean=mean,
       xlabel="measurements",
       ylabel="air temperature (deg C)",
       file_name=str(num_measurements)+'.png',
   )
