## Regression

Regression analysis is a conceptual and most widely implemented practical method for investigating functional relationships among variables. Regression can be applied in any feild or sector, where the re is a need for establishing relationship among variables. The relationship is expressed in the form of an equation or a model conncecting the response or depencent variable and one or more explanatory or predictor variables.

> Regression analysis is a mathematical measure of the average realtionship between two or more variables in terms of the original units of the data.

We denote the response variable by Y and the set of predctor variables by X with subscript of i, indicating each explanatory variable like, 

<p align="center">X<sub>1</sub>, &nbsp; X<sub>2</sub>,  &nbsp; X<sub>3</sub>, &nbsp; X<sub>4</sub>,&nbsp;..., &nbsp; X<sub>n</sub></p>

An example of linear regression model is 

<p align="center">Y =  &beta;<sub>0</sub> + &beta;<sub>1</sub>X<sub>1</sub> +  &beta;<sub>2</sub>X<sub>2</sub> + &nbsp;........ &nbsp; +  &beta;<sub>p</sub>X<sub>p</sub></p>

Where &beta;<sub>i</sub> are called the regression parameters or coefficients, are known constants to be determined (estimated) from the data.


### Steps in Regression Analysis

1. Statement of the problem

Regression analysis usually starts with a formulation of the problem. This includes the determination of the question(s) to be addressed by the analysis. The problem statement is the first and perhaps the most important step in regression analysis. It is important because an ill-defined problem or a misformulated question can lead to wasted effort. It can lead to the selection of irrelevant set of variables or to a wrong choice of the statistical method of analysis. A question that is not carefully formulated can also lead to the wrong choice of a model. Sup- Selection of potentially relevant variables. |

2. Selection of potentially relevant variables

Next step after the statement of the problem is to select a set of variables that
are thought by the experts in the area of study to explain or predict the response
variable.

3. Data collection

Based on the problem and variables under study, we can collect revelant data through appropriate means. The data mostly used now is secondary data, for research purpose primary data is need, which is collected through survey agencies, own surveys or online survey methods.

4. Model specification

The form of the model that is thought to relate the response variable to the set of predictor variables can be specified initially by the experts in the area of study based on their knowledge or their objective and/or subjective judgments. The hypothesized model can then be either confirmed or refuted by the analysis of the collected data. Note that the model needs to be specified only in form, but it can still depend on unknown parameters. We need to select the form of the function f(X<sub>1</sub> , X<sub>2</sub>, ... ,X<sub>p</sub>) in (1.1). This function can be classified into two types: linear and nonlinear. An example of a linear function is 
<p align = "center">Y = &beta;<sub>0</sub> + &beta;<sub>1</sub> + &epsilon; </p>
while a non-linear function is 
<p align="center">Y = &beta;<sub>0</sub> + e<sup>&beta;<sub>1</sub>X<sub>1</sub></sup> + &epsilon;	</p>
Note: A variable that can take only one of two possible valeus such as yes or no, 1 or 0, and sucess or failure, is called binary variable. In case of Binary variable as a response variable, the regreession we use is logistic regression.

5. Choice of fitting method

After the model has been defined and the data have been collected, the next task is to estimate the parameters of the model based on the collected data. This is also referred to as parameter estimation or model fitting. The most commonly used method of estimation is called the least squares method. Under certain assumptions, least squares method produce estimators with desirable properties.

6. Model fitting

The next step in the analysis is to estimate the regression parameters or to fit the model to the collected data using the chosen estimation method (e.g., least squares). 

7. Model validation and criticism
8. Using the chosen model(s) for the solution of the posed problem.


| Types of Regression  | Conditions   | 
|-------------- | -------------- |
| Univariate    | Only one quantitative response variable     |
| Multivariate  | Two or more quantitative response variables |
| Simple	| Only one predictor variable 		      |
| Multiple	| Two or more predictor variables	|
| Linear	| All parameters enter the equation linearly, possibly after transformation of the data	|
| NonLinear	| Ther relationship between the response and some of the predictors is nonlinear or some of the parameters appear nonlinearly, but no transormation is possible to make the parameters appear linearly	|
| Analysis of variance	| All predictors are qualitative variables |
| Analysis of covariance| Some predictors are quantitative variables and others are qualitative variables|
| Logistic 	| The response variableis qualitative |

### Normalization

This is a scaling technique, used to make all the data points range between 0 to 1 to remove the units of each mearuse factor. Formula to nomalize the data is

<p align='center'>X<sub>new</sub> = ( X - X<sub>min</sub> ) / ( X<sub>max</sub> - X<sub>min</sub> ) </p>
Note: Percentile of students in competative exams with multiple shifts uses min max scalar method, to generalize the marks allotation to all students from different exam shifts, which gives same scale for marks comparision irrespective of the shift or toughness of the exam.

### Standardization

<img src='imgs/standardization.png' align='right' width=300 >

Standardization is a scaling method where the values are centered around mean with a unit standard deviation. It means if we will calculate mean and standard deviation of standard scores it will be 0 and 1 respectively. Formula to standardize the data is 

<p align='center'> z = ( x - &mu; ) / &sigma; </p>
Where, 
&mu; = Mean of the distribution under study
&sigma; = Standard deviation of the distribution under study

Note: 

1. If we plot the standardized data for KDE(kernal density extimation - Non parametric way to extimate the distribution of the data), we get a normal distribution with mean 0 and standard deviation 1. 
2. In clase there exits outliers, Normalization is highly impacted, so standardization is preferred, since the outliers impact more on the mean, but considering as it is measure of central tendency, stadardization has less impact that normalization.

