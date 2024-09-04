| Distribution | Original Parameter | Natural Parameter (θ) | Link Function | Inverse Link (Mean Function) |
|--------------|---------------------|------------------------|---------------|------------------------------|
| Normal (Gaussian) | μ (mean) | μ | Identity: g(μ) = μ | g⁻¹(η) = η |
| Bernoulli | p (probability) | log(p / (1-p)) | Logit: g(p) = log(p / (1-p)) | g⁻¹(η) = exp(η) / (1 + exp(η)) |
| Binomial | p (probability) | log(p / (1-p)) | Logit: g(p) = log(p / (1-p)) | g⁻¹(η) = exp(η) / (1 + exp(η)) |
| Poisson | λ (rate) | log(λ) | Log: g(λ) = log(λ) | g⁻¹(η) = exp(η) |
| Exponential | λ (rate) | -λ | Negative Reciprocal: g(λ) = -1/λ | g⁻¹(η) = -1/η |
| Gamma | μ (mean) | -1/μ | Reciprocal: g(μ) = 1/μ | g⁻¹(η) = 1/η |
| Inverse Gaussian | μ (mean) | -1/(2μ²) | Inverse Square: g(μ) = 1/μ² | g⁻¹(η) = η^(-1/2) |
| Negative Binomial | p (probability) | log(p) | Log: g(p) = log(p) | g⁻¹(η) = exp(η) |





| Name of the distribution | PDF expression | Kullback-Leibler divergence | MLE | Source parameters | Natural Parameters | Expectation parameters | Log normalizer | Gradient Log normalizer | G | Gradient G | Sufficient statistics and carrier measure |
|--------------------------|-----------------|------------------------------|-----|-------------------|---------------------|------------------------|----------------|-------------------------|---|------------|-------------------------------------------|
| Normal (Gaussian) | $f(x;\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $D_{KL}(P\|Q) = \log\frac{\sigma_2}{\sigma_1} + \frac{\sigma_1^2 + (\mu_1 - \mu_2)^2}{2\sigma_2^2} - \frac{1}{2}$ | $\hat{\mu} = \frac{1}{n}\sum_{i=1}^n x_i$ <br> $\hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \hat{\mu})^2$ | $\mu, \sigma^2$ | $\eta_1 = \frac{\mu}{\sigma^2}, \eta_2 = -\frac{1}{2\sigma^2}$ | $\mathbb{E}[X] = \mu, \mathbb{E}[X^2] = \mu^2 + \sigma^2$ | $A(\eta) = -\frac{\eta_1^2}{4\eta_2} - \frac{1}{2}\log(-2\eta_2)$ | $\nabla A(\eta) = [\frac{\eta_1}{-2\eta_2}, \frac{\eta_1^2}{4\eta_2^2} - \frac{1}{2\eta_2}]$ | $G(\mu, \sigma^2) = \mu^2 + \log(2\pi\sigma^2)$ | $\nabla G(\mu, \sigma^2) = [2\mu, \frac{1}{\sigma^2}]$ | $T(x) = [x, x^2], h(x) = \frac{1}{\sqrt{2\pi}}$ |
| Bernoulli | $f(x;p) = p^x(1-p)^{1-x}$ | $D_{KL}(P\|Q) = p_1\log\frac{p_1}{p_2} + (1-p_1)\log\frac{1-p_1}{1-p_2}$ | $\hat{p} = \frac{1}{n}\sum_{i=1}^n x_i$ | $p$ | $\eta = \log\frac{p}{1-p}$ | $\mathbb{E}[X] = p$ | $A(\eta) = \log(1 + e^\eta)$ | $A'(\eta) = \frac{e^\eta}{1 + e^\eta}$ | $G(p) = -p\log p - (1-p)\log(1-p)$ | $G'(p) = \log\frac{1-p}{p}$ | $T(x) = x, h(x) = 1$ |
| Binomial | $f(x;n,p) = \binom{n}{x}p^x(1-p)^{n-x}$ | $D_{KL}(P\|Q) = n(p_1\log\frac{p_1}{p_2} + (1-p_1)\log\frac{1-p_1}{1-p_2})$ | $\hat{p} = \frac{1}{n}\sum_{i=1}^n \frac{x_i}{n}$ | $n, p$ | $\eta = \log\frac{p}{1-p}$ | $\mathbb{E}[X] = np$ | $A(\eta) = n\log(1 + e^\eta)$ | $A'(\eta) = \frac{ne^\eta}{1 + e^\eta}$ | $G(p) = -np\log p - n(1-p)\log(1-p)$ | $G'(p) = n\log\frac{1-p}{p}$ | $T(x) = x, h(x) = \binom{n}{x}$ |
| Exponential | $f(x;\lambda) = \lambda e^{-\lambda x}$ | $D_{KL}(P\|Q) = \log\frac{\lambda_2}{\lambda_1} + \frac{\lambda_1}{\lambda_2} - 1$ | $\hat{\lambda} = \frac{n}{\sum_{i=1}^n x_i}$ | $\lambda$ | $\eta = -\lambda$ | $\mathbb{E}[X] = \frac{1}{\lambda}$ | $A(\eta) = -\log(-\eta)$ | $A'(\eta) = -\frac{1}{\eta}$ | $G(\lambda) = -\log\lambda$ | $G'(\lambda) = -\frac{1}{\lambda}$ | $T(x) = x, h(x) = 1$ |
| Geometric | $f(x;p) = p(1-p)^x$ | $D_{KL}(P\|Q) = \log\frac{1-p_2}{1-p_1} - \frac{p_1}{1-p_1}\log\frac{p_1(1-p_2)}{p_2(1-p_1)}$ | $\hat{p} = \frac{n}{\sum_{i=1}^n x_i + n}$ | $p$ | $\eta = \log(1-p)$ | $\mathbb{E}[X] = \frac{1-p}{p}$ | $A(\eta) = -\log(-\eta)$ | $A'(\eta) = -\frac{1}{\eta}$ | $G(p) = -\log p - \frac{1-p}{p}\log(1-p)$ | $G'(p) = \frac{1}{p^2}\log(1-p) + \frac{1}{p(1-p)}$ | $T(x) = x, h(x) = 1$ |
| Poisson | $f(x;\lambda) = \frac{\lambda^x e^{-\lambda}}{x!}$ | $D_{KL}(P\|Q) = \lambda_1\log\frac{\lambda_1}{\lambda_2} - (\lambda_1 - \lambda_2)$ | $\hat{\lambda} = \frac{1}{n}\sum_{i=1}^n x_i$ | $\lambda$ | $\eta = \log\lambda$ | $\mathbb{E}[X] = \lambda$ | $A(\eta) = e^\eta$ | $A'(\eta) = e^\eta$ | $G(\lambda) = \lambda\log\lambda - \lambda$ | $G'(\lambda) = \log\lambda$ | $T(x) = x, h(x) = \frac{1}{x!}$ |
| Negative Binomial | $f(x;r,p) = \binom{x+r-1}{x}p^r(1-p)^x$ | Complex | $\hat{p} = \frac{nr}{\sum_{i=1}^n x_i}$ | $r, p$ | $\eta_1 = \log p, \eta_2 = \log(1-p)$ | $\mathbb{E}[X] = \frac{r(1-p)}{p}$ | $A(\eta) = -r\log(1-e^{\eta_1-\eta_2})$ | Complex | $G(p) = -r\log p - \frac{r(1-p)}{p}\log(1-p)$ | Complex | $T(x) = x, h(x) = \binom{x+r-1}{x}$ |
| Pareto | $f(x;k,\alpha) = \frac{\alpha k^\alpha}{x^{\alpha+1}}$ | Complex | $\hat{\alpha} = \frac{n}{\sum_{i=1}^n \log(\frac{x_i}{k})}$ | $k, \alpha$ | $\eta = -(\alpha+1)$ | $\mathbb{E}[X] = \frac{\alpha k}{\alpha-1}$ for $\alpha > 1$ | $A(\eta) = \log(\frac{k^{-\eta}}{-\eta-1})$ | $A'(\eta) = -\frac{\log k}{\eta+1} + \frac{1}{(\eta+1)^2}$ | $G(\alpha) = \log k + \frac{1}{\alpha} + \log\alpha$ | $G'(\alpha) = -\frac{1}{\alpha^2} + \frac{1}{\alpha}$ | $T(x) = \log x, h(x) = \frac{1}{x}$ |
| **Weibull**                  | $f(x \| \lambda, k) = \frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x/\lambda)^k}$           | N/A                                                                                                                                       | $\hat{k}, \hat{\lambda}$ (using numerical methods)   | $(\lambda, k)$                  | $-\frac{k}{\lambda^k}$                        | $\lambda \Gamma(1 + 1/k)$                 | $\log Z(\eta) = -\eta^{1/k}$                 | $-\frac{1}{k}\eta^{1/k - 1}$                | $G(\theta) = \lambda \Gamma(1 + 1/k)$       | $\frac{1}{k}\Gamma(1 + 1/k)$            | $T(x) = x^k$ (Sufficient statistics); $x^{k-1}$ (Carrier measure) |
| **Laplace**                  | $f(x \| \mu, b) = \frac{1}{2b} \exp\left(-\frac{\|x-\mu\|}{b}\right)$                                      | N/A                                                                                                                                       | $\hat{\mu} = \text{median}(x), \ \hat{b} = \frac{1}{n} \sum_{i=1}^{n} \|x_i - \hat{\mu}\|$ | $(\mu, b)$                      | $-\frac{1}{b}$                               | $\mu + b \log 2$                            | $-\frac{1}{b}$                               | $G(\theta) = \mu$                           | $b$                                    | $T(x) = \|x - \mu\|$ (Sufficient statistics); $1$ (Carrier measure) |
| **Log Normal**               | $f(x \| \mu, \sigma^2) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\left(-\frac{(\log x - \mu)^2}{2\sigma^2}\right)$ | N/A                                                                                                                                       | $\hat{\mu} = \frac{1}{n}\sum_{i=1}^{n} \log x_i, \ \hat{\sigma^2} = \frac{1}{n}\sum_{i=1}^{n} (\log x_i - \hat{\mu})^2$ | $(\mu, \sigma^2)$              | $\mu, -\frac{1}{2\sigma^2}$                   | $e^{\mu + \sigma^2/2}$                     | $\log Z(\eta) = \frac{1}{2\sigma^2} + \mu$   | $-\frac{1}{\sigma^2}$                     | $G(\theta) = \log \mu$                      | $\frac{1}{\mu}$                         | $T(x) = \log x$ (Sufficient statistics); $1/x$ (Carrier measure) |
| **Inverse Gaussian**         | $f(x \| \mu, \lambda) = \left(\frac{\lambda}{2\pi x^3}\right)^{1/2} \exp\left(-\frac{\lambda (x-\mu)^2}{2\mu^2 x}\right)$ | N/A                                                                                                                                       | $\hat{\mu} = \frac{\sum_{i=1}^{n} x_i}{n}, \ \hat{\lambda} = \frac{n}{\sum_{i=1}^{n} \frac{(x_i - \mu)^2}{\mu^2 x_i}}$ | $(\mu, \lambda)$               | $(\lambda/\mu^2, -\lambda/2\mu^2)$            | $\mu$                                      | $\log Z(\eta) = \eta - \frac{1}{2\lambda}$    | $\lambda/\eta$                              | $G(\theta) = \frac{\theta^2}{2\lambda}$     | $\theta/\lambda$                        | $T(x) = (x, x^{-1})$ (Sufficient statistics); $x^{-3/2}$ (Carrier measure) |
| **Gamma**                    | $f(x \| \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$                    | $\text{KL}(p \| q) = (\alpha_p - \alpha_q) \psi(\alpha_p) - \log\frac{\Gamma(\alpha_p)}{\Gamma(\alpha_q)} + \alpha_q (\log\beta_q - \log\beta_p) + \alpha_p (\beta_p/\beta_q - 1)$ | $\hat{\alpha} = \text{solve numerically}, \ \hat{\beta} = \frac{\alpha}{\bar{x}}$ | $(\alpha, \beta)$             | $(\alpha - 1, -\beta)$                         | $\alpha/\beta$                              | $\log Z(\eta) = -\alpha\log(-\eta_2) + \eta_2 \eta_1$ | $\alpha/\eta_2$                             | $G(\theta) = \alpha \theta - \log(\theta)$   | $\alpha/\theta - \frac{1}{\theta}$      | $T(x) = (x, \log x)$ (Sufficient statistics); $1$ (Carrier measure) |
| **Chi-Squared**              | $f(x \| k) = \frac{1}{2^{k/2} \Gamma(k/2)} x^{k/2 - 1} e^{-x/2}$                                         | N/A                                                                                                                                       | $\hat{k} = \frac{1}{n}\sum_{i=1}^{n} x_i$           | $k$                            | $k/2 - 1$                                      | $k$                                         | $\log Z(\eta) = \frac{k}{2} \log(2) + \log\Gamma(k/2)$ | $k/2$                                      | $G(\theta) = k \log(\theta) - \frac{k}{\theta}$ | $k/\theta - \frac{k}{\theta}$          | $T(x) = x$ (Sufficient statistics); $x^{k/2 - 1}$ (Carrier measure) |
| **Beta**                     | $f(x \| \alpha, \beta) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{B(\alpha,\beta)}$                            | $\text{KL}(p \| q) = \log\frac{B(\alpha_q, \beta_q)}{B(\alpha_p, \beta_p)} - (\alpha_p - \alpha_q) \psi(\alpha_p) - (\beta_p - \beta_q) \psi(\beta_p) + (\alpha_p + \beta_p - \alpha_q - \beta_q) \psi(\alpha_p + \beta_p)$ | $\hat{\alpha} = \text{solve numerically}, \ \hat{\beta} = \text{solve numerically}$ | $(\alpha, \beta)$             | $(\alpha - 1, \beta - 1)$                      | $(\alpha/(\alpha+\beta), \beta/(\alpha+\beta))$ | $\log Z(\eta) = \log\Gamma(\alpha) + \log\Gamma(\beta) - \log\Gamma(\alpha+\beta)$ | $\psi(\alpha) - \psi(\alpha+\beta)$          | $G(\theta) = \log(\Gamma(\theta)) - \frac{\theta}{\Gamma(\theta)}$ | $\theta/\Gamma(\theta)$              | $T(x) = (x, \log(1-x))$ (Sufficient statistics); $x^{\alpha-1}(1-x)^{\beta-1}$ (Carrier measure) |
| **Beta**                     | $f(x \| \alpha, \beta) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{B(\alpha,\beta)}$                            | $\text{KL}(p \| q) = \log\frac{B(\alpha_q, \beta_q)}{B(\alpha_p, \beta_p)} - (\alpha_p - \alpha_q) \psi(\alpha_p) - (\beta_p - \beta_q) \psi(\beta_p) + (\alpha_p + \beta_p - \alpha_q - \beta_q) \psi(\alpha_p + \beta_p)$ | $\hat{\alpha} = \text{solve numerically}, \ \hat{\beta} = \text{solve numerically}$ | $(\alpha, \beta)$             | $(\alpha - 1, \beta - 1)$                      | $(\alpha/(\alpha+\beta), \beta/(\alpha+\beta))$ | $\log Z(\eta) = \log\Gamma(\alpha) + \log\Gamma(\beta) - \log\Gamma(\alpha+\beta)$ | $\psi(\alpha) - \psi(\alpha+\beta)$          | $G(\theta) = \log(\Gamma(\theta)) - \frac{\theta}{\Gamma(\theta)}$ | $\theta/\Gamma(\theta)$              | $T(x) = (x, \log(1-x))$ (Sufficient statistics); $x^{\alpha-1}(1-x)^{\beta-1}$ (Carrier measure) |
| **Dirichlet**                | $f(x \| \alpha) = \frac{\Gamma(\sum_{i=1}^{K} \alpha_i)}{\prod_{i=1}^{K} \Gamma(\alpha_i)} \prod_{i=1}^{K} x_i^{\alpha_i - 1}$ | N/A                                                                                                                                       | $\hat{\alpha_i} = \text{solve numerically}$         | $\alpha$                        | $(\alpha_i - 1)$                              | $\alpha_i/\sum_{i=1}^{K} \alpha_i$          | $\log Z(\eta) = \sum_{i=1}^{K} \log\Gamma(\alpha_i) - \log\Gamma(\sum_{i=1}^{K} \alpha_i)$ | $\psi(\alpha_i) - \psi(\sum_{i=1}^{K} \alpha_i)$ | $G(\theta) = \sum_{i=1}^{K} \log\Gamma(\theta_i)$ | $\psi(\alpha_i) - \psi(\sum_{i=1}^{K} \alpha_i)$ | $T(x) = (\log x_1, \ldots, \log x_K)$ (Sufficient statistics); $\prod_{i=1}^{K} x_i^{\alpha_i - 1}$ (Carrier measure) |
| **Categorical**              | $f(x \| p) = \prod_{i=1}^{K} p_i^{x_i}$                                                                 | $\text{KL}(p \| q) = \sum_{i=1}^{K} p_i \log\frac{p_i}{q_i}$                                                                               | $\hat{p}_i = \frac{n_i}{n}$                          | $p$                            | $\log(p)$                                    | $p_i$                                       | $\log Z(\eta) = \log\left(\sum_{i=1}^{K} e^{\eta_i}\right)$ | $\frac{e^{\eta_i}}{\sum_{i=1}^{K} e^{\eta_i}}$ | $G(\theta) = \sum_{i=1}^{K} p_i \log p_i$ | $p_i \log p_i + (1-p_i) \log (1-p_i)$ | $T(x) = x$ (Sufficient statistics); $1$ (Carrier measure) |
| **Wishart**                  | $f(X \| V, n) = \frac{\|X\|^{(n-d-1)/2} \exp(-\frac{1}{2} \text{tr}(V^{-1}X))}{2^{nd/2} \|V\|^{n/2} \Gamma_d(n/2)}$ | N/A                                                                                                                                       | $\hat{V} = \frac{1}{n} \sum_{i=1}^{n} X_i$           | $(V, n)$                       | $-\frac{1}{2} V^{-1}$                         | $V$                                         | $\log Z(\eta) = \frac{n}{2} \log \|V\| + \frac{d(d-1)}{4} \log \pi + \sum_{i=1}^{d} \log \Gamma\left(\frac{n+1-i}{2}\right)$ | $-\frac{1}{2} V^{-1}$                         | $G(\theta) = \frac{1}{2} \text{tr}(V^{-1} \theta)$ | $-\frac{1}{2} V^{-1}$                 | $T(X) = X$ (Sufficient statistics); $|X|^{(n-d-1)/2}$ (Carrier measure) |
| **Inverse Wishart**          | $f(X \| \Psi,\nu) = \frac{\|\Psi\|^{\nu/2}}{2^{\nu d/2} \Gamma_d(\nu/2)} \|\Psi^{-1} X^{-1}\|^{(\nu+d+1)/2} \exp\left(-\frac{1}{2} \text{tr}(\Psi X^{-1})\right)$ | N/A                                                                                                                                       | $\hat{\Psi} = \frac{1}{n} \sum_{i=1}^{n} X_i^{-1}, \ \hat{\nu} = n$ | $(\Psi, \nu)$               | $-\frac{1}{2} (\nu + d + 1) \Psi^{-1}$         | $\Psi$                                      | $\log Z(\eta) = \frac{(\nu + d + 1)}{2} \log\|\eta^{-1}\| + \frac{1}{2} \text{tr}(\Psi \eta^{-1})$ | $-\frac{1}{2} (\nu + d + 1)\Psi^{-1}$         | $G(\theta) = \frac{(\nu + d + 1)}{2} \log\|\theta^{-1}\|$ | $\Psi^{-1}$                            | $T(X) = X^{-1}$ (Sufficient statistics); $|\Psi^{-1} X^{-1}|^{(\nu+d+1)/2}$ (Carrier measure) |