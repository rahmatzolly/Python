#!/usr/bin/env python
# coding: utf-8

# # LISTS

# In[87]:


#1.
a = [10,20,30,20,10,50,60,40,80,50,40]
#OUTPUT: {40, 10, 80, 50, 20, 60, 30}


# In[93]:


a = list(set(a)) #or a = set(a)


# In[103]:


a


# In[66]:


#2.
'''Write a Python program to sum all the items in a list. INPUT: [1,2,-8]
OUTPUT: -5'''


# In[113]:


n = [1,2,-8]


# In[117]:


print(sum(n))


# In[ ]:


# 3. INPUT: ['abc', 'xyz', 'aba', '1221'] OUTPUT: 2 count the number of strings from a given list of
# strings with length 2 or more and the first and last characters are the same


# In[162]:


a = ['abc', 'xyz', 'aba', '1221']


# In[163]:


new_list = [x for x in a if len(x) >= 2 and x[0] == x[-1]]


# In[133]:


op = len(new_list)


# In[134]:


op


# In[138]:


# 4. Write a Python program to print a specified list after removing the 0th,4th and 5th elements.
#INPUT:['Red','Green','White','Black','Pink','Yellow']OUTPUT:['Green','White','Black']


# In[153]:


x = ['Red','Green','White','Black','Pink','Yellow']


# In[155]:


x[1:4]


# In[156]:


# 5. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# INPUT: [7,8, 120, 25, 44, 20, 27] OUTPUT: [7,25,27]


# In[196]:


a = [7,8, 120, 25, 44, 20, 27]


# In[200]:


nw = [x for x in a if x % 2 != 0]


# In[199]:


y = print(nw)


# In[202]:


# 6. WriteaPythonprogramtogetuniquevaluesfromalist INPUT:[10,20,30,40,20,50,60,40], OUTPUT:[40,10,50,20,60,30]


# In[203]:


x = [10,20,30,40,20,50,60,40]


# In[216]:


nw = list(set(x))


# In[217]:


nw


# In[ ]:


# 7. WriteaPythonprogramtoconvertalistofcharactersintoastring.INPUT:['a','b','c','d']OUTPUT:abcd


# In[261]:


x = ['a','b','c','d']


# In[265]:


y = ''.join(x)


# In[266]:


y


# In[ ]:


# 8. WriteaPythonprogramtocalculatethedifferencebetweenthetwolists.
#INPUT:list1=[1,3,5,7,9]list2=[1,2,4,6,7,8]OUTPUT:[9,3,5,8,2,4,6]


# In[306]:


x=[1,3,5,7,9]


# In[307]:


y=[1,2,4,6,7,8]


# In[326]:


list(set(x)^set(y)) #Python Bitwise Operators XOR


# In[327]:


# 9. Write a Python program to get the frequency of elements in a list. INPUT: [1,2,3,2,4,1,3,5,2,3,4,1]
# OUTPUT: {1: 3, 2: 3, 3: 3, 4: 2, 5: 1}


# In[373]:


y = [1,2,3,2,4,1,3,5,2,3,4,1]


# In[374]:


nw = {x:y.count(x) for x in set(y)}


# In[375]:


nw


# In[376]:


# 10. Write a Python program to find common items in two lists. INPUT:
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink" OUTPUT: {'Green', 'White'}


# In[407]:


color1 = ["Red", "Green", "Orange", "White"]


# In[408]:


color2 = ["Black", "Green", "White", "Pink"]


# In[421]:


set(color1) & set(color2)


# In[ ]:


# 11. Q. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# INPUT : ['p', 'q'] and n =5
# OUTPUT: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


# In[440]:


n1 = ['p', 'q']


# In[441]:


n = 5


# In[442]:


op=[item+str(i)for i in range(1,n+1)for item in n1]


# In[443]:


op


# In[ ]:


# 12. WriteaPythonprogramtoconvertalistofmultipleintegersintoasingleinteger. INPUT:[11,33,50] OUTPUT113350


# In[467]:


nw = [11,33,50]


# In[471]:


int(''.join(str(k)for k in nw))


# In[481]:


# 13. WriteaPythonprogramtosplitalistintodifferentvariables.
'''INPUT:color=[("Black","#000000","rgb(0,0,0)"),("Red","#FF0000","rgb(255,0,0)"),
             ("Yellow","#FFFF00","rgb(255,255,0)")]
OUTPUT:Var1=('Black','#000000','rgb(0,0,0)') Var2=('Red','#FF0000','rgb(255,0,0)') 
    Var3=('Yellow','#FFFF00','rgb(255,255,0)')'''


# In[509]:


color=[("Black","#000000","rgb(0,0,0)"),("Red","#FF0000","rgb(255,0,0)"),
       ("Yellow","#FFFF00","rgb(255,255,0)")]
Var1,Var2,Var3=color
print('Var1 :', Var1)
print('Var2 :', Var2)
print('Var3 :', Var3)


# In[511]:


#Write a Python program to split a list every Nth element.
#INPUT: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] 
#OUTPUT: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# In[514]:


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


# In[517]:


N=3
op=[x [i::N] for i in range(N)]
print(op)


# # TUPLES

# In[ ]:


# 1. WriteaPythonprogramtounpackatupleintoseveralvariables.INPUT:(4,8,3)OUTPUT:A1=4 A2=8 A3-3


# In[520]:


x = (4,8,3)


# In[521]:


A1,A2,A3 = x


# In[526]:


print('A1=',A1)
print('A2=',A2)
print('A3=',A3)


# In[ ]:


# 2. WriteaPythonprogramtocheckwhetheranelement(5)existswithinatuple.
# INPUT:("w",3,"r","e","s","o","u","r","c","e") OUTPUT:FALSE


# In[528]:


x = ("w",3,"r","e","s","o","u","r","c","e")


# In[539]:


5 in x


# In[562]:


# 3. Write a Python program to reverse a tuple. INPUT: (5,10,15,20)
# OUTPUT: (20,15,10,5)


# In[563]:


x = (5,10,15,20)


# In[565]:


x[::-1]


# In[ ]:


# 4. Write a Python program to print a tuple with string formatting.
# INPUT:(100,200,300) OUTPUT:This is a tuple (100,200,300)


# In[569]:


x = (100,200,300)


# In[576]:


print('This is a tuple', x)


# In[621]:


# 5. Write a Python program to remove an empty tuple(s) from a list of tuples.
# INPUT:[(),(),('',),('a','b'),('a','b','c'),('d')]OUTPUT:[('',),('a','b'),('a','b','c'),'d']


# In[617]:


x = [(),(),('',),('a','b'),('a','b','c'),('d')]


# In[618]:


y = [t for t in x if t]


# In[620]:


y


# In[ ]:


# 6. Q.WriteaPythonprogramtoconvertagivenstringtoatuple.INPUT:“Shailja” OUTPUT:(‘’s’,’h,’a’,’i’,’l’,’j’,’a’)


# In[627]:


x = 'Shailja'


# In[632]:


tuple(x)


# In[ ]:


#### 7. WriteaPythonprogramto compute the element-wise sum of given tuples (InterviewQuestion)-MAP SUM ZIP FUNCTION
# INPUT:(1,2,3,4)(3,5,2,1)(2,2,3,1) OUTPUT:(6,9,8,6)


# In[649]:


t1 = (1,2,3,4)
t2 = (3,5,2,1)
t3 = (2,2,3,1)


# In[650]:


x = tuple(map(sum,zip(t1,t2,t3)))


# In[652]:


x


# In[653]:


# 8. WriteaPythonprogramtoconvertagivenlistoftuplestoalistoflists.INPUT:[(1,2),(2,3),(3,4)]OUTPUT:[[1,2],[2,3],[3,4]]


# In[671]:


x = [(1,2),(2,3),(3,4)]


# In[682]:


[list(t) for t in x]


# # Set

# In[683]:


# 1. SETQ.Write a Python program to remove an item from a set if it is present in the set.
# INPUT:{0,1,2,3,4,5} OUTPUT:Remove 2 from the said set:{0,1,2,3} Remove 7 from the said set:{0,1,2,3}


# In[710]:


x = {0,1,2,3,4,5}


# In[713]:


x.discard(2)


# In[714]:


x


# In[715]:


x.discard(7)


# In[716]:


x


# In[ ]:


# 2. WriteaPythonprogramtocheckifasetisasubsetofanotherset.
# INPUT:x: {'mango','apple'} y: {'mango','orange'} z: {'mango'}
# If x is subset of y:False If y is subset of z:False If z is subset of y:True


# In[775]:


x: {'mango','apple'} 
y: {'mango','orange'} 
z: {'mango'}
print('If x is subset of y:',x.issubset(y))
print('If y is subset of z:',y.issubset(z))
print('If z is subset of y:',z.issubset(y))


# In[ ]:


# 3. Write a Python program to remove all elements from a given set at once. 
#INPUT: {'Green', 'Black', 'Red', 'White'}
#OUTPUT: set()


# In[798]:


x = {'Green', 'Black', 'Red', 'White'}


# In[805]:


x.clear()


# In[806]:


x


# In[808]:


# 4.  Write a Python program to check if two given sets have no elements in common.

S1={1, 2, 3, 4}
S2={4, 5, 6, 7} 
#OUTPUT:False( as 4 is common)


# In[820]:


S1.isdisjoint(S2)


# In[ ]:


# 5. Write a Python program to check if a given value(10) is present in a set or not. INPUT:{1, 3, 5, 7, 9, 11}
# OUTPUT: False


# In[826]:


x = {1, 3, 5, 7, 9, 11}
y = 10


# In[839]:


10 in x


# In[840]:


# 6. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
# INPUT: ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises'] OUTPUT:['Solution', 'Python', 'Exercises', 'Practice']


# In[844]:


x = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']


# In[845]:


list(set(x)) # Order of output may vary as we are using set


# # Dictionary

# In[ ]:


# 1. WriteaPythonscripttoaddakeytoadictionary.Input:{0:10,1:20} Output:{0:10,1:20,2:30}


# In[912]:


x = {0:10,1:20}


# In[913]:


x[2]=30


# In[914]:


x


# In[927]:


# 2. WriteaPythonscriptto concatenatethefollowing dictionariesto createanewone.
# Input:dic1={1:10,2:20}dic2={3:30,4:40}dic3={5:50,6:60}Output:{1:10,2:20,3:30,4:40,5:50,6:60}


# In[939]:


dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}


# In[940]:


x={}


# In[941]:


x.update(dic1)
x.update(dic2)
x.update(dic3)


# In[942]:


x


# In[943]:


# 3. Writea Pythonscriptto checkwhether a givenkey(10)alreadyexistsina dictionary.
# Input:{1:10,2:20,3:30,4:40,5:50,6:60} Output:”Key10isnotpresentinthedictionary”


# In[967]:


x = {1:10,2:20,3:30,4:40,5:50,6:60}
k = 10


# In[971]:


if k in x:
    print(f'Key10ispresentinthedictionary')
else:
    print(f'Key10isnotpresentinthedictionary')


# In[ ]:


# 4. Q.WriteaPythonprogramtoremoveakey(age)fromadictionary.
# Input: 'name':'JohnDoe', 'age':30, 'occupation':'SoftwareEngineer', 'email':'john@example.com', 'is_employed':True}


# In[990]:


x = {'name':'JohnDoe', 'age':30, 'occupation':'SoftwareEngineer', 'email':'john@example.com', 'is_employed':True}


# In[991]:


x


# In[993]:


del x["age"]


# In[994]:


x


# In[995]:


# 5. WriteaPythonprogramto removeduplicatesfromthe dictionary(InterviewQuestion)
# Input:{'a':1,'b':2,'c':1,'d':3,'e':2,'f':4} Output:{'a':1,'b':2,'d':3,'f':4}


# In[1079]:


x = {'a':1,'b':2,'c':1,'d':3,'e':2,'f':4}


# In[1080]:


temp=[]
op_d={}
for key,val in x.items():
    if val not in temp:
        temp.append(val)
        op_d[key]=val
op_d
#print("AfterRemovingDuplicates:"+str(op_d))


# In[1063]:


# 6. WriteaPythonprogramtogetthe maximum and minimum valuesofadictionary.
# Input:{‘u’:1000,’v’:3000,'x':500,'y':5874,'z':560} Output:Grow Data Skills


# In[1071]:


x = {'u':1000,'v':3000,'x':500,'y':5874,'z':560}


# In[1072]:


maxm = max(x.values())


# In[1073]:


maxm


# In[1074]:


minm = min(x.values())


# In[1075]:


minm


# In[1076]:


# 7. WriteaPythonprogramto checkifa dictionary is emptyornot.Input:my_dict={} Output:”DictionaryisEmpty"


# In[1095]:


x = {}


# In[1096]:


if not x:
    print("DictionaryisEmpty")
else:
    print("DictionaryisnotEmpty")


# In[1111]:


# 8. WriteaPythonprogramto createa dictionaryof keys x,y,andz where each keyhasas valuealistfrom11-20,21-30,and31-40
# respectively.Accessthefifthvalueofeachkeyfromthedictionary.Input:{'x':[11,12,13,14,15,16,17,18,19],
# 'y':[21,22,23,24,25,26,27,28,29], 'z':[31,32,33,34,35,36,37,38,39]} Output:15 25 35


# In[1112]:


k = {'x':[11,12,13,14,15,16,17,18,19],
    'y':[21,22,23,24,25,26,27,28,29], 
        'z':[31,32,33,34,35,36,37,38,39]}
    


# In[1113]:


k


# In[1128]:


vx=k['x'][4]
vy=k['y'][4]
vz=k['z'][4]


# In[1123]:


print(vx)
print(vy)
print(vz)


# In[ ]:


# 9. WriteaPythonprogram to drop empty itemsfroma givendictionary.
# Input:{'c1':'Red','c2':'Green','c3':None} Output:{'c1':'Red','c2':'Green'}


# In[1168]:


x = {'c1':'Red','c2':'Green','c3':None}


# In[1170]:


op={key:value for key,value in x.items() if value is not None}
print(op)


# In[1176]:


# 10. WriteaPythonprogramtofiltera dictionary based on values>170
# Input:{'CierraVega':175,'AldenCantrell':180,'KierraGentry':165,'PierreCox':190}
    # Output:{'CierraVega':175,'AldenCantrell':180,'PierreCox':190}


# In[1175]:


x = {'CierraVega':175,'AldenCantrell':180,'KierraGentry':165,'PierreCox':190}


# In[1178]:


op={key:value for key,value in x.items() if value > 170}
print(op)


# In[1179]:


# 11. WriteaPythonprogramto verifythat allvaluesina dictionaryarethe same (InterviewQuestion)
# Input:{'CierraVega':12,'AldenCantrell':12,'KierraGentry':12,'PierreCox':12} Output:“Allvaluesare12


# In[1211]:


x = {'CierraVega':12,'AldenCantrell':12,'KierraGentry':12,'PierreCox':12}


# In[1212]:


if len(set(x.values())) == 1:
    print("allvaluesare same:", list(set(x.values()))[0])
else:
    print("Valuesarenotthesame")


# In[1214]:


# 12. WriteaPythonprogramtoconvertstringvaluesofagivendictionaryintointeger/floatdatatypes.
# INPUT:[{'x':'10','y':'20','z':'30'},{'p':'40','q':'50','r':'60'}]
# OUTPUT:Stringvaluesofa givendictionary,into integertypes:[{'x':10,'y':20,'z':30},{'p':40,'q':50,'r':60}]
# Stringvaluesofa givendictionary,into floattypes:[{'x':10.12,'y':20.23,'z':30.0},{'p':40.0,'q':50.19,'r':60.99}]


# In[1216]:


x = [{'x':'10','y':'20','z':'30'},{'p':'40','q':'50','r':'60'}]


# In[1222]:


op1=[{key:int(value) for key,value in d.items()} for d in x ]
print(op1)


# In[1223]:


op2=[{key:float(value) for key,value in d.items()} for d in x ]
print(op2)


# In[1224]:


# 13. WriteaPythonprogramto filter evennumbersfroma dictionaryof values.
# INPUT:{'V':[1,4,6,10],'VI':[1,4,12],'VII':[1,3,8]} OUTPUT:{'V':[4,6,10],'VI':[4,12],'VII':[8]}


# In[1225]:


x = {'V':[1,4,6,10],'VI':[1,4,12],'VII':[1,3,8]}


# In[1231]:


op={key:[num for num in value if num%2==0] for key,value in x.items()}
print(op)


# # STRINGS

# In[1233]:


# 1. Q. Write a Python program to count the number of characters (character frequency) in a string.
# INPUT: google.com OUTPUT: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


# In[1279]:


x = 'google.com'


# In[1286]:


op = {k:x.count(k) for k in x}


# In[1287]:


op


# In[1316]:


# 2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
'''If the string length is less than 2, return the empty string instead.
INPUT: 'w3resource' OUTPUT : 'w3ce'
INPUT: 'w3' OUTPUT: 'w3w3' '''


# In[1348]:


x1 = 'w3resource'


# In[1349]:


x1[:2] + x1[-2:] if len(x1)>=2 else""


# In[1350]:


x2 = 'w3'


# In[1351]:


x2[:2] + x2[-2:] if len(x2)>=2 else""


# In[ ]:


# 3. WriteaPythonprogramtoremovethe5th indexcharacterfrom a nonempty string.


# In[1366]:


x = 'Python'


# In[1371]:


x[:5]+x[6:]


# In[1372]:


# 4. WriteaPythonprogramto countthe occurrencesof eachwordina givensentence.
#INPUT:‘thequickbrownfoxjumpsoverthelazydog.’
#OUTPUT:{'the':2,'jumps':1,'brown':1,'lazy':1,'fox':1,'over':1,'quick':1,'dog.':1


# In[1381]:


x = 'the quick brown fox jumps over the lazy dog.'


# In[1391]:


y = x.split()


# In[1392]:


y


# In[1398]:


z = {k:y.count(k)for k in set(y)}


# In[1399]:


z


# In[1397]:


type(z)


# In[1400]:


# 5. WriteaPythonfunctionto inserta stringinthe middleofa string


# In[1443]:


x = ('[[]]','Python') # OUTPUT:[[Python]]


# In[1444]:


ori='[[]]'
ins='Python'
mid=len(ori)//2
op=ori[:mid]+ins+ori[mid:]


# In[1425]:


op


# In[1445]:


# 6. WriteaPythonfunctionto reversea stringifits lengthisa multipleof 4.INPUT:’python’ OUTPUT:’python


# In[1463]:


x = 'python'


# In[1464]:


x[::-1] if len(x)%4==0 else x


# In[1466]:


# 7. Write a Python program to check whether a string starts with specified characters (grow)


# In[1467]:


x = 'growdataskills'


# In[1470]:


s = 'grow'


# In[1473]:


op = x.startswith(s)


# In[1474]:


op


# In[1486]:


# 8. WriteaPythonprogramto reverse words ina string.
# INPUT:"The quick brown fox jumps over the lazy dog."
# OUPUT:“dog.lazy the over jumps fox brown quick The”


# In[1493]:


x = "The quick brown fox jumps over the lazy dog."


# In[1502]:


y = x.split()


# In[1503]:


y


# In[1501]:


" ".join(reversed(y))


# In[1525]:


# 9. WriteaPythonprogramto checkwhethera stringcontains all lettersofthe alphabet(InterviewQuestion).
# INPUT:'The quick brown fox jumps over the lazy cat'


# In[1508]:


x = 'The quick brown fox jumps over the lazy cat'


# In[1512]:


y = set('abcdefghijklmnopqrstuvwxyz')


# In[1513]:


y


# In[1522]:


(x.lower())


# In[1524]:


set(x.lower())>=y


# In[1526]:


# 10. WriteaPythonprogramto count and display vowels in text.
# INPUT:resource
# OUTPUT:4-> ['e','o','u','e]


# In[1527]:


x = 'resource'


# In[1528]:


v = 'aeiou'


# In[1529]:


vowel_count = sum(char in v for char in x)


# In[1530]:


vowel_list=[char for char in x if char in v]
print(vowel_count,'->',vowel_list)

