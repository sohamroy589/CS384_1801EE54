# All decimal 3 places
import math

# Function to compute mean
def mean(first_list):
    sum_value = summation(first_list)
    if len(first_list) == 0:
        return 0
    mean_value = sum_value / len(first_list)
    return round(mean_value, 3)


# Function to compute median. You cant use Python functions
def median(first_list):
    if len(first_list) == 0:
        return 0
    sorted_list = sorting(first_list)
    median_value = round(sorted_list[len(first_list) >> 1], 3)
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    return round(math.sqrt(variance(first_list)), 3)


# Function to compute variance. You cant use Python functions
def variance(first_list):
    if len(first_list) == 0:
        return 0
    variance_value = 0
    mean_value = mean(first_list)
    for x in first_list:
        if isinstance(x, int) or isinstance(x, float):
            variance_value += (x - mean_value) ** 2
        else: return 0
    variance_value /= len(first_list)
    return round(variance_value, 3)


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    rmse_value = 0
    # RMSE Logic
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    mse_value = 0
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    mae_value = 0
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    nse_value = 0
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    pcc_value = 0
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    skewness_value = 0
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    sorted_list = first_list
    for r in range(len(first_list)-1, 0, -1):
        for i in range(r):
            if sorted_list[i] > sorted_list[i+1]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i+1]
                sorted_list[i+1] = temp
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    kurtosis_value = 0
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    summation_value = 0
    for x in first_list:
        if isinstance(x, int) or isinstance(x, float):
            summation_value += x
        else: return 0 
    return round(summation_value, 3)
