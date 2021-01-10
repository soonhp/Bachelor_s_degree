#과제 3

mba <- read.csv(file="C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제3/mba_car.csv")
dim(mba)

table(mba[,2])
mba_fa_score <- factanal(mba[,3:18], factors=3, scores="regression")    #0.05보다 크므로 인자의 수 6개로
mba_fa_score
score <- cbind(mba[,2], mba_fa_score$scores)
head(score)
score
dim(score)
score.array <- array(rep(0, 30), dim=c(10, 3))
score.array
for(i in 1:10){
  score.array[i, 1] = mean(subset(score, score[,1] == i)[,2])
  score.array[i, 2] = mean(subset(score, score[,1] == i)[,3])
  score.array[i, 3] = mean(subset(score, score[,1] == i)[,4])
}
score.array <- na.omit(score.array)
dim(score.array)
score.array

rownames(score.array) = c("BMW 328i", "Ford Explorer", "Infinity J30", "Jeep Grand Cherokee","Lexus ES300","Chrysler Town & Country","Mercedes C280","Saab 9000","Porsche Boxster","Volvo V90")
score.array


plot(score.array[,1], score.array[,3], xlab = "appealing", ylab="off-road", pch="")
text(score.array[,1], score.array[,3], labels=rownames(score.array))


psy <- read.csv(file="C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제3/psych_test.csv")
head(psy)
op <- options(digits=3)
psy.cor <- cov2cor(psy.cov$cov)
psy.cor
ability.cov$cov
ability.cov$n.obs
n.ability


f1 <- factanal(covmat = psy, factors = 3, n.obs = 145, method = "mle")


a<-c(0.318,
      0.436, 0.419, 
      0.335, 0.234, 0.323, 
      0.304, 0.157, 0.283, 0.722, 
      0.326, 0.195, 0.350, 0.714, 0.685, 
      0.116, 0.057, 0.056, 0.203, 0.246, 0.170, 
      0.314, 0.145, 0.229, 0.095, 0.181, 0.113, 0.585, 
      0.489, 0.239, 0.361, 0.309, 0.345, 0.280, 0.408, 0.512 )
psy <- diag(9) / 2
psy[upper.tri(psy)] <- a
psy <- psy + t(psy)  
rownames(psy) <- colnames(psy) <- 
  c("Vis","Cub","Loz","Par","Sen","Wor","Add","Cou","Str")
f1 <- factanal(covmat = psy, factors = 1, method = "mle", n.obs = 145)
f2 <- factanal(covmat = psy, factors = 2, method = "mle", n.obs = 145)
f3 <- factanal(covmat = psy, factors = 3, method = "mle", n.obs = 145)


six <- read.csv(file="C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제3/six_variables.csv")
six_fa1 <-factanal(six, factors=1, rotation="none")
six_fa1
six_fa2 <-factanal(six, factors=2, rotation="none")
six_fa3 <-factanal(six, factors=3, rotation="none")
