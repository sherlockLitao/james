print('hello')# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from matplotlib import pyplot as plt

#years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
#gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

import tensorflow as tf 
sess = tf.Session() 
a = tf.constant(1) 
b = tf.constant(2) 
print(sess.run(a+b))