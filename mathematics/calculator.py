
from numpy import sqrt, mean, square

# # creating a RMS function
def rms(serie):
    return round(sqrt(mean(square(serie))), 4)