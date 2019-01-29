""""""
"""  KNN
How does K-Nearest Neighbors define what it means for two points to be close to each other?
> By using the distance formula using all features of the data.


What is a potential problem if k is even?
> There could be an equal number of nearest neighbors from both classes.


Why is normalizing your data essential for K-Nearest Neighbors?
> So a feature with a vastly different scale does not dominate other features.


Overfitting happens when:
> k is too small so outliers dominate the result.


What would you expect to happen to the validation accuracy of a K-Nearest Neighbors classifier as 
k increases from 1 to infinity?
> Validation accuracy goes up and then down. As k increases, you begin to avoid overfitting and accuracy goes up.
    Once k gets too big, you begin to underfit, and accuracy will go back down.
    
    
The .predict() function in scikit-learn’s KNeighborClassifier class takes _____ as a parameter and returns _____.
> A list of points to classify / a list of predictions.


True/False: K-Nearest Neighbors can work with data with 1000 features.
True. K-Nearest Neighbors can work with data with any number of features greater than 0.


Underfitting happens when:
> k is too big so larger trends in the dataset aren’t represented.

"""
"""  BAYES THEOREM

A certain lake contains 30% Magikarp and 70% whitefish. Misty has a 20% of catching a fish. 
What is the probability that Misty catches a Magikarp?
> 0.6%  Catching a fish and catching a Magikarp are independent events, so we multiply 0.2 * 0.3 and get 0.06 which is 6%.


What does P(A|B) mean?
> The probability of event A given that B is true.


What is the definition of a prior?
> An additional piece of information that helps us calculate a probability.


What is the difference between a Bayesian approach and a Frequentist approach?
> A Bayesian approach uses a prior. A frequentist approach does not.


Why can we ignore the denominator of Bayes Theorem when calculating the probabilities of each class?
> The denominator is the same for every class.


If the target_names of a Naive Bayes classifier are [B, A, D, C], and the predict_proba function returns the 
list [.3, .1, .5, .1] for a given datapoint, what is the predicted class for that datapoint? 
> D


Which of the following is not a Natural Language Processing technique that can improve performance of a Naive Bayes Classifier?
> Smoothing.


What is the purpose of smoothing in a Naive Bayes Classifier?
> To prevent a feature with a probability of 0 from ruining the total probability. 
  Smoothing doesn't remove any data from your dataset!
  
  
The .predict() method in the MultinomialNB class takes _____ as a parameter and returns _____
> A list of data points, a list of classifications.


Why is a Naive Bayes Classifier a supervised machine learning algorithm?
> You need labeled data in order to calculate the probabilities used in Bayes Theorem.
"""

"""  K MEANS 

K-means algorithm stops when ________.
> centroids stabilize (convergence)


What is inertia in the context of clustering?
> Inertia is the distance from each sample to the centroid of its cluster. The lower the better.


For Step 1 of K-means, how do we place the k centroids for the initial clusters?
> Place k random centroids.


What is the purpose of the elbow method?
> To find the best number of clusters.


The sklearn library comes with a breast cancer dataset with characteristics of breast cancer cell nuclei: 
mean radius, mean texture, mean perimeter, mean area, etc. What is a sample and what is a feature in this dataset?
> Each cell nuclei (row) is a sample and the mean radius (column) is a feature.




"""
