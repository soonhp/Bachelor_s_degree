#-*-coding: utf-8


################ 한글로 나오게 하기 
import platform

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
    
#이 장에서는 서울시 구별 CCTV 수를 파악하고, 
#인구 대비 CCTV 비율을 파악해서 순위 비교
#인구 대비 CCTV 평균치를 확인하고 CCTV가 과하게 부족한 구를 확인한다.
#단순한 그래프 표현에서 한 단꼐 더 나아가 경향을 확인하고 
#시각화 하는 기초 확인

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import os
os.chdir('C:/Users/박순혁/Desktop/class/LAB')
CCTV_Seoul = pd.read_excel('CCTV_2015(5).xlsx')
# 구별 인구당 CCTV 비율
CCTV_Seoul['CCTV비율'] = CCTV_Seoul['CCTV'] / CCTV_Seoul['인구수'] * 100
CCTV_Seoul['CCTV비율'].sort_values().plot(kind='barh',  grid=True, figsize=(10,10))
plt.ylabel('구별')
plt.xlabel('인구당 CCTV 갯수')
plt.title('구별 인구당 CCTV 갯수 비')
plt.show()
#구별 면적당 cctv 개수 비율
CCTV_Seoul['면적당cctv비율'].sort_values().plot(kind='barh',grid=True, figsize=(10,10))
plt.ylabel('구별')
plt.xlabel('면적당cctv개수')
plt.title('구별 면적당 CCTV 갯수')
plt.show()
matplotlib auto

# 지역별 범죄 비율 (정규화된 발생 건수로 정렬 )
col1 = [ '살인발생', '강도발생', '강간발생', '절도발생', '폭력발생']
CCTV_Seoul['범죄']=np.sum(CCTV_Seoul[col1],axis=1) / 5 
crime_anal_norm_sort = CCTV_Seoul.sort_values(by='범죄', ascending=False)
plt.figure(figsize = (10,10))
sns.heatmap(crime_anal_norm_sort[col1], annot=True, fmt='f', linewidths=.5,
                       cmap='RdPu')
plt.title('범죄비율 (정규화된 발생 건수로 정렬)')
plt.show()


# 지역별 검거 비율(정규화된 검거의 합으로 정렬)
CCTV_Seoul['강간검거율'] = CCTV_Seoul['강간검거']/CCTV_Seoul['강간발생']*100
CCTV_Seoul['강도검거율'] = CCTV_Seoul['강도검거']/CCTV_Seoul['강도발생']*100
CCTV_Seoul['살인검거율'] = CCTV_Seoul['살인검거']/CCTV_Seoul['살인발생']*100
CCTV_Seoul['절도검거율'] = CCTV_Seoul['절도검거']/CCTV_Seoul['절도발생']*100
CCTV_Seoul['폭력검거율'] = CCTV_Seoul['폭력검거']/CCTV_Seoul['폭력발생']*100

# 지역별 검거 비율
target_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
col2 = [ '살인검거', '강도검거', '강간검거', '절도검거', '폭력검거']
CCTV_Seoul['검거']=np.sum(CCTV_Seoul[col2],axis=1)/5
crime_anal_norm_sort = CCTV_Seoul.sort_values(by='검거', ascending=False)
plt.figure(figsize = (10,10))
sns.heatmap(crime_anal_norm_sort[target_col], annot=True, fmt='f',  linewidths=.5, cmap='RdPu')
plt.title('범죄 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()
# 인구와 CCTV 와 범죄 상관 관계
import seaborn as sns
sns.pairplot(CCTV_Seoul, x_vars=["인구수", "CCTV"], 
             y_vars=['살인발생','절도발생','폭력발생'], kind='reg', size=3)
plt.show()

sns.pairplot(CCTV_Seoul, x_vars=["인구수", "CCTV"], 
             y_vars=['강간발생','강도발생'], kind='reg', size=3)
plt.show()

sns.pairplot(CCTV_Seoul, x_vars=["인구수"], 
             y_vars=["CCTV"], kind='reg', size=3)
plt.show()

# 지역별    범죄 발생
col1 = [ '살인발생', '강도발생', '강간발생', '절도발생', '폭력발생']
CCTV_Seoul['범죄발생수'] = np.sum(CCTV_Seoul[col1], axis=1)
# 지역별    범죄 검거
col2 = [ '살인검거', '강도검거', '강간검거', '절도검거', '폭력검거']
CCTV_Seoul['범죄검거수'] = np.sum(CCTV_Seoul[col2], axis=1) 

sns.pairplot(CCTV_Seoul, vars=["CCTV", "범죄발생수", "범죄검거수"], kind='reg', size=3)
plt.show()
#면적당 cctv비율과 범죄와의 상관관계 파악 그래프(pairplot)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(CCTV_Seoul, vars=['면적당cctv비율','범죄발생률','범죄검거율'],kind='reg',size=3)
plt.show()

#서울시 전체구의 데이터로 상관관계 파악
CCTV_Seoul = pd.read_excel('CCTV_2015(5).xlsx')
CCTV_Seoul=CCTV_Seoul.set_index('구별')
s = CCTV_Seoul.corr()
y= CCTV_Seoul.면적당cctv비율
x= CCTV_Seoul['범죄발생률']
x = sm.add_constant(x)
model2 = sm.OLS(y,x).fit()
model2.summary()

#서울시의 면적당 cctv 비율 top 5 구의 상관관계 파악
CCTV_Seoul = pd.read_excel('CCTV_2015(7).xlsx')
CCTV_Seoul=CCTV_Seoul.set_index('구별')
s = CCTV_Seoul.corr()
y= CCTV_Seoul.면적당cctv비율
x= CCTV_Seoul['범죄발생률']
x = sm.add_constant(x)
model2 = sm.OLS(y,x).fit()
model2.summary()


####################################
#시계열 예측을 통해 16년도 구별 범죄발생률 예측하기

#구로구 16년도 범죄발생률 예측
crime_rate=pd.read_excel('crime_rate.xlsx')
crime_rate=crime_rate.set_index("Unnamed: 0")
t = np.arange(2000,2016)
a=list(crime_rate.loc['구로구'])
df = pd.Series(a, index=t)
plt.plot(df, marker='o')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Year')
plt.ylabel('crime_rate')
plt.title('Crime_Rate_Years')
matplotlib auto
df=pd.DataFrame({'t':t,'a':a})
x = df.t
y = df.a
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.summary()

y_pred = model.predict(x)
x_test = [2016,2017]
x_test = sm.add_constant(x_test)
y_test = model.predict(x_test)
y_test

#금천구 16년도 범죄발생률 예측
t = np.arange(2000,2016)
b=list(crime_rate.loc['금천구'])
df = pd.Series(b, index=t)
plt.plot(df, marker='o')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Year')
plt.ylabel('crime_rate')
plt.title('Crime_Rate_Years')
matplotlib auto
df=pd.DataFrame({'t':t,'b':b})
x = df.t
y = df.b
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.summary()

y_pred = model.predict(x)
x_test = [2016,2017]
x_test = sm.add_constant(x_test)
y_test = model.predict(x_test)
y_test

#동대문구 16년도 범죄발생률 예측
t = np.arange(2000,2016)
c=list(crime_rate.loc['동대문구'])
df = pd.Series(c, index=t)
plt.plot(df, marker='o')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Year')
plt.ylabel('crime_rate')
plt.title('Crime_Rate_Years')
matplotlib auto
df=pd.DataFrame({'t':t,'c':c})
x = df.t
y = df.c
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.summary()

y_pred = model.predict(x)
x_test = [2016,2017]
x_test = sm.add_constant(x_test)
y_test = model.predict(x_test)
y_test

# 양천구 16년도 범죄발생률 예측
t = np.arange(2000,2016)
d=list(crime_rate.loc['양천구'])
df = pd.Series(d, index=t)
plt.plot(df, marker='o')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Year')
plt.ylabel('crime_rate')
plt.title('Crime_Rate_Years')
matplotlib auto
df=pd.DataFrame({'t':t,'d':d})
x = df.t
y = df.d
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.summary()

y_pred = model.predict(x)
x_test = [2016,2017]
x_test = sm.add_constant(x_test)
y_test = model.predict(x_test)
y_test

# 용산구 16년도 범죄발생률 예측
t = np.arange(2000,2016)
e=list(crime_rate.loc['용산구'])
df = pd.Series(e, index=t)
plt.plot(df, marker='o')
plt.grid(axis='y', linestyle='--')
plt.xlabel('Year')
plt.ylabel('crime_rate')
plt.title('Crime_Rate_Years')
matplotlib auto
df=pd.DataFrame({'t':t,'e':e})
x = df.t
y = df.e
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.summary()

y_pred = model.predict(x)
x_test = [2016,2017]
x_test = sm.add_constant(x_test)
y_test = model.predict(x_test)
y_test



#####################################
# 방정식 구하기
CCTV_Seoul=pd.read_excel('CCTV_2015(7).xlsx')
x=CCTV_Seoul[['구별','범죄발생률']]
x=x.set_index('구별')   
Actual_Value=CCTV_Seoul[['구별','면적당cctv비율']]
Actual_Value=Actual_Value.set_index('구별')
y=-6206.0394*x+167.6709
y.rename(columns={'범죄발생률':'면적당cctv비율'},inplace=True)
# 잔차 구하기
residual=Actual_Value-y
residual.rename(columns={'면적당cctv비율':'면적당cctv비율 잔차'},inplace=True)
# 잔차가 작은 동대문구와 금천구의 범죄발생률 -0.001을 줄이기 위해 필요한 면적당 cctv 비율 값 구하기
x_proposal=x.loc[['동대문구','금천구']]
x_proposal=x_proposal-0.001
y_proposal=-6206.0394*x_proposal+167.6709
y_proposal.rename(columns={'범죄발생률':'면적당cctv비율'},inplace=True)

# 면적당 cctv비율 x 면적 값을 통해 cctv 개수 구하기
CCTV_Seoul=CCTV_Seoul.set_index('구별')   
y=CCTV_Seoul.loc[['동대문구','금천구'],['면적']]
y_proposal.rename(columns={'면적당cctv비율':'면적'},inplace=True)
cctv_proposal=y_proposal*y
cctv_proposal.rename(columns={'면적':'CCTV'},inplace=True)
# cctv개수가 기존보다 몇 대가 더 필요한지 값을 통해 범죄발생률 0.001을 낮추기 위해 설치할 cctv 수 제안
preexistence_cctv=CCTV_Seoul.loc[['동대문구','금천구'],['CCTV']]
CCTV_proposal=cctv_proposal-preexistence_cctv






