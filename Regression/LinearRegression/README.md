
## Linear Regression

Linear regression is used to formulate an equation to represent a relationship between two variables and predict the value of a variable based on the independent variable.
To measure the direction and the strenght of the relationship between Y and X, we find covariance and the correlation coefficient.

<img alt="Covariance Graphs" align="right" src="https://www.statisticshowto.com/wp-content/uploads/2013/12/g-covariance.gif">

**Covariance:** Covariance is a measure of how much two random variables vary together. It’s similar to variance, but where variance tells you how a single variable varies, co variance tells you how two variables vary together.

<img src="https://render.githubusercontent.com/render/math?math=cov_{x,y}=\frac{\displaystyle\sum_{i=1}^{n}(x_{i}-\bar{x})(y_{i}-\bar{y})}{N-1}">

Note: The population covariance is the same fomula, except `N` instead on `N - 1`. For any estimator of population parameter related to despersion, it is taken `N - 1`, as this extimator is found to be unbiased, consistent, efficient, and sufficient.

Covariance tells what is the direction of one variable with respect to the another. If the covariance if positive, the relation is directly proportional, if not, inversely proportional. We can see that, variance of x is nothing but, covariance of x with itself. In two variable point of view, the relation is always positive, and it indicates the average distance among the elements from mean, where as in two different variables, it cannot be assigned to a quality, it just indicates the direction of the relationship. This measure can also indicate the strength of the relationship, but unfortunately the highest number is not fixed, so there is no particular limit where we can say this relationship has good strength.

Taking an example of positive slope for a scatter plot, and using the covariance equaiton, we can see that the value generated at each point is positive and incase of negetive slope, the values generated are negetive. So instead of looking at the graph for a larger data sets, we can caluculate the covariance and emphasize the direction of the relation more efficiently(moreover with a certain quantitative mearure indicating the rate of the proportionality).


**Correlation**: Similar to covariance, correlation also indecates the direction relationship of one variable with respect to another variable, and interestingly, the direction of the reverse of the relationship is same and has the same strenght. As we used standardization for scaling the data, we scale corvariance and restrict the value between 0 and 1, so it is easy to know how much strong the relationship is, irrespective of the scale of data. So it is better measure than covariance to know the relationship among the variables.

<p align='center'><img src='imgs/Correlation.png'></p>

Note: 
1. From the formula it can be seen that, Cor(X, Y) = Cor(Y, X).
2. Unlike Cov(X, Y), Cor(X, Y) is scale invariant, that is, it does not change if we change the units of measurements, and the mod of correlation is always less than 1. [ $-1 \leq Cov(X, Y) \leq 1$ ]
3. Cor(X, Y) = 0, does not necessarilymean that Y and X are not related. It only implies that they are not linearly related, because the correlation coefficient measures only linear relationships.

So correlation is not a good measure if the realationship is not linear, and the correlation is effected by outliers. Tho emphasize this point, Anscombe has constructed four data sets, known as Anscombe quartet, each with distinct pattern, but each having the same correlation coefficient.

<p align='center'> <img src='imgs/AnscombeQuartet.png'> </p>

The relationship between a response variable Y and a predictor variable X is postulated as a linear model

<p align='center'>Y = &beta;<sub>0</sub> + &beta;<sub>1</sub>X + &epsilon;,</p>

Where &beta;<sub>0</sub> and &beta;<sub>1</sub> are constants called model regression coefficients or parameters, and &epsilon; is a random distrubance or error.
A linear regression model is used to estmate a value based on any other value, given some data to train the model. Linear regression model is prefered when we observe a linear pattern in the scatter plot and correlation is high, then the results produced by this model is most likely to be equal to the original value.

<img src="https://render.githubusercontent.com/render/math?math=\hat{\beta}_{1} = \frac{\sum_{}(y_{i} - \overline{y})(x_{i} - \overline{x})}{\sum_{}{(x_{i}- \overline{x})^2}}">

and

<img src="https://render.githubusercontent.com/render/math?math=\hat\beta_{0} = \overline{y} - \hat\beta_{1}\overline{x}">

the y cap we got is called fitted values. It is the point on the least squares regression line corresponding to the independent variable value. The vertical distance corresponding to the i<sup>th</sup> observation is

<p align='center'>e<sub>i</sub> = y<sub>i</sub> - &circ;y<sub>i</sub> </p>

Another formula to find the coefficient of X is 

<img src="http://render.githubusercontent.com/render/math?math=\hat\beta_{1} = \frac{Cov(Y, X)}{Var(X)} = Cor(Y, X)\frac{s_{y}}{s_{x}}">


