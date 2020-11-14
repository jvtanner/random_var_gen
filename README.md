# Random variable simulations

Understanding the process that leads to different random variables is a great way to gain
familiarity for what they mean. For each random variable, write a function that simulates its
generation process. Your function should return a number. The only probability function that
you may use when coding your solution is numpy.random.rand(): a function that returns a
uniform random in the range [0, 1]. We include a solution to (a) in the starter code and below.
Note that a function from one part may call a function from a previous part if you wish.


a. X ∼ Ber(p = 0.4)     
1 or 0 to indicate whether or not an underlying event was “successful.”

b. X ∼ Bin(n = 20, p = 0.4)     
The number of successes after 20 independent experiments. 

c. X ∼ Geo(p = 0.03)        
The number of trials until the first success. 

d. X ∼ NegBin(r = 5, p = 0.03)      
The number of trials until 5 successes. 

e. X ∼ Poi(λ = 3.1) approximate     
The number of events in a minute, where the historical rate is 3.1 events per min.
Hint: Break the minute down into 60,000 ms events like we did in lecture.

f. X ∼ Exp(λ = 3.1) approximate     
The amount of time until the next event, where the historical rate is 3.1 events per min.
Hint: Like part (e), think of an event for each millisecond.


