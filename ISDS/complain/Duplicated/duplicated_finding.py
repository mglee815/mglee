from os import altsep
import pandas as pd
import numpy as np
import pickle as pkl
import sys
import datetime
import matplotlib.pyplot as plt


sys.stdout = open('Duplicated/log/log.txt', 'w')
pd.set_option('display.max_rows', None)

print(f"=============={datetime.datetime.now()}에 생성된 log 입니다===============")

df = pd.read_pickle("Duplicated/sample5data/sample5_df.pkl")

###나이가 -68세부터 2003세까지 다양한 outlier가 있음###
under_0 = df['나이'] < 0
over_100 = df['나이'] > 100
print(f"나이가 0세 이하인 이상치 : {sum(under_0)} 개")
print(f"나이가 100세 이상인 이상치 : {sum(over_100)} 개")
idx = under_0 | over_100
df = df[idx == False]
idx = df.duplicated('본문')
df_duplicated = df[idx]
print(f"중복을 제거하기 전 데이터의 수 (전체의 5%sample) : {len(df)} 개")
print(f"중복 된 민원의 수 : {sum(idx)}개")

gender_count = (df.groupby('성별').count()['제목'])
df_gender = pd.DataFrame()
df_gender['freq'] = gender_count
df_gender['ratio'] = gender_count / sum(gender_count)

age_count = (df.groupby('나이').count()['제목'])
df_age = pd.DataFrame()
df_age['freq'] = age_count
df_age['ratio'] = age_count / sum(age_count)

region_count = (df.groupby('민원발생지').count()['제목'])
df_region = pd.DataFrame()
df_region['freq'] = region_count
df_region['ratio'] = region_count / sum(region_count)

print(f"전체 민원의 5% sample의 성별 비율 : \n {df_gender} \n")
print(f"전체 민원의 5% sample의 나이 비율 : \n {df_age} \n")
print(f"전체 민원의 5% sample의 민원 발생지 : \n {df_region} \n")
print(f"민원 접수 기관과 처리 기관이 같은 경우 : {len(df[df['접수기관'] == df['처리부서']])} ")
print(f"민원 접수 기관과 처리 기관이 디른 경우 : {len(df[df['접수기관'] != df['처리부서']])} ")

print("\n\n ================ ===============================\n\n")


gender_count_d = (df_duplicated.groupby('성별').count()['제목'])
df_gender_d = pd.DataFrame()
df_gender_d['freq'] = gender_count_d
df_gender_d['ratio'] = gender_count_d / sum(gender_count_d)

age_count_d = (df_duplicated.groupby('나이').count()['제목'])
df_age_d = pd.DataFrame()
df_age_d['freq'] = age_count_d
df_age_d['ratio'] = age_count_d / sum(age_count_d)

region_count_d = (df_duplicated.groupby('민원발생지').count()['제목'])
df_region_d = pd.DataFrame()
df_region_d['freq'] = region_count_d
df_region_d['ratio'] = region_count_d / sum(region_count_d)



print(f"중복된 민원의 성별 비율 : \n {df_gender_d} \n")
print(f"중복된 민원의 나이 비율 : \n {df_age_d} \n")
print(f"중복된 민원의 발생지 : \n {df_region_d} \n")
print(f"(중복) 민원 접수 기관과 처리 기관이 같은 경우 : {len(df_duplicated[df_duplicated['접수기관'] == df_duplicated['처리부서']])} ")
print(f"(중복) 민원 접수 기관과 처리 기관이 디른 경우 : {len(df_duplicated[df_duplicated['접수기관'] != df_duplicated['처리부서']])} ")

#시각화
import matplotlib.font_manager as fm

plt.subplot(221)
plt.scatter(df_age.index, df_age.ratio)
plt.scatter(df_age_d.index, df_age_d.ratio, alpha= 0.5)


plt.subplot(222)
x = np.array(range(len(df_gender.columns)))
w = 0.5

# df_gender.set_index([["male", 'female']], inplace = True)
# df_gender_d.set_index([["male", 'female']], inplace = True)
plt.bar(x, df_gender.ratio, width = w, label = 'All', alpha = 0.5)
plt.xticks = (x,["male", "female"])
x = x + w
plt.bar(x, df_gender_d.ratio, width = w, label = 'Duplicated', alpha = 0.5)
plt.xticks = (x,["male", "female"])
plt.legend(loc = 5)

plt.savefig("Duplicated/log/age.png")



sys.stdout.close()

