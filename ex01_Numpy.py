#!/usr/bin/env python
# coding: utf-8

# In[2]:


# numpy 라이브러리 import하기
# 앞으로 np라는 이름으로 부르기
import numpy as np


# In[3]:


list1=[1,2, 3, 4, 5]
list1


# In[4]:


#array생성하기
arr=np.array(list1)
arr


# In[5]:


arr1 = np.array([1,2,3,4,5])
arr1


# In[6]:


#리스트
#[1,2,3] , [4,5,6] 각 요성의 값을 더한다.


# In[7]:


list1 = [1,2,3]
list2 = [4,5,6]


# In[8]:


arr3 = np.array(list1)
arr4 = np.array(list2)


# In[9]:


arr5 = arr3 + arr4
arr5


# In[10]:


#list3=[]
#for i in range(3):
#    list3.append(list1[i]+list2[i])
#list3


# In[ ]:





# In[11]:


#2차원 array 생성하기
arr6 = np.array( [ [ 1,2,3 ],[ 4,5,6 ] ] )
arr6


# In[12]:


#array 의 크기 확인하기
#shape
arr6.shape


# In[13]:


#array전체 요소 개수 확인하기
#size 
arr6.size


# In[14]:


#array 타입 확인하기
#dtype
arr6.dtype


# In[15]:


#array 차원 확인하기
#ndim
arr6.ndim


# In[16]:


#3차원의 array 만들고 배열의 크기, 차원 , 전체 요소 개수 확인
arr7 = np.array(   [   [   [1,2],[3,4]   ],[   [5,6],[7,8]   ]   ]   )
arr7


# In[17]:


print('배열의 크기', arr7.shape)


# In[18]:


print('배열의 요소개수' , arr7.size)


# In[19]:


print('배열의 차원', arr7.ndim)


# In[20]:


print('배열의 타입', arr7.dtype)


# In[21]:


print('배열의 크기:{}'.format(arr7.shape))
print(f'배열의 차원:{arr7.ndim}')
print('배열의 개수:', arr7.size)


# In[22]:


#배열 생성하기

# 0의 값으로 배열 생성하기  => 0으로 초기화
# zeros(배열의 크기)
np.zeros((3,4))


# In[23]:


# 1 값으로 생성하기 => 1호 초기화
#ones()
np.ones((3,4))


# In[24]:


#지정해서 생성하기
#full(배열의 크기, 채워넣을 값)
np.full((3,4),5)
       # 3개의 배열 4개의 값이 들어갈수 있게 , 5 라는 값으로 넣어서 만들어라~~~  


# In[25]:


#연속되는 숫자로 배열 생성하기
#arange( 시작하는 수, 끝나는 수 +1, 간격이 되는 수)
#시작되는 수 기본 값 : 0
#간격이 되는 수 기본값 :1
np.arange(1, 50+1, 10)


# In[26]:


np.arange(1, 50, 10)


# In[27]:


np.arange(1,42,10)


# In[29]:


#1부터 50까지 1씩 커지는 배열 만들기
#np.linspace(시작하는수, 끝나는 수, 등분할 값)

#같은 간격만틈의 배열을 만들때 사용

np.linspace(1,50,50)


# In[31]:


#for문으로 사용할 수 있다. 
for i in np.linspace(1,50,20):
    print(i)


# In[32]:


#랜덤값으로 배열 생성하기
# np.random.rand(배열의 크기)
# 0 ~ 1 사이의 값을 가지는 배열을 생성
np.random.rand(2,3)


# In[34]:


#내가 원하는 범위 안에서 랜덤값 생성
#np.random.randit(시작수, 끝수+1, size = 배열의 크기)

np.random.randint(2,10,size=(3,2))


# In[38]:


#2부터 10까지의 런덤 실수값으로 이루어진 (5,4) 크기의 배열 생성

np.random.rand(2,10) , np.random.randint(2,10, size=(5,4))


# In[40]:


#정수+소수점 = 실수
정수 = np.random.randint(2,10 , size=(5,4))
정수


# In[41]:


소수점 = np.random.rand(5,4)
소수점


# In[42]:


실수=정수+소수점
실수


# In[47]:


abc = np.random.rand(5,4) + np.random.randint(2,10, size=(5,4))
print(abc)


# In[ ]:





# In[ ]:


#타입 변경하기
# 배열.astype(변경할 타입)


# In[44]:


실수.astype('int')


# In[ ]:


#배열의 생성


# In[ ]:


#배열의 기능


# In[48]:


arr=np.array([[1,2,3],[4,5,6]])
arr


# In[53]:


#인덱싱
#[대괄호]
# 2차원에서 0번째 출력
arr[0]
arr[0][1]


# In[54]:


arr[0,1]
#2차원에서 1번 선택해서 1차원에서 1번째 선택


# In[ ]:


#슬라이싱


# In[ ]:


#0~9 까지의 값이 담긴 배열 생성


# In[56]:


arr1 = np.arange(10)
arr1


# In[ ]:


# 3부터 7까지의 값 출력


# In[61]:


arr1[3:8]


# In[62]:


#2차원 슬라이싱
# 0~49까지 정수의 값이 담겨있는 array생성하기
arr2=np.arange(50)
arr2


# In[66]:


#arr2를 (5,10)으로 재 배열하기
#reshape
#바뀌기 전과 후의 데이터 수가 똑같아야함

#arr2.reshape(5,10)
#출력을 진행하고 저장은 진행되지 않음, 변수에 담아줘야 저장이 됨
arr2 = arr2.reshape(5,10)


# In[67]:


#2차원 슬라이싱
arr2


# In[ ]:


# [고차원, 1차원]


# In[ ]:


#어떤식의 인덱스 번호가 부여 되어 있는지 확인 
#


# In[68]:


arr2[0:2]


# In[69]:


arr2[0:2, 0:10]   #위와 같은 출력


# In[70]:


#전체 출력
#시작수 : 끝수+1
# : 끝수 +1 =처음부터 끈수까지
# 시작수 : = 시작수부터 끝까지
# : = 처음부터 끝까지
arr2[0:2, :]


# In[75]:


arr2[0:4, 0:5]   #[:4, :5]


# In[74]:


arr2[0:5, 0:1]   #[:,0]


# In[ ]:


# 위 키(cm)
#아래 몸무게(kg)
# 10개의 데이터
#bmi 계산하기


# In[78]:


#파일 불러오기

data = np.loadtxt('height_weight.txt', delimiter=',')
data


# In[1]:


bmi=[]

for i in range(0,10):
    bmi.append(data[1,i]/(data[0,i]/data[0,i]*10000)

print(bmi)


#print(round(bmi, 8))  소수점 맞추어 주기


# In[131]:


d = "format example4 : {1:.2f} / {0:.1f}".format(3.22521321, 10.123456)
print(d)


# In[88]:


height=data[0] /100
weight=data[1]
bmi = weight/ height**2
bmi


# In[95]:


키_cm = data[0]
키_cm


# In[99]:


키_m = 키_cm /100
키_m


# In[97]:


몸무게 = data[1]
몸무게


# In[101]:


몸무게 / (키_m*키_m)


# # Boolean 인덱싱
# #True 는 출력하고 False 는 출력하지 않음
# #인덱싱을 진행할떄 개수와 동일한 수의 Boolean data필요
# #원하는 조건에 맞는 값을 출력하는 방법

# In[110]:


arr3 = np.array([10,20,15,30])
arr3


# In[ ]:


# 20,30 F  , 10,15 T


# In[111]:


bol=np.array([True, False, True, False])   #비효율적
bol


# In[112]:


arr3[bol]


# In[113]:


arr3 < 17


# In[115]:


arr3[bol]


# In[114]:


#17미만의 값만 출력
arr3[arr3<17]


# In[119]:


# arr3 에서 20인 값만 출력

print(arr3 == 20)


# In[121]:


print(arr3[arr3 == 20])


# In[120]:


arr3[arr3 == 20]


# In[118]:


arr3[arr3 != 20]


# In[ ]:


# numpy에서 사용하는 연산 함수


# In[ ]:


#1~9 까지의 랜덤한 수가 담긴 (2,5) 크기의 배열 생성


# In[123]:


arr = np.random.randint(1,10,size=(2,5))
arr


# In[126]:


#배열 안에 있는 값 더하기
#np.sum(배열값)
np.sum(arr)


# In[127]:


np.sum(arr, axis = 0)
#axis 각 요소 끼리 1차원 0, 


# In[128]:


np.sum(arr, axis = 1)
# 2차원일경우 1 


# In[129]:


#배열 안에 있는 값의 평균
#np.mean(배열값)

np.mean(arr)


# In[130]:


np.mean(arr,axis = 1)


# # 영화 평점 데이터로 분석해보기

# In[186]:


import numpy as np


# In[132]:


#파일 불러오기   (6040 유저)

movie_data = np.loadtxt('ratings.txt', delimiter='::')
movie_data


# In[133]:


#데이터 타입 변경
#dtype
movie_data = np.loadtxt('ratings.txt', delimiter='::', dtype = 'int')
movie_data
#   id(user),  영화번호,      평점 , 영화시간 (사용하지 않음)


# In[134]:


#전체 평점 평균 구하기
# 1) 평접 인덱싱   2) 평균내기
#  2차원 전체, 
movie_data[:,2]


# In[135]:


np.mean(movie_data[:,2])


# In[141]:


# 각 사용자별 평점 평균 구하기
# 리스트에 [사용자, 사용자의 평점평균]
# 유저                         # 평점
m_avg = movie_data[:,0]+movie_data[0:6041,2:3]
m_avg


# In[139]:


movie_data[:,0]


# In[ ]:


#전체 정보에서 id값이 1인 값만 출력
movie_data[movie_data[:,0]==1]
#출력 된 값에서 평점값만 추출한 후 평균 구하기

for i in range(movie_data[:,0]==i, i < 6041):
    print(np.mean(movie_data[:,2]))


# In[145]:


#전체 정보에서 id값이 1인 값만 출력
user_list = []
user = movie_data[movie_data[:,0]==1]
#출력 된 값에서 평점값만 추출한 후 평균 구하기
#np.mean(user[:,2])  # 1번 사용자에 대한 평점 평균
user_list.append([1,np.mean(user[:,2])])
user_list


# In[175]:


user_list=[]
for i in range(1,6041):
    user = movie_data[movie_data[:,0]==i]   ##반복될떄마다 다른 유저 의 정보를 출력
    user_list.append([i,np.mean(user[:,2])])
user_list


# In[176]:


np.size(user_list)


# In[ ]:


# 각 사용자별 평균 평점이 4점 이상인 사용자 구하기


# In[177]:


user_list_arr = np.array(user_list)
user_list_arr[user_list_arr[:,1] >= 4][:,0]
user_list_arr


# In[188]:


user_list_arr = np.array(user_list)
user_list_arr[user_list_arr[:,1] >= 4][:,0].astype('int')


# In[178]:


# 쌤 풀이
user_np=np.array(user_list)
user_np


# In[179]:


over4bol = user_np[:,1]>=4


# In[180]:


user_np[over4bol,0]


# In[181]:


user_np[over4bol,0].astype('int')

