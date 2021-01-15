import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def plot_data(data, xlabel, ylabel):
    plt.plot(data, 'r-')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=mean, color='b', linestyle='--')
    plt.savefig(str(num_measurements)+'.png')
    plt.clf()


def read_data(file_name, column):
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column]


for num_measurements in [25, 100, 500]:

    temperatures = read_data(file_name='data/temperatures.csv', column='Air temperature (degC)')

    mean = np.mean(temperatures)

    plot_data(data=temperatures, xlabel='measurements', ylabel='air temperature (deg C)')
Wait for the other members of the break-out room and discuss this point:
What will now happen if the functions are copy-pasted into another project/script? (Hint: how is for instance num_measurements declared?)
Run the modified improvement.py script.

Stage and commit the changes in improvement.py.
Step F: improve to more stateless functions
After digesting the material in this workshop you realize that you can do one last effort of improving your script by making your functions more stateless (aiming for pure functions here!)

Update the improvement.py file by copying the following code:
import pandas as pd
from matplotlib import pyplot as plt


def plot_data(data, mean, xlabel, ylabel, file_name):
    plt.plot(data, "r-")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(file_name)
    plt.clf()


def compute_mean(data):
    mean = sum(data) / len(data)
    return mean


def read_data(file_name, nrows, column):
    data = pd.read_csv(file_name, nrows=nrows)
    return data[column]


for num_measurements in [25, 100, 500]:

    temperatures = read_data(
        file_name="data/temperatures.csv",
        nrows=num_measurements,
        column="Air temperature (degC)",
    )

    mean = compute_mean(temperatures)

    plot_data(
        data=temperatures,
        mean=mean,
        xlabel="measurements",
        ylabel="air temperature (deg C)",
        file_name=str(num_measurements)+'.png',
    )
