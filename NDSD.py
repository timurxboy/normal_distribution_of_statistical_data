from math import sqrt, fabs, pow


class StatisticsCalculator:
    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def calculate_mean(self):
        s = sum(self.data)
        mean = s / self.n
        return mean

    def calculate_standard_deviation(self):
        mean = self.calculate_mean()
        squared_diff_sum = sum((x - mean) ** 2 for x in self.data)
        variance = squared_diff_sum / self.n
        std_deviation = sqrt(variance)
        return std_deviation

    def calculate_coefficient_of_variation(self):
        mean = self.calculate_mean()
        std_deviation = self.calculate_standard_deviation()
        absolute_diff_sum = sum(fabs(x - mean) for x in self.data)
        coefficient = (std_deviation * 100) / (absolute_diff_sum / self.n)
        return coefficient

    def calculate_precision_index(self):
        mean = self.calculate_mean()
        std_deviation = self.calculate_standard_deviation()
        precision_index = (std_deviation * 100) / (mean * sqrt(self.n))
        return precision_index

    def calculate_skewness_coefficient(self):
        mean = self.calculate_mean()
        std_deviation = self.calculate_standard_deviation()
        sum_pow4 = sum(pow(x - mean, 4) for x in self.data)
        skewness_coefficient = sum_pow4 / (self.n * pow(std_deviation, 3))
        return skewness_coefficient

    def calculate_kurtosis_coefficient(self):
        mean = self.calculate_mean()
        std_deviation = self.calculate_standard_deviation()
        sum_pow4 = sum(pow(x - mean, 4) for x in self.data)
        kurtosis_coefficient = sum_pow4 / (self.n * pow(std_deviation, 4)) - 3
        return kurtosis_coefficient

    def calculate_mean_error(self):
        std_deviation = self.calculate_standard_deviation()
        mean_error = std_deviation / sqrt(self.n)
        return mean_error

    def calculate_standard_error(self):
        std_deviation = self.calculate_standard_deviation()
        standard_error = std_deviation / sqrt(2 * self.n)
        return standard_error

    def calculate_variance_error(self):
        coefficient_of_variation = self.calculate_coefficient_of_variation()
        variance_error = (coefficient_of_variation / sqrt(2 * self.n)) * sqrt(1 + 2 * coefficient_of_variation / 100)
        return variance_error

    def calculate_precision_error(self):
        precision_index = self.calculate_precision_index()
        precision_error = precision_index * sqrt((1 / (2 * self.n)) + pow(precision_index / 100, 2))
        return precision_error

    def calculate_skewness_error(self):
        std_deviation = self.calculate_standard_deviation()
        skewness_error = sqrt(std_deviation / self.n)
        return skewness_error

    def calculate_kurtosis_error(self):
        kurtosis_error = sqrt(24 / self.n)
        return kurtosis_error

    def calculate_ga(self):
        skewness_coefficient = self.calculate_skewness_coefficient()
        ga = sqrt((fabs(skewness_coefficient) * (self.n - 1)) / ((self.n + 1) * (self.n + 3)))
        return ga

    def calculate_ge(self):
        ge = sqrt((24 * (self.n - 2) * (self.n - 3) * self.n) / (pow(self.n - 1, 2) * (self.n + 3) * (self.n + 5)))
        return ge
