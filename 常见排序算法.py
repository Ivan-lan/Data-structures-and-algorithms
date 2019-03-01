
# coding: utf-8

# ## 排序算法的Python实现

# 参考： https://zhuanlan.zhihu.com/p/40695917, 《数据结构与算法--Python语言描述》
# 
# 主要介绍插入排序、选择排序、冒泡排序、快速排序和归并的思想，实现代码全部采用 Python 实现。

# ### 准备工作
# 所谓 “磨刀不误砍柴工”，在进行排序算法练习的时候，我们需要做一些准备的工作：
# 
# - 生成算法需要的数列：随机数列
# - 对于一些极端情况，考虑算法的效率，需要生成基本有序的数列
# - 测试算法性能的函数
# - 判断数列是否有序
# - 数列中元素相互交换
# - 数列的拷贝

# In[3]:


#生成随机数列
#coding=utf-8
from random import randint
def generateRandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr


# In[4]:


# 生成基本有序的数列
def generateNearlyOrderedArray(n, swapTimes):
    arr = []
    for i in range(n):
        arr.append(i)
    for j in range(swapTimes):
        posx = randint(0, n-1)
        posy = randint(0, n-1)
        arr[posx], arr[posy] = arr[posy], arr[posx]
    return arr


# In[5]:


# 判断数列是否有序（算法是否正确）
def isSorted(alist):
    for i in range(0, len(alist)-1):
        if alist[i] > alist[i+1]:
            return False
    return True


# ### 插入排序
"""
插入排序的算法复杂度是 O(n^2)，其工作原理是总是保持一个位置靠前的已排好的子表，然后每一个新的数据项被 “插入” 到前边的子表里，
排好的子表增加一项。我们认为只含有一个数据项的列表是已经排好的。每次选择后面未排序的一个数据（从 1 开始到 n-1），
这个数和左边已排好的子表中的数比较。把之前已经排好的列表中比这个数据大的移到它的右边。当子表的数小于等于当前数，
或者当前数已经和子表的所有数据比较了时，就可以在此处插入当前数据项。
"""
# In[2]:


def insert_sort(lis):
    for i in range(1, len(lis)):
        cur = lis[i] # 记录当前数
        idx = i # 用来比较的指针
        while idx > 0 and lis[idx-1]>cur: # 循环停止条件：和所有元素比较或遇到小于等于当前元素
            lis[idx]=lis[idx-1]  # 比当前元素大的元素右移
            idx -= 1 # 指针左移检查下一个
        lis[idx]=cur  # 插入合适的位置
    return lis


# In[9]:


lis = generateRandomArray(10,1,20)
lis


# In[10]:


lis = insert_sort(lis)
lis


# In[11]:


isSorted(lis)


# 在插入排序中，每次处理哪个记录并不重要，关键在于将被处理的记录插入已排序序列的正确位置，因此可以采用最方便的方式取记录，即按顺序提取。
# 
# 选择排序的想法则是每次选择合适的记录，只要严格按递增的方式选出记录（每次选出最小的元素），简单地顺序排放即可完成排序工作。

# ### 选择排序
# 
# 每次遍历所有未排序的元素，选择最小的元素，和未排序部分的第一个元素交换位置。遍历n-1次。
# 
# 两重循环，第一层控制扫描次数，第二层扫描未排序的元素，寻找最小值。

# In[14]:


def select_sort(lis):
    for i in range(len(lis)-1):
        min_idx = i # 记录最小值的索引
        for j in range(i, len(lis)):
            if lis[j]<lis[min_idx]:
                min_idx = j # 寻找最小值下标
        lis[i], lis[min_idx] = lis[min_idx], lis[i] # 交换未排序的第一个元素和最小元素
    return lis


# In[15]:


lis = generateRandomArray(10,1,20)
lis


# In[16]:


lis = select_sort(lis)
lis


# In[17]:


isSorted(lis)


# ### 交换排序-冒泡排序
"""
# 交换排序的思想是：认为一个序列的记录没排好序，那么其中一定有逆序存在，如果交换所发现的逆序记录对，
得到的序列将更接近排序序列，通过不断减少序列中的逆序，最终得到排序序列。
# 
# 冒泡排序通过比较相邻记录，发现相邻的逆序对时就交换，通过反复比较和交换，最终完成排序。
如果序列中每对相邻记录的顺序正确，整个序列就是排序的。
# 
# 从左到右的顺序比较一对对相邻记录，发现逆序立马交换，再做下一次比较，每一遍检查都会将最大的元素移动
到未排序部分的最后，通过一遍遍扫描，表的最后将累积越来越多的排好序的大元素。每遍扫描，这段元素增加一个，
经过n-1遍扫描，一定能完成排序。
"""
# In[24]:


def bubble_sort(lis):
    for i in range(len(lis)):
        for j in range(1,len(lis)-i):
            if lis[j-1]>lis[j]:
                lis[j-1],lis[j]=lis[j],lis[j-1]
    return lis


# In[25]:


lis = generateRandomArray(10,1,20)
lis


# In[26]:


lis = bubble_sort(lis)
lis

"""
扫描有时不需要做那么多次，如果发现排序已经完成就可以早结束，如果在一次扫描中没遇到逆序，说明排序工作已经完成，可以提前结束。
 
在外层循环里加一个标识变量flag，在内层循环开始之前将flag赋值为False，如果扫描检查中遇到逆序，就赋值为True，
在内层循环结束后检查flag，其值为False表示未发现逆序，立刻结束循环。
"""
# In[27]:


def bubble_sort2(lis):
    for i in range(len(lis)):
        flag = False
        for j in range(1,len(lis)-i):
            if lis[j-1]>lis[j]:
                lis[j-1],lis[j] = lis[j],lis[j-1]
                flag=True
        if not flag:
            break
    return lis


# In[28]:


lis = generateRandomArray(10,1,20)
lis


# In[29]:


lis = bubble_sort2(lis)
lis


# ### 快速排序
"""
# 快速排序也采用发现逆序和交换记录位置的方法，基本思想是：划分，即按某种标准将考虑的记录划分为：小记录和大记录，
并通过递归不断划分，最终得到一个排序的序列。
# 
# 基本过程：
# 
# - 选择一种标准，将被排序序列中的记录按这种标准划分为大小两组，小的组排在前面
# - 采用同样的方式，递归地分别划分得到的两组记录，继续递归地划分下去
# - 划分总是得到越来越小的分组，如此工作下去直到每个记录组中最多包含一个记录时，整个序列的排序完成
# 
# 实现：
# 
# 利用两个指针i和j，其初值为序列的第一个和最后一个记录的位置。划分过程中，他们的值交替地作为空位和下一被检查记录的下标。
取第一个记录，作为划分标准。交替进行下面两套操作：
# 
# - 从右到左逐个检查j一边的记录，检查中j值不断减一，直到找到第一个值小于标准的记录，将其存入i所指向的空位，
移动后j位置变为空，i值加一指向下一位
# - 从左到右检查i一边的记录，检查中i值不断加一，直到找到第一个大于标准的记录，将其存入j所指向的位置。
# - 重复交替地进行上述两套操作，直到i不再小于j为止。
# - 划分结束时，i与j值相等，指向表中的空位，将最先选取的标准存入。
# 
# 一次划分完成后，对两边的子序列按同样的方式递归处理。
"""
# In[49]:


def quick_sort(lis):
    qsort(lis, 0, len(lis)-1)
    return lis

def qsort(lis, l, r):
    if l>=r:
        return
    i = l
    j = r
    pivot = lis[i]
    while i<j:
        while i<j and lis[j]>=pivot:
            j -= 1
        if i<j:
            lis[i]=lis[j]
        while i<j and lis[i]<=pivot:
            i += 1
        if i<j:
            lis[j]=lis[i]
    lis[i]=pivot
    qsort(lis,l,i-1)
    qsort(lis,i+1,r)


# In[50]:


lis = generateRandomArray(10,1,20)
lis


# In[51]:


lis = quick_sort(lis)
lis


# ### 快排的简单实现
"""
# 选取一个记录作为划分标准，将表中记录分为两组。工作过程中，本分段的记录（除标准外）顺序分为三段：小记录，大记录和未检查记录。
用两个指针，i的值总是最后一个小记录的下标，j的值是第一个未处理记录的下标。每次迭代比较标准和待检查的值j，有两种情况：
# 
# - 记录j较大，简单将j加一
# - 记录j较小，需要将记录调到左边，方法是i加一，交换i和j的值，将j加一
# - 最后还需要将标准放在正确的位置，只需交换与i的记录即可。此时，在标准之前的值都小于标准，在标准之后的值都大于标准。再递归处理分段。
# 
# 因为要检查的范围已知，用for循环即可。
"""
# In[52]:


def quick_sort1(lis):
    
    def qsort(lis,l,r):
        if l>=r:
            return
        pivot = lis[l]
        i = l
        for j in range(l+1,r+1):
            if lis[j]<pivot:  # 发现小的数
                i+=1   
                lis[i],lis[j]=lis[j],lis[i] # 交换小的数到左边
        lis[i],lis[l]=lis[l],lis[i] # 将标准放到正确的位置
        
        qsort(lis,l,i-1)
        qsort(lis,i+1,r)
    
    qsort(lis,0,len(lis)-1)
    return lis


# In[53]:


lis = generateRandomArray(10,1,20)
lis


# In[54]:


lis = quick_sort1(lis)
lis


# ### 归并排序
"""
# 归并排序的工作分为几个层次：最上层控制一遍遍归并，完成整个表的排序工作；在一遍处理中，需要分别完成一对对递增序列的归并；
在归并每一对序列中，又需要一个个地处理序列元素。
# 
# - 最下层：实现表中相邻的一对有序序列的归并工作，将归并结果存入另一个顺序表的相同位置
# - 中间层：基于操作1（一对序列的归并操作），实现对整个表里顺序各对有序序列的归并，完成一遍归并，并对序列的归并结果存入
另一顺序表的同位置分段
# - 最高层：在两个顺序表之间往复执行操作2，完成一遍归并后交换两个表的地位，然后再重复操作2的工作，直到表整个表里只有
一个有序序列时排序完成。
"""
# In[82]:


def merge(l1,l2,low,mid,high): # 将一对分段排序合并
    i, j, k = low,mid,low
    while i<mid and j<high:
        if l1[i]<=l1[j]:
            l2[k]=l1[i]
            i+=1
        else:
            l2[k]=l1[j]
            j+=1
        k+=1
    while i<mid:
        l2[k]=l1[i]
        i+=1
        k+=1
    while j<high:
        l2[k]=l1[j]
        j+=1
        k+=1

def merge_pass(l1, l2, llen, slen):
    
    i = 0
    while i+2*slen < llen: # 归并一对长为slen的分段
        merge(l1,l2,i,i+slen,i+2*slen)
        i += 2*slen
        
    if i+slen<llen: # 剩下两段，后段的长度小于slen
        merge(l1,l2,i,i+slen,llen)
        
    else: # 只剩下一段
        for j in range(i,llen):
            l2[j]=l1[j]

def merge_sort(lis):
    slen,llen = 1, len(lis)
    temp = [None]*llen
    while slen<llen:
        merge_pass(lis,temp,llen,slen)
        slen *= 2
        merge_pass(temp,lis,llen,slen)
        slen *= 2
    return lis


# In[83]:


lis = generateRandomArray(10,1,20)
lis


# In[84]:


lis = merge_sort(lis)
lis

