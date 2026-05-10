---
tags: [reference, math]
created: 2026-01-03T11:00:00
modified: 2026-01-11T14:00:00
---

# Statistics Basics

Core statistical concepts for ML research.

## Descriptive Statistics

- **Mean**: Average value. Sensitive to outliers.
- **Median**: Middle value. Robust to outliers.
- **Standard Deviation**: Spread around the mean.

## Hypothesis Testing

- Null hypothesis (H0) vs alternative hypothesis (H1)
- p-values: probability of observing data as extreme as the result, assuming H0 is true
- Significance level (alpha): typically 0.05

## Confidence Intervals

A 95% confidence interval means: if we repeated the experiment many times, 95% of intervals would contain the true parameter.

## Regression

- Linear regression: y = mx + b, minimized via gradient descent or normal equations
- The gradient descent update rule: w = w - lr * dL/dw
- Always check residuals for normality and homoscedasticity
