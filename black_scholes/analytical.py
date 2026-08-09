import numpy as np
import scipy

## Function which simply calculates intermediary values that are used in ##
## the below calculations                                                ##

def intermediaries(S, K, T, R, sigma):
	d_1 = (np.log(S/K)+(R+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
	d_2 = d_1 - sigma*np.sqrt(T)
	return d_1, d_2

## This function takes in the current stock price (S), strike price (K), ##
## time until expriation in years (T), risk-free rate (R) and the        ##
## volatility of the stock (sigma) and returns the fair price for the    ##
## European call option today                                            ##

def bs_call(S, K, T, R, sigma):
	d_1, d_2 = intermediaries(S, K, T, R, sigma)
	return S*scipy.stats.norm.cdf(d_1) - K*np.exp(-R*T)*scipy.stats.norm.cdf(d_2)

## This function performs a similar calulation but instead returns the   ##
## fari price for the European put option today                          ##

def bs_put(S, K, T, R, sigma):
	d_1, d_2 = intermediaries(S, K, T, R, sigma)
	return K*np.exp(-R*T)*scipy.stats.norm.cdf(-d_2)-S*scipy.stats.norm.cdf(-d_1)


