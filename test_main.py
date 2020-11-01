import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_variance(self) : 
        for i in range(5) : 
            data = np.random.normal( i, i*0.3, size=50) 
            mu = sum(data) / len(data)
            var = ( len(data) / (len(data)-1) )*( sum(data*data) / len(data) - mu*mu )
            self.assertTrue( np.abs( var - sample_variance(data) )<1e-7, "your function for calculating the variance is not correct" )
            
    def test_common_variance(self) : 
        self.assertTrue( inspect.getsource(common_variance).find("sample_variance")>0, "Your function for the common variance does not include a call to sample_variance" ) 
        for i in range(5) : 
            dat1, dat2 = np.random.normal(i, i*0.2, size=50 ), np.random.normal( i-4, i*0.4, size=20 )
            var1, var2 = sample_variance(dat1), sample_variance(dat2) 
            final_var = ( (len(dat1)-1)*var1 + (len(dat2)-1)*var2 ) / ( len(dat1) + len(dat2) - 2 )
            self.assertTrue( np.abs( final_var - common_variance(dat1, dat2))<1e-7, "Your function for calculating the common variance is not working correctly" )
