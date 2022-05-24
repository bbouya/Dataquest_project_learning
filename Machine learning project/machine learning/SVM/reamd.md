Thiss is a tutorial for SVM algorithm
SVM or Support Vector Machine is a linear Model for classification and regression problems. It can solve linear and non-linear problems and work well for many practical problems. The idea of SVM is simple. The algorithm creates a line or a hyperplane which seperates the data into classes.
We have used Iris dataset for explanation: 
1. Import Iris dataset.
2. Preprocess Data(ignored here)
3. Split data into train and test data
4. fit the training data in SVM model
5. Predict the test data
6. Evalute F2 score and print confusion Matrix


## Multiclass Classification with support vector machines(SVM),

Support Vector Machines (SVM) are not new but are still powerful tool for classification due to their tendency not to averfit. but to perform well in many cases.
    - What's mathematical concept behind the support vector Machine ?
    - What is a kernel and what are kernal functions
    - What is the kernel trickN
    - What is the dual problem of a SVM?
    - How does Multiclass Classification take place?
    - Implementation via python and Scikit learn

#### The objectif :
The objective is to find a hyperplane in an n-dimensional space that separates the data points to their potential classes. The hyperplane should be positioned with the maximum distance to the data points. The data points with the minimum distance to the hyperplane are called Support Vectors. Due to their close position, their influence on the exact position of the hyperplane is bigger than of other data points. In the graphic below the Support Vectors are the 3 points (2 blue, 1 green) laying on the lines.
#### The kernel Functions :
The most popular kernel functions, that are also availbale in scijit-learn are linear, polynomial, radial basis function and sigmoid.
    1. Linear Function
    2. Polynomial Function
    3. Radial basis Function(RBF)
    4. Sigmoid Function.

#### The kernel Trick : 
What does the kernal function do ?
It takes two datapoints x_n, x_m and calculates a distance score of those, this score is higher for closer datapoints and vice versa, Using this score helps to transform the data points to a higher-dimensional mapping, which reduces the computatinal effort and time is especially useful for huge amounts of data, it prevents the need for a more complex transformation 
That's why this step is often referred to as KERNAL Trick.
As can be seen in the graphic below, the mapping of the data points is turned fromm a 2D to a 3D space using a kernel function ()