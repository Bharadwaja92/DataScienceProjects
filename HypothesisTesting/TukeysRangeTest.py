""""""
"""
Let's say that we have performed ANOVA to compare three sets of data from the three VeryAnts stores. 
We received the result that there is some significant difference between datasets.

Now, we have to find out which datasets are different.

We can perform a Tukey's Range Test to determine the difference between datasets.

If we feed in three datasets, such as the sales at the VeryAnts store locations A, B, and C, Tukey's Test can tell us 
which pairs of locations are distinguishable from each other.

The function to perform Tukey's Range Test is pairwise_tukeyhsd, which is found in statsmodel, not scipy. 
We have to provide the function with one list of all of the data and a list of labels that tell the function which 
elements of the list are from which set. We also provide the significance level we want, which is usually 0.05.

For example, if we were looking to compare mean scores of movies that are dramas, comedies, or documentaries, 
we would make a call to pairwise_tukeyhsd like this:

movie_scores = np.concatenate([drama_scores, comedy_scores, documentary_scores])
labels = ['drama'] * len(drama_scores) + ['comedy'] * len(comedy_scores) + ['documentary'] * len(documentary_scores)

tukey_results = pairwise_tukeyhsd(movie_scores, labels, 0.05)
It will return a table of information, telling you whether or not to reject the null hypothesis for each pair of datasets.
"""

