import matplotlib.pyplot as plt
import numpy as np

def sample_variance( data ) : 
  # Your code to compute the sample variance goes here
  


def common_variance( data1, data2 ) :
  # Your code to compute the common variance using the formula in the 
  # description on the left goes here
 
 

# This code generates the graph -- you should not need to modify from here onwards
xvals, total_var, common_var = np.zeros(10), np.zeros(10), np.zeros(10)
for i in range(10) : 
  # This line generates 100 samples from two normal distribuions.  The first of these 
  # distributions is centered on zero.  the second is centered on the value of i.
  # As we go through the loop the two distributions thus get progressively further and 
  # further appart.
  samples1, samples2 = np.random.normal(0,1,size=100), np.random.normal(i,1, size=100)
  xvals[i], common_var[i] = i, common_variance( samples1, samples2 )
  # This line calculates the variance and assumes all the data points are from a 
  # single distribution
  total_var[i] = sample_variance(np.concatenate([samples1, samples2]))
 
# This generates the graph.  
plt.plot( xvals, total_var, 'ro' )
plt.plot( xvals, common_var, 'bo' )
plt.xlabel("Difference between means")
plt.ylabel("Variance")
plt.savefig("variance.png")
