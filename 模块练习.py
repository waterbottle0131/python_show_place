#导入math模块练习（pow是幂函数用法，pow（a，b）=a的b次方，sqrt是算数平方根用法，sqrt（a）即为求a的算数平方根）
import math
#s算25的平方根
print(math.sqrt(9))
#算Π的值
print(math.pi)

from math import pow
print(pow(2,10))

#生成1到10内的随机整数
import random as rd
print(rd.randint(1,10))

from math import sqrt,pow
print(sqrt(16))
print(pow(3,4))


#导入tool.py的emotion_level函数
from tool import emotiom_level
print(emotiom_level(90))

#导入numpy模块测试
import numpy as np
print(np.sqrt(100))

#导入ceil floor 测试
from math import ceil,floor
print(ceil(3.2))
print(floor(9.3))

#datetime模块导入
from datetime import datetime
print(datetime.now())

#os模块导入
import os
print(os.getcwd())

from tool import emotiom_level
from math import sqrt
print(sqrt(144))
print(emotiom_level(75))