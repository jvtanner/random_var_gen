from numpy.random import rand
import math


def simulate_bernoulli(p=0.4):
    if rand() < p:
        return 1
    return 0


def simulate_binomial(n=20, p=0.4):
    for i in range(n):
        return simulate_bernoulli(p)


def simulate_geometric(p=0.03):
    count = 0
    while not simulate_bernoulli(p):
        count += 1
    return count


def simulate_negativeBinomial(r=5, p=0.03):
    count = 0
    while not simulate_bernoulli(p) == r:
        count += 1
    return count


def simulate_poisson(lamb=3.1):
    event = 0
    limit = 60000
    for i in range(limit):
        if simulate_bernoulli(lamb/limit):
            event += 1
    return event


def simulate_exponential(lamb=3.1):
    limit = 60000
    for i in range(limit):
        if simulate_bernoulli(lamb/limit):
            return i


