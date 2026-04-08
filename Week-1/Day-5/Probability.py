# PROBABILITY 
import numpy as np

# Python Basics
fav = 1
tot = 2
prob = fav / tot
print(prob)

# 10 Dice rolls
rolls = np.random.randint(1,7,size=10)
print(rolls)

# Addition Rule
P_a = 0.5
P_b = 0.3
Pa_and_Pb = 0.4
Pa_union_Pb = P_a + P_b - Pa_and_Pb
print(Pa_union_Pb)

#Multiplication Rule
PA = 0.8
PB = 0.5
PA_and_PB = PA * PB
print(PA_and_PB)

# Complement Rule
pa = 0.4
pa_com = 1 - pa
print(pa_com)

# Conditional probability 
data = np.random.choice(['A', 'B'], size=1000)
P_B = np.mean(data == 'B')
P_A_and_B = np.mean((data == 'B') & (data == 'A'))
print(P_A_and_B)

# Bayes Theorem
P_disease = 0.01
P_positive_given_disease = 0.9
P_positive = 0.05

P_disease_given_positive = (P_positive_given_disease * P_disease) / P_positive
print(P_disease_given_positive)

# Discrete Distribution
#Bernoulli
from scipy.stats import bernoulli
bernoulli.rvs(p=0.5, size=10)

# Binomial
from scipy.stats import binom
binom.pmf(k=3, n=10, p=0.5)

# Poisson
from scipy.stats import poisson
poisson.pmf(k=2, mu=3)

# Normal Distribution
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 100)
plt.plot(x, norm.pdf(x))
plt.show()

# Uniform Distribution
from scipy.stats import uniform
uniform.pdf(0.5)

# Exponential Distribution
from scipy.stats import expon
expon.pdf(1)

# Expectation and variance
import numpy as np
data = np.array([1, 2, 3, 4])
print(np.mean(data))
print(np.var(data))

# Likelihood and log-likelihood
from scipy.stats import norm
data = [1.2, 0.9, 1.1]
log_likelihood = np.sum(norm.logpdf(data, loc=1, scale=0.1))
print(log_likelihood)