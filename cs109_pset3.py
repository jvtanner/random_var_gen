from numpy.random import rand


def simulate_bernoulli(p=0.4):
    if rand() < p:
        return 1
    return 0


def simulate_binomial(n=20, p=0.4):
    count = 0
    for i in range(n):
        if simulate_bernoulli(p):
            count += 1
    return count
    # return number of successes


def simulate_geometric(p=0.03):
    count = 0
    while not simulate_bernoulli(p):
        count += 1
    return count


def simulate_negativeBinomial(r=5, p=0.03):
    count = 0
    successes = 0
    while successes < r:
        count += simulate_geometric(p)
        successes += 1
    return count


def simulate_poisson(lamb=3.1):
    return simulate_binomial(60000, lamb/10000)


def simulate_exponential(lamb=3.1):
    for i in range(60000):
        if simulate_bernoulli(lamb/10000):
            return i
    return

def main():
    x = simulate_bernoulli(1)
    return x

if __name__ == "__main__":
    main()