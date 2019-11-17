b<-women
b
plot(b$height,b$weight)
cor(b$height,b$weight) [1] 0.9954948
b_lm=lm(weight~height,data=b) 或 b_lm=lm(b$weight~b$height)
summary(b_lm)
plot(b)
plot(b$height,b$weight)
abline(b_lm,col = "red",lwd=2)



b_lm2=lm(weight~height+I(height^2),data=women)


------数据读取----------
library(readxl)
hit_rate<-read_excel("~/工作/培训/相关与回归分析/样本题目/hit_rate.xlsx")
------查看数据集-------------
head(hit_rate)
plot(hit_rate$hit_rate_pv,hit_rate$`7d_active_rate`)
-------清洗数据-----------
hit_rate[which(hit_rate$`7d_active_rate`==0),]
hit_rate=hit_rate[-which(hit_rate$`7d_active_rate`==0),]
plot(hit_rate$hit_rate_pv,hit_rate$`7d_active_rate`)
------建立回归----------
hist(hit_rate$`7d_active_rate`)
hist(hit_rate$hit_rate_pv)-------验证正态分布
cor(hit_rate$`7d_active_rate`,hit_rate$hit_rate_pv)-------相关系数
hit_rate_lm=lm(hit_rate$`7d_active_rate`~hit_rate$hit_rate_pv)-------建立回归模型
summary(hit_rate_lm)
plot(hit_rate$hit_rate_pv,hit_rate$`7d_active_rate`)
abline(hit_rate_lm,col='red')



hit_rate2<-read_excel("~/工作/培训/相关与回归分析/样本题目/hit_rate2.xlsx")
cor(hit_rate2[,c(1,2,8)])
hit_rate2_lm=lm(hit_rate2$`7d_active_rate`~hit_rate2$show_pv+hit_rate2$clcik_pv)
summary(hit_rate2_lm)
plot(hit_rate2_lm)



hit_rate2$show_pv=as.factor(hit_rate2$show_pv)
hit_rate2_lm2=lm(hit_rate2$`7d_active_rate`~hit_rate2$show_pv+hit_rate2$clcik_pv)
summary(hit_rate2_lm2)



plot(live_rate)


live_rate_lm=lm(live_rate~.,data=live_rate)
summary(live_rate_lm)


live_rate_lm2=lm(live_rate~pages,data=live_rate)
summary(live_rate_lm2)
live_rate_lm3=lm(live_rate~duration,data=live_rate)
summary(live_rate_lm3)


cement=data.frame(
	X1=c(7,1,11,11,7,11,3,1,2,21,1,11,10),
  X2=c(26,29,56,31,52,55,71,31,54,47,40,66,68),
  X3=c(6,15,8,8,6,9,17,22,18,4,23,9,8),
  X4=c(60,52,20,47,33,22,6,44,22,26,34,12,12),
  Y=c(78.5,74.3,104.3,87.6,95.9,109.2,102.7,72.5,93.1,115.9,83.8,113.3,109.4)
	)
lm.sol=lm(Y~.,data=cement)
summary(lm.sol)


lm.sol=lm(Y~X1+X2,data=cement)
summary(lm.sol)



x=seq(-10,10,0.001)
y=1/(1+exp(1)^(-x))
plot(x,y,type='l',lwd=2)
abline(v=0,col="red")
abline(h=0.5,col="red")


library(readxl)
live_rate2 <- read_excel("工作/培训/相关与回归分析/样本题目/live_rate2.xlsx",col_types = c("numeric", "numeric", "numeric"))
live_rate2_lm=glm(live_rate~duration,data=live_rate2)
summary(live_rate2_lm)
library(car)
Anova(live_rate2_lm)
predict(live_rate2_lm, type='response')
pre=ifelse(predict(live_rate2_lm, type='response')>0.5,1,0)
live_rate2_glm=cbind(live_rate2,pre)
write_csv(cbind(test,pre),'log_pre.csv')


titanic_train_lm=glm(Survived~Pclass+Sex+Age+SibSp+Parch+Fare+Embarked,family=binomial(link='logit'),data=titanic_train2)
titanic_train2_lm=glm(Survived~Pclass+Sex+Age+SibSp,family=binomial(link='logit'),data=titanic_train2)
summary(titanic_train2_lm)
library(car)
Anova(titanic_train2_lm)
predict(titanic_train2_lm, newdata = test,type='response')
pre=ifelse(predict(titanic_train2_lm, newdata = test,type='response')>0.5,1,0)
cbind(test,pre)
write.csv(cbind(test,pre),'titian_pre.csv')