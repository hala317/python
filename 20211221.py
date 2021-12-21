#!/usr/bin/env python
# coding: utf-8

# # 파이썬

# In[2]:


1+3


# In[4]:


print(-10)


# In[5]:


print(2+8)


# In[6]:


print(3*8)


# In[8]:


print("안녕하세요")


# In[9]:


print('hello world!')


# In[10]:


print(5<10)


# In[11]:


print(10<5)


# In[12]:


num=3
print(num)


# num1=13
# num2=25
# num3=77

# In[13]:


a, b = 10, 15
print(a)
print(b)


# In[14]:


#str1 python 대입, str2 python 대입!!!
str1 = str2 = 'python'
print(str1)
print(str2)


# In[15]:


x=100
y=200
sum =x+y
print(sum)


# In[18]:


a= 'she\'s gone'
print(a)


# In[22]:


#개행 
s1 = "자세히 보아야 예쁘다. \n 오래 보아야 사랑스럽다. \n 너도 그렇다"
print(s1)

s1 = """자세히 보아야 예쁘다. 
오래 보아야 사랑스럽다. 
너도 그렇다"""
print(s1)


# # 인덱싱

# In[25]:


name = 'My name is Harah'
print(name[8])
print(name[-5])


# # 슬라이싱

# In[34]:


print(name[11:15])  #이름 가져오기

print(name[3:7])  #name 가져오기

print(name[-16:-9])  #뒤에서 읽기

print(name[:])  #전체 문자열 가져오기


# In[40]:


day = '2021년 12월 21일의 날씨는 맑음입니다.'
#날짜 : 2021년 12월 21일
# 날씨 : 맑음

print('날짜:', day[:13])
print('날씨:', day[-6:-4])

print('날씨:', day[19:21])


# # 문자열 포맷팅

# In[45]:


#오늘은 12월 21이 입니다
day = 24
s = '오늘은 12월 %d일 입니다.' %day
print(s)


# In[44]:


s= '오늘은 12월 {}일 입니다.' .format(day)
print(s)


# In[49]:


s=f'오늘은 12월 {day}일 입니다'
print(s)


# In[58]:


x=100
y=200
sum2=x+y
print(x,'와 ',y,'의 합은 ',sum2,'입니다' )
print('{}와 {}의 합은 {}입니다'.format(x,y,sum2))
print('%d와 %d의 합은 %d입니다.' %(x,y,sum2))
print(f'{x}와 {y}의 합은 {sum2}입니다.')


# In[ ]:


#마크 다운 이미지 넣기


# In[ ]:





# In[ ]:





# # 산술연산자

# In[60]:


num1 = 10
num2 = 7
print(num1/num2)
print(num1%num2)
print(num1//num2)


# In[61]:


print(num1+num2)


# In[64]:


str1='안녕'
str2='하세요'
print(str1+str2)
str3='10'
str4='7'
print(str3+str4)


# In[65]:


str1='10'
num3=7
print(int(str1)+num3)   #형변환
print(str1+str(num3))


# In[67]:


num1=23
num2=3


# In[68]:


print(num1)


# In[69]:


num1=23
num2=3
print('더하기결과 : ',num1+num2)
print('빼기결과 : ',num1-num2)
print('곱하기결과 : ',num1*num2)
print('나누기결과 : ',num1/num2)


# In[ ]:





# In[ ]:





# In[ ]:




