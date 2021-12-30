#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1, 2, 3, 4, 5]


# In[2]:


#리스트 주소값 확인
id(list1)


# In[3]:


#리스트 값 추가
list1.append(6)


# In[4]:


#리스트 주소값 확인
id(list1)


# In[5]:


#리스트에 새로운 값 할당
list1 = [1, 2, 3, 4]
id(list1)


# In[6]:


#리스트 2를 리스트 1에 넣으면 주소값도 같다
list2 = list1
id(list2)


# In[7]:


#다른 주소로 값만 가져오기
#.copy() : 값만 가져오는 기능
list3 = list1.copy
id(list3)


# In[8]:


print('list1 : ', list1)
print('list2 : ', list2)


# In[9]:


#list2.append(5)
list1.append(6)


# In[10]:


print('list1 : ', list1)
print('list2 : ', list2)


# In[11]:


str1 = '문자열'
type(str1)


# In[12]:


int1=60
type(int1)


# # 리스트

# In[13]:


# remove, insert, pop, append, count, len, reverse, sort, indexing,slicing, index..............
# 라이브러리에서는 인덱싱, 슬라이싱  가장 중요하게 사용,  append, remove,


# In[14]:


#1~50 까지가 담긴 리스트
nlist=[]
for i in range(1,51):
    nlist.append(i)#리스트 값 추가
print(nlist)


# In[15]:


# 인덱싱 슬라이딩

# 대괄효[]

# 10 출력하기
print(nlist[9])
# 15~25 출력하기
nlist[14:25]


# In[16]:


#   \n 개행
str1='asdf\nsdf'
str1


# In[17]:


print(str1)


# In[18]:


# print :  원하는 위치에서 출력 가능 : 실행
# 변수명 출력: 마지막 위치에서만 가능 : 출력


# In[19]:


list1


# In[20]:


print(list1)


# # 딕셔너리
# - key, value 로 이루어짐

# In[21]:


#dic_team 변수명을 사용해서 딕셔너리 만들기
# 이름 나이 Key 값 사용    ###나이 좀 하지마..ㅜㅠ
#팀원들의 정보


# In[22]:


#dic_team={'이름 : 나영','나이: 2'}


# In[23]:


dic_team = {
    '이름' : ['상민','하라','지은','현도','나영'],
    '나이' : [20,21,22,23,24,25] 
}

