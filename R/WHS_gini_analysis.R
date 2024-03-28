> data <- read.csv("~/Desktop/Data Analyst/Git/world-happiness-analysis/data/WHR_2019_Full.csv")
> reg_model <- lm(Score ~ Gini.index, data = data)
> summary(reg_model)

Call:
lm(formula = Score ~ Gini.index, data = data)

Residuals:
Min 1Q Median 3Q Max
-2.53965 -0.69915 -0.01688 0.79610 2.04717

Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) 7.38486 0.59328 12.447 < 2e-16 ***
Gini.index -0.04699 0.01625 -2.893 0.00473 **
---
Signif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.091 on 96 degrees of freedom
(58 observations deleted due to missingness)
Multiple R-squared: 0.08017, Adjusted R-squared: 0.07059
F-statistic: 8.367 on 1 and 96 DF, p-value: 0.004727