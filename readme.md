# Fachprojekt Data Mining and Data Analysis

Code for an undergraduate data mining and data analysis project on Gamma-Hydron Separation at TU Dortmund University.

In the project, we discuss different approaches to tell apart gamma-rays from other particles of the universe, which is known as 'Gamma-Hydron Separation'. In order to do so, we will extract different features from a given set of particle observations, which could potentially characterize gamma-rays. Afterwards, we use different classifier-algorithms in order to distinguish those gamma-rays from non-relevant observations.  

The following code contains basic library imports and loads the sample data, aswell as the test data and their extracted feature sets. In addition, 10 random data samples are shown; a data sample is provided as a two dimensional array, so each value can be interpreted as a pixel. Especially as it comes to the feature extraction, we think it is way easier to think of the samples as pictures with pixels rather than pure arrays with individual array values.  

As it comes to the plots for different hyperparameter-configurations of the classifiers, we already precomputed inital results by executing the given code in advance. If the values are supposed to be computated again, the given array allocations have to be deleted (or marked as a comment).

__Unfortunatly we cannot provide the original data.__
