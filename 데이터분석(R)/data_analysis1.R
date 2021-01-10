radio <- read.table("C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제2/Table1_7.txt")
colnames(radio) = c("Symptoms", "Activity", "Sleep", "Eat", "Appetite", "Skin_reaction")
head(radio)
cor(radio)
summary(radio)


radio_pca1 <- princomp(x = radio)
print(summary(radio_pca1), loadings = TRUE)

radio_pca2 <- princomp(x = radio, cor=T) #COR=T 표준화
print(summary(radio_pca2), loadings = TRUE)

women <- read.table("C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제2/Table1_9.txt")
colnames(women) = c("Country", "100m", "200m", "400m", "800m","1500m", "3000m", "Marathon")

women_pca2 <- princomp(x = women[,-1] ,cor=T)
print(summary(women_pca2), loadings = TRUE)
women_pca2$scores[,1]


row.names(women)<- women[,1]
cor(women[,-1])
women2<-as.matrix(cor(women[,-1]))
eigen(women2)
women1<-women[,-1]
women_pca <- prcomp(women[, -1], scale = TRUE)
summary(women_pca)
print(women_pca$rotation)


women3<-women_pca$x[,1]
w2<-cbind(women_pca$x[,1])
w2[order(w2[,1]),]


#첫번째 주성분과 두번째 주성분과의 산점도(상관관계 및 이상치)
library(MVA)
plot(women_pca$x[,1:2], type = "n")
text(women_pca$x[,1:2], 
     abbreviate(row.names(women)))
bvbox(women_pca$x[,1:2], add=TRUE)

class(women[,-1])
poldist<-dist(women[,-1])

pol.mds<-cmdscale(poldist, k=49, eig=TRUE)
pol.mds
ev <- pol.mds$eig
cumsum(abs(ev)) / sum(abs(ev))
cumsum(ev^2) / sum(ev^2) 

pol.mds<-cmdscale(poldist, k=2, eig=TRUE)

x <- pol.mds$points
plot(x[,1], x[,2], type = "n")
text(x[,1], x[,2], labels = rownames(x), cex = 0.7)




psych <- read.table("C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제2/psychiatric.txt")
colnames(psych) = c("ID", "figure", "problem", "tools", "vocaburary", "sex")
head(psych)

psych_s <- psych[,-c(1,6)]
psych_pca = prcomp(psych_s)
summary(psych_pca)
print(psych_pca$rotation)
library(dplyr)
psych_m <- psych %>% 
  filter(sex == 1)
psych_m <- psych_m[,-c(1,6)]
psych_m
psych_m_pca = prcomp(psych_m)
summary(psych_m_pca)
print(psych_m_pca$rotation)


psych_w <- psych %>% 
  filter(sex == 2)
psych_w <- psych_w[,-c(1,6)]
psych_w
psych_w_pca = prcomp(psych_w)
summary(psych_w_pca)
print(psych_w_pca$rotation)


UShealth <- read.table("C:/Users/박순혁/Desktop/class/2020-1/dataanalysis/과제2/US_health.txt")
colnames(UShealth) = c("state", "land", "popu", "acc", "card",
                       "can", "pul", "pnue", "diab", "liv",  
                       "doc", "hosp", "r", "d")
head(UShealth)
row.names(UShealth)<-UShealth[,1]
View(UShealth)
UShealth_s<-UShealth[,-c(1,2,3,11,12,13,14)]
dim(UShealth)

class(UShealth_s)
poldist<-dist(UShealth_s)

pol.mds<-cmdscale(poldist, k=49, eig=TRUE)
pol.mds
ev <- pol.mds$eig
cumsum(abs(ev)) / sum(abs(ev))
cumsum(ev^2) / sum(ev^2) 

pol.mds<-cmdscale(poldist, k=2, eig=TRUE)

x <- pol.mds$points
plot(x[,1], x[,2], type = "n")
text(x[,1], x[,2], labels = rownames(x), cex = 0.7)

stars(UShealth_s, draw.segments = TRUE, key.loc = c(15,2))
