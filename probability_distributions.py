from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#1
f = stats.poisson(2)
f.pmf(0)
f.sf(3)
f.sf(0)
(f.rvs(10000)==0).mean()
(f.rvs(10000)>=3).mean()
(f.rvs(10000)>0).mean()


#2
x = stats.norm(3.0,.3)
x_2 = np.random.normal(3, .3, 1000)
x.isf(.05)
x.ppf(.15)
x_1 = (x_2 <= 3.5).mean()
x_3 = np.percentile(x_2, 15)



#3
y = stats.binom(4326, .02).sf(97)
y_2 = (stats.binom(4326, .02).rvs(1000)>=97).mean()
#4

stats.binom(60,.01).pmf(1)
stats.poisson(300).pmf(1)
#5

stu = round(22 * 3 *.9)
stats.binom(stu, .03).sf(0)
stats.binom(stu, .03 * 2).sf(0)
stats.binom(stu, .03 * 5).sf(0)
(stats.binom(stu, .03).rvs(1000)> 0).mean()
(stats.binom(stu, .03*2).rvs(1000)> 0).mean()
(stats.binom(stu, .03*5).rvs(1000)> 0).mean()
#6
t = 60 - (10 + 15 + 2)
stats.norm(30, 5).cdf(t)
(np.random.normal(30, 5, 1000)< 33).mean()