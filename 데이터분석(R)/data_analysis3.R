cereal <- read.delim("C:/Users/¹Ú¼øÇõ/Desktop/class/2020-1/dataanalysis/°úÁ¦4/T11-9.DAT", header=F, sep="")
colnames(cereal) = c("Brand", "Manufacturer", "Calories", "Protein", "Fat", "Sodium", "Fiber", "Carbohydrates", "Sugar", "Potassium", "Group")
head(cereal)
cereal <- cereal[,2:10]
cereal[,7]=as.numeric(cereal[,7])
str(cereal)


lda.cv <- lda(Country ~ Gender + Freshwater + Marine, data=salmon , CV = TRUE)
lda.cv$class

res <- data.frame(est = lda.cv$class, truth = salmon[,1])
tab <- table(res) ## confusion matrix
tab

1 - sum(diag(tab)) / nrow(salmon)


salmon <- read.delim("C:/Users/¹Ú¼øÇõ/Desktop/class/2020-1/dataanalysis/°úÁ¦4/T11-2.DAT", header=F, sep="")
salmon
colnames(salmon) = c("Country", "Gender", "Freshwater", "Marine")
head(salmon)

trainIdx <- c(1:30, 51:80) ## 40 samples of each class are used as training data
testIdx <- c(31:50, 81:100) ##  10 samples of each class are used as test data

## Fit LDA
lda.fit <- lda(Country ~ Gender + Freshwater + Marine, data = salmon, subset = trainIdx)
ld.pred <- predict(lda.fit, dimen = 2)
ld <- ld.pred$x
head(ld)
ld.pred$class

## Check quality of prediction
df_train <- data.frame(est = ld.pred$class, truth = salmon[trainIdx,"Country"]);df_train
tab <- table(df_train) ## confusion matrix
tab
1 - sum(diag(tab)) / nrow(df_train) ## error rate only 0% -> expect very good predicions

## Predict labels for new observations
lda.pred <- predict(lda.fit, newdata = salmon[testIdx,])## apply to test data
str(lda.pred)
lda.pred$class


## Check quality of prediction
df_test <- data.frame(est = lda.pred$class, truth = salmon[testIdx,"Country"])
tab <- table(df_test) ## confusion matrix
tab
1 - sum(diag(tab)) / nrow(df_test) ## error rate only 0% -> expect very good predicions

x1 <- matrix(c(3,2,4,7,4,6),nrow=3)
x2 <- matrix(c(6,5,4,9,7,8),nrow=3)

sample.mean1 <- apply(x1, 2, mean) 
sample.mean2 <- apply(x2, 2, mean)

n1 <- nrow(x1);n1
n2 <- nrow(x2);n2
n <- n1+n2

S.u <- ((n1-1)*var(x1) + (n2-1)*var(x2))/(n-2)
S.u.inverse <- solve(S.u)

w <- S.u.inverse %*% (sample.mean1-sample.mean2)


lda.1 <- sample.mean1 %*% w
lda.1

lda.2 <- sample.mean2 %*% w
lda.2

cutoff <- (lda.1 + lda.2)/2
cutoff

x0 <- matrix(c(2,7),nrow=1)
x0 %*% w


library(lavaan)
x <- matrix(c(0.77,0.38,0.39,-0.25,0.38,0.65,0.39,-0.32,0.39,
              0.39,0.62,-0.27,-0.25,-0.32,-0.27,6.09),nrow=4)
rownames(x) <- c("D1","D2","D3","SA")
colnames(x) <- c("D1","D2","D3","SA")

result <- '# latent variables
Result =~ NA*D1 + D2 + D3 + SA
# factor variances
Result ~~ 1*Result' 

result.res <- sem(result, sample.cov = x, sample.nobs=6053)
summary(result.res, standardized=TRUE)
lavResiduals(result.res) # ÀÜÂ÷È®ÀÎ(Ç¥ÁØÈ­µÈ(z)ÀÜÂ÷µµ °°ÀÌ³ª¿È)
resid(result.res, type="standardized") #Ç¥ÁØÈ­µÈ ÀÜÂ÷

head(HolzingerSwineford1939)
dim(HolzingerSwineford1939)
hs <- HolzingerSwineford1939[,-c(1:6)]

cor <- cor(hs)

psy <- '# latent variables
 factor1 =~ NA*x1 + x2 + x3
 factor2 =~ NA*x4 + x5 + x6
 factor3 =~ NA*x7 + x8 + x9
# factor variances
 factor1 ~~ 1*factor1 
 factor2 ~~ 1*factor2
 factor3 ~~ 1*factor3
 factor1 ~~ factor2
 factor2 ~~ factor3
 factor1 ~~ factor3'

psy.res <- sem(psy, sample.cov = cor, sample.nobs=301)
summary(psy.res, fit=TRUE)

