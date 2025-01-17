# All decimal 3 places
import math

# Function to compute mean
def mean(first_list):
    return round(mean_helper(first_list), 3)


def mean_helper(first_list):
    sum_value = summation_helper(first_list)
    if len(first_list) == 0:
        return 0
    mean_value = sum_value / len(first_list)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    if len(first_list) == 0:
        return 0
    sorted_list = sorting(first_list.copy())
    median_value = round(sorted_list[len(first_list) >> 1], 3)
    return round(median_value, 3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    return round(math.sqrt(variance_helper(first_list)), 3)


def variance_helper(first_list):
    if len(first_list) == 0:
        return 0
    variance_value = 0
    mean_value = mean_helper(first_list)
    for x in first_list:
        if isinstance(x, (int, float)):
            variance_value += (x - mean_value) ** 2
        else: return 0
    variance_value /= len(first_list)
    return variance_value

# Function to compute variance. You cant use Python functions
def variance(first_list):
    return round(variance_helper(first_list), 3)


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    return round(math.sqrt(mse_helper(first_list, second_list)), 3)


def mse_helper(first_list, second_list):
    mse_value = 0
    if len(first_list) != len(second_list) or len(first_list) == 0:
        return 0
    for x, y in zip(first_list, second_list):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            mse_value += (x - y) * (x - y)
        else: 
            return 0
    mse_value /= len(first_list)
    return mse_value

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    return round(mse_helper(first_list, second_list), 3)


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    if len(first_list) != len(second_list) or len(first_list) == 0:
        return 0
    diff_list = []
    for x, y in zip(first_list, second_list):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            diff_list.append(abs(x - y))
        else: 
            return 0
    mae_value = summation_helper(diff_list) / len(first_list)
    return round(mae_value, 3)


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    if len(first_list) != len(second_list) or len(first_list) == 0:
        return 0
    for x, y in zip(first_list, second_list):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            return 0
    mse_value = mse_helper(first_list, second_list)
    variance_value = variance_helper(first_list)
    nse_value = 1 - (mse_value / variance_value)
    return round(nse_value, 3)


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    if len(first_list) != len(second_list) or len(first_list) == 0:
        return 0
    for x, y in zip(first_list, second_list):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            return 0
    x_mean, y_mean = mean_helper(first_list), mean_helper(second_list)
    x_var, y_var = variance_helper(first_list), variance_helper(second_list)
    pcc_value = 0
    for i in range(len(first_list)):
        pcc_value += (first_list[i] - x_mean) * (second_list[i] - y_mean)
    pcc_value /= math.sqrt(x_var * y_var) * len(first_list)
    return round(pcc_value, 3)

# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    skewness_value = 0
    x_mean = mean_helper(first_list)
    for x in first_list:
        if isinstance(x, (int, float)):
            skewness_value += (x - x_mean) ** 3
        else:
            return 0
    skewness_value /= len(first_list) * (math.sqrt(variance_helper(first_list)) ** 3)
    return round(skewness_value, 3)
    
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
    x_mean = mean_helper(first_list)
    for x in first_list:
        if isinstance(x, (int, float)):
            kurtosis_value += (x - x_mean) ** 4
        else:
            return 0
    kurtosis_value /= len(first_list) * (variance_helper(first_list) ** 2)
    return round(kurtosis_value, 3)


# Function to compute sum. You cant use Python functions
def summation(first_list):
    return round(summation_helper(first_list), 3)

def summation_helper(first_list):
    summation_value = 0
    for x in first_list:
        if isinstance(x, (int, float)):
            summation_value += x
        else: return 0 
    return summation_value
