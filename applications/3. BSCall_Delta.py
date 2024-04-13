from math import exp, log, sqrt
from scipy.stats import norm

def BSCall_Delta(spot, time, strike, expiry, vol, rate):
    vol /= 100
    rate /= 100
    d1 = (log(spot/strike)+(rate+vol**2/2) * (expiry - time)) / vol / sqrt(expiry - time)
    return norm.cdf(d1)

spot = 100
time = 0
strike = 110
expiry = 0.5
vol = 25
rate = 3

delta_call = BSCall_Delta(spot, time, strike, expiry, vol, rate)
print(f"The value of the call delta is: ${delta_call:.3f}")
