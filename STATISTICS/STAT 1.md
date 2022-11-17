# STATISTICS

**Data:** Measurements or objesrvations that are collected as a source of information.

**Population:** The collection of data related to the subject under study, and number of individuals in the population is called poulation size, denoted by 'N'.

**Sample:** A finite subset of statistical individuals in a population is called a sample and number of individuals in a sample is called sample size, denoted by 'n'.

There are two types of statistics:

1. Descriptive statistics
2. Inferential statistics

### VARIABLE MEASUREMENT SCALES

Four types of variable measurement scales


1. **Nominal data**
    
    Categorical data where ranking is not important. Nominal data is data that can be labelled or classified into mutually exclusive categories within a variable. These categories cannot be ordered in a meaningful way.
    
    Eg: Male / Female
    
2. **Ordinal data**

    Ordinal data is a categorical, statistical data type where the variables have natural, ordered categories and the distances between the categories are not known.
    
    Eg: (Low; Medium; High), (Strongly Agree; Agree; Neutral; Disagree; Strongly Disagree)

3. **Interval data**

    Interval data, also called an integer, is defined as a data type which is measured along a scale, in which each point is placed at equal distance from one another. Interval data always appears in the form of numbers or numerical values where the distance between the two points is standardized and equal.
    Eg: temperature (Farenheit), temperature (Celcius), pH, SAT score (200-800), credit score (300-850)

4. **Ratio data**

    Ratio data is a form of quantitative (numeric) data. It measures variables on a continuous scale, with an equal distance between adjacent values.


### MEASURE OF CENTRAL TENDENCY

It identifies the central position of the data set

1. **Mean:**
	The mean is the average or the most common value in a collection of numbers.

2. **Median:**
	The middle number; found by ordering all data points and picking out the one in the middle (or if there are two middle numbers, taking the mean of those two numbers). 
3. **Mode:**
	The most repeated value from the population.

### MEASURES OF DESPERSION

It is a measure of spread of data about the mean.

1. **Range:**
	The simplest method to measure the despersion, by removing minimum value from the maximum value of the population.
	
	Range = Y<sub>max</sub> - Y<sub>min</sub>

2. **Quartile deviation:**
	It is known as semi-interquartile range, i.e., half of the difference between the upper quartile and lower quartile.

	Q = 1/2 $\times$ ( Q3 - Q1 )

3. **Mean deviation:**
	Mean deviation is the arithmetic mean (average) of deviations ⎜D⎜of observations from a central value (mean or median).

	A = $1 \over n$ $\sum$ |x<sub>i</sub> - $\mu$|

4. **Standard Deviation:**
	The square root of the arithmetic average of the square of the deviations measured from the mean. 
	
	$\sigma=\sqrt{\sum(y_i-\bar y)\over n}$ = $\sqrt{\sum{y_i \over{n}}- \bar y^2}$ 

## RANDOM VARIABLE

A numerical value assigned to the outcomes of a random experiment is called random variable. For example, in tossing two coins we get 4 possible outcomes, but to we cannot use the values in mathematical equations. So for better understanding we assign a numeric value to each of the outcome of the even based on a condition.
<!--
TODO
-->


# SAMPLING
In any kind of survey, working with the whole population is impractical, so instead we use some statistical sampling techniques to get a sample that can represent the population as much as possible. Sampling is a method that allows researchers to predict information about a population based on results from a subset of the population, without having to investigate every individual. Reducing the number of individuals in a study reduces the cost and workload, and may make it easier to obtain high quality information, but this has to be balanced against having a large enough sample size with enough power to detect a true association.

Types of sampling:

## Probability sampling

#### Simple random sampling

In this sampling method the sampling units are selected from the population in a random manner. There are two types of simple random sampling.

1. Simple random sampling without replacement(SRSWOR):

In this method, when we randomly select a unit from population, it is not replaced back to the population, so the probablity of chosing next element from the population is 1/(N-1), since the previously selected unit is removed from the population.

2. Simple random sampling with replacement(SRSWR):

In this method the probablity of selection of any element from the population is always 1/(N) at every stage.

#### Systematic sampling

Sampling units are selected at regular intervals from teh sampling frame. The intervals are chosen to ensure an adequate sample size. If we need a sample size n from a population of size N, you should select every (N/n)<sup>th</sup> unit for the sample. Systematic sampling is more convenient that simple random sampling, but it may lead to bais in case the data collected has a patter of sorted order or similar.

#### Stratified sampling

The entire heterogenous population is divided into a number of homogenous groups, usually termed asstrata, which differ from one another but each of these gourps is homogenous within itself. Then units are sampled at random from each of these stratum, the sample size in each stratum varies according tothe relative imortance of the stratum in the population. The sample, which is the aggreate of the sampled units of each of the stratum, is termed as stratified sample and the technique of drawing  this sample is known as stratified sampling. Such a sample is by far the best and can safely be considered as representative of the population from which it has been drawn.

#### Cluster Sampling

Our entire population is divided into clusters or sections and then the clusters are randomly selected. All the elements of the cluster are used for sampling. Clusters are identified using details such as age, sex, location etc.

Cluster sampling can be done in following ways:

* Single stage cluster sampling

Entire cluster is selected randomly for sampling.
<p align='center'> <img src='imgs/oneStageClusterSampling.png'>  </p>

* Two stage cluster sampling

Here first we randomly select clusters and then from those selected clusters we randomly select elements for sampling.
<p align='center'> <img src='imgs/twoStageClusterSampling.png'>  </p>


## Non-probablity sampling

It does not rely on randomization. This technique is more reliant on the researcher’s ability to select elements for a sample. Outcome of sampling might be biased and makes difficult for all the elements of population to be part of the sample equally. This type of sampling is also known as non-random sampling.

#### Convenience sampling

Here the samples are selected based on the availability. This method is used when the availability of sample is rare and also costly. So based on the convenience samples are selected.

#### Purposive sampling

This is based on the intention or the purpose of study. Only those elements will be selected from the population which suits the best for the purpose of our study.

#### Quota sampling

This type of sampling depends of some pre-set standard. It selects the representative sample from the population. Proportion of characteristics/ trait in sample should be same as population. Elements are selected until exact proportions of certain types of data is obtained or sufficient data in different categories is collected.

#### snowball sampling

This technique is used in the situations where the population is completely unknown and rare. Therefore we will take the help from the first element which we select for the population and ask him to recommend other elements who will fit the description of the sample needed. So this referral technique goes on, increasing the size of population like a snowball.


<!--source:-->
<!--Gupta SC and VK Kapoor Fundamentals of Mathematical Statistics , [towardsdatascience](https://towardsdatascience.com/sampling-techniques-a4e34111d808), [MATH 417](http://home.iitk.ac.in/~shalab/course1.htm)-->
