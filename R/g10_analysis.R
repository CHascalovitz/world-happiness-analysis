> data <- read.csv("~/Desktop/Data Analyst/Git/world-happiness-analysis/data/WHR_2019_Full.csv")
> g10_countries <- c("The United States", "Japan", "The Netherlands", "The United Kingdom", "France", "Italy", "Canada", "Sweden", "Germany", "Belgium", "Switzerland")
> global_avg <- mean(data$Score)
> g10_data <- subset(data, Country.or.region %in% g10_countries)
> t_test_result <- t.test(g10_data$Score, mu = global_avg)
> print(t_test_result)

One Sample t-test

data: g10_data$Score
t = 9.8007, df = 10, p-value = 1.911e-06
alternative hypothesis: true mean is not equal to 5.407096
95 percent confidence interval:
6.577734 7.266630
sample estimates:
mean of x
6.922182