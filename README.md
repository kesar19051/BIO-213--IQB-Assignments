# Preprocessing and data splitting

*   Checked for null values
*   Removed duplicate values
*   Not identified outliers

Splitting the dataset

*   Random attribute set so that same results are displayed.
*   Stratify is set to the label to keep the distribution equal as the original data set.

# (A) Training

# Q3. Varying hyperparameters

1. Criterion

The results obtained using Entropy are better than Gini. Entropy is a measure of information that indicates the disorder of the features with the target while the gini impurity measures the frequency at which any element of the dataset will be mislabelled when it is randomly labeled. 
The entropy takes values between 0 and 1 while Gini is half of it: it takes value between 0 and 0.5

2. Splitter

Splitter='random' gives a degradation of result. The accuracy, precision and recall are less than the base model. This is because 'random' splitter uses a random uniform function while 'best' splitter evaluates all splits using the criterion before splitting.

3. Min-samples split

4. Max depth

As seen from the above accuracy vs depth graph, the accuracy increases as the depth increases. This is because with increasing depth the model becomes more and more complex and captures more information about the data. However, with high depth the model tends to overfit and keeping the restricting the max_depth of the tree can help combat overfitting.

5. Min Samples Leaf

With this parameter there is an increase in the performance of the model. According to scikit-learn, we can use min_samples_leaf to ensure that multiple samples inform every decision in the tree, by controlling which splits will be considered. 

6. Max Features

Max_features tells number of features to consider when looking for the best split. By default it looks at all the features for the split. However, here it looks at the limited features due to which we see a decreased performance scores in terms of accuracy, precision and recall. If we keep it default, it can lead to overfitting.

7. Class Weight

class_weight is used to provide a weight or bias for each output class. But what does this actually mean, see when the algorithm calculates the entropy or gini impurity to make the split at a node,

8. Max Leaf Nodes
