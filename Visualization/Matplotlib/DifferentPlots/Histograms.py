""""""
"""
To get more of an intuitive sense for a dataset, we can use a histogram to display all the values.

A histogram tells us how many values in a dataset fall between different sets of numbers 
(i.e., how many numbers fall between 0 and 10? Between 10 and 20? Between 20 and 30?). 
Each of these questions represents a bin, for instance, our first bin might be between 0 and 10.

All bins in a histogram are always the same size. 
The width of each bin is the distance between the minimum and maximum values of each bin. 
In our example, the width of each bin would be 10.

Use the keyword bins to set how many bins we want to divide the data into. 
The keyword range selects the minimum and maximum values to plot.
"""

""" 
If we want to compare two different distributions, we can put multiple histograms on the same plot. 
This could be useful, for example, in comparing the heights of a bunch of men and the heights of a bunch of women. 

we can solve a problem like this:

1) Use the keyword alpha, which can be a value between 0 and 1. This sets the transparency of the histogram. 
   A value of 0 would make the bars entirely transparent. A value of 1 would make the bars completely opaque.
2) Use the keyword histtype with the argument 'step' to draw just the outline of a histogram:


We can normalize our histograms using normed=True. 
This command divides the height of each column by a constant such that the total shaded area of the histogram sums to 1.
"""






