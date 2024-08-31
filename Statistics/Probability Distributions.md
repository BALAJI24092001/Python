
# Comprehensive Table of Probability Distributions



| Distribution | Type | PDF/PMF | CDF | Parameters | Usage |
|--------------:|:------:|:---------:|:-----|------------|-------|
| 1. Bernoulli | Discrete | $P(X=1) = p, P(X=0) = 1-p$ | $F(x) = 0  if x < 0  1-p  if 0 \le x < 1  1 & if  x \ge 1$ | $p \in [0,1]$ | Models binary outcomes (success/failure) |
| 2. Binomial | Discrete | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $F(x) = \sum_{k=0}^{\lfloor x \rfloor} \binom{n}{k} p^k (1-p)^{n-k}$ | $n > 0, p \in [0,1]$ | Number of successes in n independent Bernoulli trials |
| 3. Poisson | Discrete | $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | $F(x) = e^{-\lambda} \sum_{k=0}^{\lfloor x \rfloor} \frac{\lambda^k}{k!}$ | $\lambda > 0$ | Models rare events in a fixed interval |
| 4. Geometric | Discrete | $P(X=k) = p(1-p)^{k-1}$ | $F(x) = 1 - (1-p)^{\lfloor x \rfloor}$ | $p \in (0,1]$ | Number of trials until first success |
| 5. Negative Binomial | Discrete | $P(X=k) = \binom{k+r-1}{k} p^r (1-p)^k$ | No closed form | $r > 0, p \in (0,1]$ | Number of failures before r successes |
| 6. Uniform (Discrete) | Discrete | $P(X=k) = \frac{1}{b-a+1}$ | $F(x) = \frac{\lfloor x \rfloor - a + 1}{b - a + 1}$ | $a \leq b$, both integers | Equal probability for all outcomes in range |
| 7. Hypergeometric | Discrete | $P(X=k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$ | No closed form | $N \geq 1, 0 \leq K \leq N, 0 \leq n \leq N$ | Sampling without replacement |
| 8. Normal (Gaussian) | Continuous | $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | No closed form (uses error function) | $\mu \in \mathbb{R}, \sigma > 0$ | Models many natural phenomena |
| 9. Uniform (Continuous) | Continuous | $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$ | $F(x) = \frac{x-a}{b-a}$ for $a \leq x \leq b$ | $a < b$ | Equal probability density over an interval |
| 10. Exponential | Continuous | $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$ | $F(x) = 1 - e^{-\lambda x}$ for $x \geq 0$ | $\lambda > 0$ | Time between events in a Poisson process |
| 11. Gamma | Continuous | $f(x) = \frac{x^{k-1} e^{-x/\theta}}{\theta^k \Gamma(k)}$ | No closed form | $k > 0, \theta > 0$ | Waiting times, rainfall amounts |
| 12. Beta | Continuous | $f(x) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{B(\alpha,\beta)}$ | No closed form | $\alpha > 0, \beta > 0$ | Modeling probabilities, proportions |
| 13. Chi-square | Continuous | $f(x) = \frac{x^{k/2-1} e^{-x/2}}{2^{k/2} \Gamma(k/2)}$ | No closed form | $k > 0$ (integer) | Sum of squares of standard normal variables |
| 14. Student's t | Continuous | $f(x) = \frac{\Gamma(\frac{v+1}{2})}{\sqrt{v\pi} \Gamma(\frac{v}{2})} (1 + \frac{x^2}{v})^{-\frac{v+1}{2}}$ | No closed form | $v > 0$ | Estimating mean of normally distributed population |
| 15. F | Continuous | $f(x) = \frac{\sqrt{\frac{(d_1x)^{d_1} \cdot d_2^{d_2}}{(d_1x + d_2)^{d_1+d_2}}}}{x \cdot B(\frac{d_1}{2}, \frac{d_2}{2})}$ | No closed form | $d_1 > 0, d_2 > 0$ (integers) | Ratio of chi-square distributions, ANOVA |
| 16. Lognormal | Continuous | $f(x) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x-\mu)^2}{2\sigma^2}}$ | No closed form | $\mu \in \mathbb{R}, \sigma > 0$ | Product of many independent positive variables |
| 17. Weibull | Continuous | $f(x) = \frac{k}{\lambda} (\frac{x}{\lambda})^{k-1} e^{-(x/\lambda)^k}$ | $F(x) = 1 - e^{-(x/\lambda)^k}$ | $k > 0, \lambda > 0$ | Reliability analysis, extreme value theory |
| 18. Cauchy | Continuous | $f(x) = \frac{1}{\pi \gamma [1 + (\frac{x-x_0}{\gamma})^2]}$ | $F(x) = \frac{1}{\pi} \arctan(\frac{x-x_0}{\gamma}) + \frac{1}{2}$ | $x_0 \in \mathbb{R}, \gamma > 0$ | Long-tailed distributions, resonance behavior |
| 19. Laplace | Continuous | $f(x) = \frac{1}{2b} e^{-\frac{\|x-\mu\|}{b}}$ | $$F(x) = \begin{cases} \frac{1}{2} e^{\frac{x-\mu}{b}} & \text{if } x < \mu \\ 1 - \frac{1}{2} e^{-\frac{x-\mu}{b}} & \text{if } x \geq \mu \end{cases}$$ | $\mu \in \mathbb{R}, b > 0$ | Double exponential distribution |
| 20. Pareto | Continuous | $f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}$ | $F(x) = 1 - (\frac{x_m}{x})^\alpha$ | $x_m > 0, \alpha > 0$ | Power law probability distributions |
| 21. Logistic | Continuous | $f(x) = \frac{e^{-\frac{x-\mu}{s}}}{s(1 + e^{-\frac{x-\mu}{s}})^2}$ | $F(x) = \frac{1}{1 + e^{-\frac{x-\mu}{s}}}$ | $\mu \in \mathbb{R}, s > 0$ | Growth models, logistic regression |
| 22. Rayleigh | Continuous | $f(x) = \frac{x}{\sigma^2} e^{-\frac{x^2}{2\sigma^2}}$ | $F(x) = 1 - e^{-\frac{x^2}{2\sigma^2}}$ | $\sigma > 0$ | Norms of bivariate normal variables |
| 23. Multinomial | Multivariate Discrete | $P(X_1=x_1,\ldots,X_k=x_k) = \frac{n!}{x_1!\cdots x_k!} p_1^{x_1} \cdots p_k^{x_k}$ | No closed form | $n > 0, \sum p_i = 1$ | Generalization of binomial to multiple categories |
