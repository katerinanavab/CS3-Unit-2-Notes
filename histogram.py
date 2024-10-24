import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Generate data 
rng = np.random.default_rng(50)
data = rng.normal(size=1000)

# HISTOGRAM shows FREQUENCY of values
plt.hist(data)
plt.savefig('histogram.png')
plt.close()

# Example of a more customized hist
plt.hist(data, bins=30, density=True, alpha=0.5, histtype='stepfilled', color='orchid', edgecolor='none')
plt.savefig('hist-custom.png')
plt.close()

# HEXAGONAL binnings
mean = [0, 0]
cov = [[1,1], [1,2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T
plt.hexbin(x, y, gridsize=10)
cb = plt.colorbar(label='count in bin')

plt.savefig('hexbin.png')